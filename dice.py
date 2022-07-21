import numpy as np 
import matplotlib.pyplot as plt


trials = np.arange(1,101)
dice1=np.random.randint(1,7,100)
dice2=np.random.randint(1,7,100)
dice_sum=dice1+dice2
print(dice_sum)

fig = plt.figure(tight_layout = True)

ax = fig.add_subplot(2,2,1)
ax.scatter(trials,dice_sum,s=2,color='green')
ax.set_title('Scatter')
ax.set_xlabel('trials')
ax.set_ylabel('Sum')

ax = fig.add_subplot(2,2,2)
ax.plot(trials,dice_sum,color='red')
ax.set_title('Line')
ax.set_xlabel('trials')
ax.set_ylabel('Sum')

ax = fig.add_subplot(2,2,3)
ax.hist(dice_sum,bins=10,edgecolor='black')
ax.set_title('Histogram')

ax = fig.add_subplot(2,2,4)
ax.pie(dice_sum)
ax.set_title('Yummy Pie')

plt.show()