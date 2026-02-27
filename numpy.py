import numpy as np

a = np.array([1,2,3,4,5])
b=np.arange(10)
c = np.linspace(0,10,5)

d=np.zeros((3,3))
e = np.ones((2,4))
f=np.eye(4)

g = np.random.randint(1,100,(4,4))

h = a*2
i=b+5

j = g.reshape(2,8)
k=g.flatten()
l = g.T

m=np.sum(g)
n = np.mean(g)
o=np.min(g)
p = np.max(g)
q=np.std(g)

r = np.sort(g,axis=1)
s=np.unique([1,2,3,4,2,3,5,6,1,7])

t = g[g>50]
u=g[(g>20)&(g<70)]

v = np.dot(np.array([[1,2],[3,4]]),
           np.array([[5,6],[7,8]]))

w=np.vstack((a,a))
x = np.hstack((a,a))

y=np.argmax(g)
z = np.argmin(g)

print("a:",a)
print("g:\n",g)
print("reshape:\n",j)
print("T:\n",l)
print("stats:",m,n,o,p,q)
print(">50:",t)
print("dot:\n",v)
print("idx:",y,z)
