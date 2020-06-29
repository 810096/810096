import matplotlib.pyplot as plt
import numpy as np
import xlrd
data = xlrd.open_workbook(r'D:\新北勞動參與率vs失業率.xlsx')
table = data.sheets()[0]
new_ticks = np.linspace(2007, 2018, 12)
plt.rcParams['font.family'] = 'DFKai-SB'
plt.figure(dpi=120,linewidth = 2)
plt.xticks(new_ticks)
plt.xlabel('國小')
plt.ylabel('%')
axis_x = []
Y1=[]
Y2=[]
x=table.col_values(0)[1:13]
y1=table.col_values(2)[1:13]
y2=table.col_values(1)[15:27]
n=12
axis_x =x
Y1=y1
Y2=y2
plt.plot(axis_x, Y1, '*--', label='G1') 
plt.plot(axis_x, Y2, 'rd--', label='G2') 
for x, y1 in zip(axis_x, Y1):
    plt.text(x, y1, '%.2f' % y1 ,ha='center', va='bottom')
for x, y2 in zip(axis_x, Y2):
    plt.text(x, y2, '%.2f' % y2 ,ha='center', va='bottom')
plt.show()
