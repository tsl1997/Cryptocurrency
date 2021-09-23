from openpyxl import Workbook
import requests,datetime
url = 'https://www.binancezh.top/bapi/composite/v1/public/marketing/symbol/list'
header1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
resp = requests.get(url, headers = header1)
resps = resp.json().get('data')

wb = Workbook()
sh = wb.active
sh.append(['名称', '价格', '交易对', '市值','最大供应','初始价格','首日收盘价','首日高点','上架时间'])

for i in resps:
        symbol =i.get('symbol')
        print(symbol)
        url = 'https://api.yshyqxx.com/api/v3/klines?symbol=' + symbol + '&interval=1d'
        #获取代币的具体信息链接，1d是一天，可以更换为其他的参数。
        header1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
        resp = requests.get(url, headers = header1).json()
        #print('测试:',resp[0])
        sj = resp[0][0]
        time_stamp = int(sj)/1000
        #print(time_stamp)#测试是否可以输出数值
        datetime_array = datetime.datetime.utcfromtimestamp(time_stamp)
        other_way_time = datetime_array.strftime("%Y-%m-%d")
        #print('初始价格:',resp[0][1])
        #print('高点价格:',resp[0][2])
        #print('收盘价格:',resp[0][4])
        #print('时间:',other_way_time)
        d = i.get('name'),i.get('price'),i.get('symbol'),i.get('marketCap'),i.get('maxSupply'),resp[0][1],resp[0][4],resp[0][2],other_way_time
        sh.append(d)  # 每次写入一行
wb.save('币安.xlsx')