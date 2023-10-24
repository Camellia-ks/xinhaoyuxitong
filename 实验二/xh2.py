# -*- coding: UTF-8 -*-
#coding=utf-8

import numpy as np # 科学计算
import matplotlib.pyplot as plt # 画图
import scipy.signal as sg # 导入 scipy 的 signal 库 命名为 sg

'''
n = np.linspace(-10, 11, 21, endpoint=False) # 定义离散时间序列
rad = np.pi / 4 # 基波周期 N=8
plt.stem(n, sg.square(rad * n, 0.5)) # 绘制离散周期方波图像
plt.xticks(np.arange(-10, 10, step=5.0)) # 横坐标间隔
plt.text(0, 1, r'$f(t) = \mathrm{sg.square}(\frac{\pi}{4} \cdot t, 0.5)$', fontsize=12, ha='center')
plt.xlabel('Time')
plt.ylabel('Amplitude')
#plt.text(0, 1, 'name', fontsize=12, ha='center')
#plt.text(0, 1, 'This is a square wave', fontsize=12, ha='center')
plt.grid() # 显示网格
plt.show() # 显示图像
'''
'''
# 连续指数信号 
# 产生随时间衰减的指数信号	
t = np.linspace(0, 5, 5000, endpoint=False)# 定义时间序列
plt.plot(t, 2*np.exp(-1*t))# 绘制随时间衰减的指数信号图
plt.text(2, 1.5, r'$f(t) = 2e^{-t}$', fontsize=12, ha='center')
plt.grid()
plt.show()
'''


# 阶跃信号
t = np.linspace(-1, 1, 500, endpoint=False) # 产生-1～1的500个点
plt.plot(t, np.array(t>0, dtype=int))  # 取t为x轴的分布， t当中大于0的部分为y轴的分布 （即当x<0时y=0，当y>0时y=1）
plt.text(0,1,r'$f(t) = u(t)$',fontsize = 12,ha='center')
plt.grid()
_ = plt.ylim(-0.5, 1.5)
plt.show()


'''
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100)
y = np.sin(x)

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)
plt.title(r'$f(x)=sin(x)$') 
plt.plot(x, y)
#plt.show()

x1 = [t*0.375*np.pi for t in x]
y1 = np.sin(x1)
plt.subplot(1,2,2)
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') 
plt.plot(x1, y1)
plt.show()'''