import matplotlib.pyplot as plt
import numpy as np
import time  
from quickSort import quickSort
from mergeSort import mergeSort
from heapSort import heapSort

#Trabalho de Análise e Projeto de Algoritmos - DCC001
#Professor: Stênio Sã Rosário Furtado Soares
#Turma A 2021.1 - Ensino Remoto Emergencial
#Grupo: Camila Vieira e Lucas Piazzi

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
    return entries
    

#PRINT
alist = generateEntries(100, 0, 'integer')
startTimeQuickSort = time.time()
quickSort(alist)
endTimeQuickSort = time.time()
qsTime= endTimeQuickSort-startTimeQuickSort
print("QUICKSORT",alist, "quicksort time: ",qsTime , " s" )


alist = generateEntries(100, 0, 'integer')
startTimeMergeSort = time.time()
mergeSort(alist)
endTimeMergeSort = time.time()
msTime = endTimeMergeSort - startTimeMergeSort
print("MERGESORT",alist , "mergesort time: ", msTime, " s" )


alist = generateEntries(100, 0, 'integer')
startTimeHeapSort = time.time()
heapSort(alist)
endTimeHeapSort = time.time()
hsTime = endTimeHeapSort - startTimeHeapSort
print("HEAPSORT",alist , "heapsort time: ", hsTime, " s" )
#PRINT 


# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='Iteration',
       title='Time x Entries graph')
ax.grid()

fig.savefig("test.png")
plt.show()