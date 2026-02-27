import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=np.arange(1,11)
y = np.random.randint(10,100,10)

plt.plot(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Line Plot")
plt.show()

plt.bar(x,y)
plt.show()

plt.scatter(x,y)
plt.show()

data={
    "Day":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
    "Sales":[120,150,180,170,200,220,210]
}

df=pd.DataFrame(data)

plt.plot(df["Day"],df["Sales"])
plt.show()

plt.bar(df["Day"],df["Sales"])
plt.show()

plt.pie(df["Sales"],
        labels=df["Day"],
        autopct="%1.1f%%")
plt.show()

arr=np.random.randn(1000)

plt.hist(arr,bins=30)
plt.show()
