#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ei code ta jyputer notebook e real answer dei na ...eta IDLE te kora lage but amr pc te IDLE te korle vul dekai
# tai ans paibar jnoo kono rokom Jupyter notebook e korci

import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt


plt.style.use('fivethirtyeight')

fig1 = plt.figure()

ax1 = fig1.add_subplot(1,1,1)

def animate(p):
    plot_data = open('text.txt','r').read()

    line_data = plot_data.split('\n')
    x1=[]
    y1=[]

    for line in line_data:
        if len(line)>1:
            x,y = line.split(',')
            x1.append(x)
            y1.append(y)


        ax1.clear()
        ax1.plot(x1,y1)

anime_data = animation.FuncAnimation(fig1, animate, interval = 500)


plt.tight_layout()
plt.show()

