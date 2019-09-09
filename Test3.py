from matplotlib import pyplot as plt
import numpy as np

a = np.floor(10*np.random.random(10000))

num0 = np.count_nonzero(a==0)
num1 = np.count_nonzero(a==1)
num2 = np.count_nonzero(a==2)
num3 = np.count_nonzero(a==3)
num4 = np.count_nonzero(a==4)
num5 = np.count_nonzero(a==5)
num6 = np.count_nonzero(a==6)
num7 = np.count_nonzero(a==7)
num8 = np.count_nonzero(a==8)
num9 = np.count_nonzero(a==9)

print("0 : ",num0)
print("1 : ",num1)
print("2 : ",num2)
print("3 : ",num3)
print("4 : ",num4)
print("5 : ",num5)
print("6 : ",num6)
print("7 : ",num7)
print("8 : ",num8)
print("9 : ",num9)

counts = [num0,num1,num2,num3,num4,num5,num6,num7,num8,num9]
name = ['0','1','2','3','4','5','6','7','8','9']

plt.pie(counts, labels = name, autopct='%1.2f%%')
plt.show()