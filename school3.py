import request, time
from datetime import datetime

while True:
    start = datetime.now()
    url = "http://opendata.epa.gov.tw/ws/Data/ATM00625/?$format-json"
    res = request.get(url)

    date = res.json()
    creationDate = datetime.strptime(datas[0]['DataCreationDate'],
    ftime = creationDate.strftime("%Y%m%d%H%M%S")
    with open ("D:\\pm2.5_"+ftime+".json", 'wb') as f:
        #f.write(res.content)
        f.write(res.content)
    td = datetime.now() - start
    print("花費", td.second, "秒")
    time.sleep(60*30-td.seconds)
