import requests, time
from datetime import datetime

while True:
    start = datetime.now()
    uil = 'https://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=json'
    res = requests.get(uil)
    print(res.text)
    datas = res.json()
    creationData = datetime.strptime(datas[0]['DataCreationDate'], '%Y-%m-%d %H:%M')
    ftime = creationData.strftime('%Y%m%d%H%M')
    with open('D:\\pm25_'+ftime+'.json', 'wb') as f:
        #f.write(res.content)
        f.write(res.content)
    td = datetime.now() - start
    print('花費', td.seconds, '秒')
    time.sleep(60*30-td.seconds)
