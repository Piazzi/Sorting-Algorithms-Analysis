import matplotlib.pyplot as plt
import numpy as np

#Considere conjuntos de dados com quantidades de elementos variando de 10, 100, 1000, 10.000
#e 100.000. No sentido de identificar diferenças de comportamento dos algoritmos conforme a entrada,
#a análise a ser apresentada deve considerar diferentes características dos dados, como casos com e
#sem repetição de elementos, casos em que todos os elementos são inteiros, em quem todos os
#elementos são reais não necessariamente inteiros e os casos em que os dados estão ordenadas,
#inversamente, ordenadas, bem como quando são dispostos de forma aleatória.

def generateEntries(n, unique, type):
    entries = []
    i = 0
    while i < n:
        entries.append(np.random.randint(-10000, 10000))
        i = i + 1
    print(entries)
    return entries
    
generateEntries(100, 0, 'integer')
    
# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()