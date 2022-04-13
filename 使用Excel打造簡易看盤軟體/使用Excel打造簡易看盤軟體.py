#!/usr/bin/env python
# coding: utf-8

# # 主題：使用EXCEL打造簡易看盤軟體(以0050前五大持股為例)
# ## 一、  製作投資組合簡易看盤軟體。(資料來源：Yahoo Finance)
# #### 　　1. 蒐集資料：開盤、最高、最低、收盤、成交量
# #### 　　2. 繪製技術指標：近一個月的K線、MA5、MA10、MA20、BBAND
#     
# ## 二、 交易期間擷取股價資訊並繪製走勢圖(資料來源：富果Realtime API)
# #### 　　1. 擷取昨日收盤價(一次)
# #### 　　2. 每60秒更新目前成交價、五檔、走勢圖
# 
# ## 三、 若有較大的漲跌幅就發Line提醒自己
# #### 　　1. 權值股以2%為例(並非實際投資策略)
# #### 　　2. 配合股價資訊，使用LineNotification提醒
# 
# ## 四、 收盤時自動擷取當日交易資料儲存回CSV
# #### 　　1. 使用fugle API擷取收盤資訊
# #### 　　2.  更新完成後發line通知自己
# 

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlwings as xw
import requests
import time

wb = xw.Book("簡易Excel看盤軟體.xlsx")
stock_sheets = list(wb.sheets)[2:]
stock_ids = wb.sheets["股票代號清單"].range("A1").expand("down").value
stock_sheet_names = [sheet.name for sheet in stock_sheets]
for stock in stock_ids:
    if not stock in stock_sheet_names:
        wb.sheets["公版"].copy(name = stock, after = wb.sheets[-1])

def get_candlestick_chart_figure(stock_id):
    df = pd.read_csv(f"{stock_id}.TW.csv").drop(columns = ["Adj Close"])
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
    df.set_index("Date", inplace=True)
    df["5MA"] = df["Close"].rolling(5).mean()
    df["10MA"] = df["Close"].rolling(10).mean()
    df["20MA"] = df["Close"].rolling(20).mean()
    df["BBmax"] = df["Close"].rolling(20).mean() + df["Close"].rolling(20).std() * 2
    df["BBmin"] = df["Close"].rolling(20).mean() - df["Close"].rolling(20).std() * 2
    df = df[len(df.index)-30:len(df.index)]
    df_candle = df[["Open", "High", "Low", "Close", "Volume"]]

    df_MA = df[["5MA", "10MA", "20MA"]]
    df_BB = df[["BBmax", "BBmin"]]
    colors = {
        "red": df_candle[df_candle["Open"] < df_candle["Close"]],
        "green": df_candle[df_candle["Open"] > df_candle["Close"]],
        "yellow": df_candle[df_candle["Open"] == df_candle["Close"]]
    }
    fig = plt.figure(figsize=[4.8, 3.6])
    for color in colors.keys():
        plt.bar(colors[color].index, 
                colors[color]["High"]-colors[color]["Low"], 
                width=0.1, 
                bottom=colors[color]["Low"], 
                color=f"{color}")
        unchanged = 0
        if color == "yellow":
            unchanged = 0.1
        plt.bar(colors[color].index, 
                colors[color]["Close"]-colors[color]["Open"] + unchanged, 
                width=0.5, 
                bottom=colors[color]["Open"], 
                color=f"{color}")
        plt.bar(colors[color].index, 
            colors[color]["Volume"] / colors[color]["Volume"].mean(),
            width=0.5,
            bottom=df_BB["BBmin"].min() * 0.95,
            color=f"{color}")
    plt.plot(df_MA, label=df_MA.columns, lw=0.5)
    plt.plot(df_BB, label=df_BB.columns, lw=0.5)
    plt.xticks(rotation="vertical")
    plt.legend()
    for picture in wb.sheets[stock].pictures:
        picture.delete()
    wb.sheets[stock].pictures.add(fig,
                                  left=wb.sheets[stock].range("F1").left,
                                  top=wb.sheets[stock].range("F1").top)

def reset_realtime_trend_data(stock_id):
    for chart in wb.sheets[stock_id].charts:
        chart.delete()
    wb.sheets[stock_id].charts.add(left=wb.sheets[stock_id].range("N1").left, top=wb.sheets[stock_id].range("N1").top)
    wb.sheets[stock_id].charts[0].chart_type = "line"
    last_row = wb.sheets[stock_id].range("Z1").end("down").row
    wb.sheets[stock_id].range(f"AA2:AA{last_row}").value = ""

