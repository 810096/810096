import request, time
from datetime import datetime

現在 = datetime.now()
print(現在)
ftime = 現在.strftime("%Y%m%d_%H%M%S)
print("時間格式化", ftime)

with open ("D:\\pm2.5_"+ftime+".json", 'wb') as f:
    #f.write(res.content)
    f.write(b"xxxxxx")
    print("寫入完成", 現在)