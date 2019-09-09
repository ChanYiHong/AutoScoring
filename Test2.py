import numpy as np
import matplotlib.pyplot as plt
m_height = np.array([167,170,163,160,178,177,175,171,163,169,165,181,175,170,181,177,172,168,160,175,173,158,158,158,175,160])
w_height = np.array([163,177,179,168,174,176,162,172,155,157,179,155,178,165,179,163,168,170,161,167,165,183,172,175,160,189])

print("Monday group height : " )
print(m_height)

print("Monday group mean : ")
print(np.mean(m_height))  #mean
print("Monday group variance : ")
print(np.var(m_height))  #variance   
print("Monday group standard deviation : ")
print(np.std(m_height))  #standard deviation

print("Wednesday group height : " )
print(w_height)

print("Wednesday group mean : ")
print(np.mean(w_height))
print("Wednesday group variance : ")
print(np.var(w_height))
print("Wednesday group standard deviation : ")
print(np.std(w_height))

plotData = [m_height, w_height]
plt.boxplot(plotData)
plt.show()
