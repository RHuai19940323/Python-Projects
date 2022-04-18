#!/usr/bin/env python
# coding: utf-8

# # 回測流程
# 
# ### 1. 到yahoo finance蒐集資料
# ### 2. 設計回測表格
#     日期, 收盤價, 購買成本(收盤價 x (1+手續費率)), 投入資金, 買進股數(零股計算), 累積股數, 累積資產淨值
# ### 3. 設計投資策略
#     月中定期定額10000
# ### 4. 執行回測
# ### 5. 顯示結果(表格&圖表)

# In[9]:


import pandas as pd
import xlwings as xw
import time
import glob
history_data = glob.glob("history_data/*.csv")
ETFs = ["0050", "0056", "006208"]
ETFs_Adj_Close = {}

for i in range(0, len(history_data)):
    ETFs_Adj_Close[ETFs[i]] = pd.DataFrame(pd.read_csv(history_data[i], index_col = "Date")["Adj Close"])

for ETF in ETFs:
    ETFs_Adj_Close[ETF]["Adj Close"] = round(ETFs_Adj_Close[ETF]["Adj Close"], 2)
    ETFs_Adj_Close[ETF]["Buy-in Cost"] = round(ETFs_Adj_Close[ETF] * 1.002425, 2)
wb = xw.Book("Backtesting(0050,0056,006208).xlsx")
#[wb.sheets.add(ETFs[i], after=wb.sheets[-1].name) for i in range(0, len(ETFs))]
#del wb.sheets[0]
ETF_sheets = wb.sheets
def basicData(sheet):
    sheet.range("A1").value = ETFs_Adj_Close[sheet.name]
    headers = [
        "日期", 
        "收盤價", 
        "購買成本\n(收盤價 x (1+手續費率+交易稅))", 
        "投入資金", 
        "買進股數(零股)", 
        "資產成本",
        "剩餘資金",
        "股票現值",
        "持股獲利",
        "資產淨值"
    ]
    sheet.range("A1").value = headers
def middle_of_the_month(sheet, i):
    for j in range(15, 19):
        if ETFs_Adj_Close[sheet.name].index[i-2][-2:] == str(j):
            return True
def check_buy_once(sheet, i):
    for j in range(1, 5):
        if sheet.range(f"D{i-j}").value != 0:
            return False;
    return True
        
def investing_data(sheet):
    last_row = sheet.range("A1").end("down").row
    for i in range(2, last_row+1):
        if (middle_of_the_month(sheet, i)) and (check_buy_once(sheet, i)):
            sheet.range(f"D{i}").value = 10000
            sheet.range(f"E{i}").value = 10000 // sheet.range(f"C{i}").value
        else:
            sheet.range(f"D{i}").value = 0
            sheet.range(f"E{i}").value = 0
        
        sheet.range(f"F{i}").formula = f"=C{i}*E{i}"
        sheet.range(f"G{i}").formula = f"=D{i}-F{i}"
        sheet.range(f"H{i}").formula = f"=B{last_row}*E{i}"
        sheet.range(f"I{i}").formula = f"=H{i}-F{i}"
        sheet.range(f"J{i}").formula = f"=G{i}+H{i}"
for sheet in ETF_sheets:
    sheet.activate()
    basicData(sheet)
    investing_data(sheet)
    time.sleep(2)
wb.save()
df_backtesting = {}
backtesting_result = {}

for ETF in ETFs:
    df_backtesting[ETF] = pd.read_excel("Backtesting(0050,0056,006208).xlsx", sheet_name = ETF)
    backtesting_result[ETF] = {}
    backtesting_result[ETF]["總投入資金"] = sum(df_backtesting[ETF]["投入資金"])
    backtesting_result[ETF]["總持有股數"] = sum(df_backtesting[ETF]["買進股數(零股)"])
    backtesting_result[ETF]["總資產"] = sum(df_backtesting[ETF]["資產淨值"])
    backtesting_result[ETF]["總獲利"] = sum(df_backtesting[ETF]["持股獲利"])
    backtesting_result[ETF]["投資報酬率"] = str(round(backtesting_result[ETF]["總獲利"] * 100 / backtesting_result[ETF]["總投入資金"], 3)) + "%"
pd.DataFrame(backtesting_result)   