def get_realtime_data(stock, fugle_token):
    payload = {
            "symbolId": stock_id,
            "apiToken": fugle_token
        }
    res_meta = requests.get("https://api.fugle.tw/realtime/v0.3/intraday/meta", params=payload)
    res_quote = requests.get("https://api.fugle.tw/realtime/v0.3/intraday/quote", params=payload)
    json_meta = res_meta.json()
    json_quote = res_quote.json()
    stock_name = json_meta["data"]["meta"]["nameZhTw"]
    last_close = json_meta["data"]["meta"]["priceReference"]
    current_price = json_quote["data"]["quote"]["trade"]["price"]
    bids = json_quote["data"]["quote"]["order"]["bids"]
    bid_prices =  np.array([bid["price"] for bid in bids]).reshape(5, 1)
    bid_volumes = np.array([bid["volume"] for bid in bids]).reshape(5, 1)
    asks = json_quote["data"]["quote"]["order"]["asks"]
    ask_prices =  np.array([ask["price"] for ask in asks]).reshape(5, 1)
    ask_volumes = np.array([ask["volume"] for ask in asks]).reshape(5, 1)
    last_update = json_quote["data"]["quote"]["order"]["at"]
    return {
        "個股名稱": stock_name,
        "昨日收盤價": last_close,
        "目前成交價": current_price,
        "五檔買價": bid_prices,
        "五檔買量": bid_volumes,
        "五檔賣價": ask_prices,
        "五檔賣量": ask_volumes,
        "上次更新時間": last_update
    }

def line_me(content, line_token):
    requests.post("https://notify-api.line.me/api/notify",
                  headers = {"Authorization": f"Bearer {line_token}"},
                  params = {"message": content})

def write_to_excel(sheet, datas):
    sheet.range("A2").value = datas["個股名稱"]
    sheet.range("B2").value = datas["昨日收盤價"]
    sheet.range("C2").value = datas["目前成交價"]
    sheet.range("D2").formula = "=(C2-B2)/B2"
    if sheet.range("D2").value < 0:
        sheet.range("D2").color = 0, 255, 0
    elif sheet.range("D2").value > 0:
        sheet.range("D2").color = 255, 0, 0
    else:
        sheet.range("D2").color = 255, 255, 0
        
    sheet.range("A6:A10").value = datas["五檔買量"]
    sheet.range("B6:B10").value = datas["五檔買價"]
    sheet.range("C6:C10").value = datas["五檔賣價"]
    sheet.range("D6:D10").value = datas["五檔賣量"]
    sheet.range("B12").value = datas["上次更新時間"]
    
def draw_realtime_trend(sheet, datas):
    last_row = sheet.range("Z1").end("down").row
    for i in range(2, last_row+1):
        if sheet.range(f"Z{i}").value == time.strftime("%H:%M"):
            sheet.range(f"AA{i}").value = datas["目前成交價"]
            break
    sheet.charts[0].set_source_data(sheet.range(f"Z2:AA{last_row}"))

def update_today_data(stock_id, fugle_token):
    csv = xw.Book(f"{stock_id}.TW.csv")
    csv_sheet = csv.sheets[0]
    payload = {
            "symbolId": stock_id,
            "apiToken": fugle_token
        }
    res_quote = requests.get("https://api.fugle.tw/realtime/v0.3/intraday/quote", params=payload)
    json_quote = res_quote.json()
    last_row = csv_sheet.range("A1").end("down").row
    csv_sheet.range(f"A{last_row+1}").value = time.strftime("%Y/%m/%d")
    csv_sheet.range(f"B{last_row+1}").value = json_quote["data"]["quote"]["priceOpen"]["price"]
    csv_sheet.range(f"C{last_row+1}").value = json_quote["data"]["quote"]["priceHigh"]["price"]
    csv_sheet.range(f"D{last_row+1}").value = json_quote["data"]["quote"]["priceLow"]["price"]
    csv_sheet.range(f"E{last_row+1}").value = json_quote["data"]["quote"]["trade"]["price"]
    csv_sheet.range(f"F{last_row+1}").value = json_quote["data"]["quote"]["trade"]["price"]
    csv_sheet.range(f"G{last_row+1}").value = json_quote["data"]["quote"]["total"]["tradeVolume"] * 1000
    csv.save()
    csv.app.quit()
    
fugle_token = wb.sheets["股票代號清單"].range("fugle_token").value
line_token = wb.sheets["股票代號清單"].range("line_token").value
for stock_id in stock_ids:
    get_candlestick_chart_figure(stock_id)
    reset_realtime_trend_data(stock_id)
count_minute = 0
while True:
    if time.strftime("%H:%M") == "09:00":
        break
while time.strftime("%H:%M") != "13:31":
    start = time.time()
    for stock_id in stock_ids:
        wb.sheets[stock_id].activate()
        datas = get_realtime_data(stock_id, fugle_token)
        
        change_rate = (datas["目前成交價"]-datas["昨日收盤價"]) / datas["昨日收盤價"]
        if change_rate > 0.02:
            line_me(f"{stock_id}漲幅超過2%", line_token)
        elif change_rate < -0.02:
            line_me(f"{stock_id}跌幅超過2%", line_token)
            
        write_to_excel(wb.sheets[stock_id], datas)
        
        if count_minute == 4:
            draw_realtime_trend(wb.sheets[stock_id], datas)
    if count_minute == 4:
        count_minute = 0
    count_minute += 1
    end = time.time()
    time.sleep(15-(end-start))
wb.save()
for stock_id in stock_ids:
    update_today_data(stock_id, fugle_token)
line_me("今日台股收盤資料已更新", line_token)

