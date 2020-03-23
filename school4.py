import requests, time, json, sys
from datetime import datetime, timedelta

start = datetime(2020, 3, 18, 0, 0)

print('時\tpm2.5')
for i in range(24):
    ftime = start.strftime('%Y%m%d%H%M')
    filename = 'D:\\pm25_'+ftime+'.json'
    try:
        with open(filename, 'r', encoding='UTF-8') as f:
            datas = json.loads(f.read())
            print(start.strftime('%H')+'\t'+datas[7]['PM25'])
    except:
        print(filename, sys.exc_info()[0],'not found!!')

    start = start + timedelta(hours=1)
