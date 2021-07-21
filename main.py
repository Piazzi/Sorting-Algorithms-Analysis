import matplotlib.pyplot as plt
import numpy as np
import time  
import random
from algorithms.bubbleSort import bubbleSort
from algorithms.insertionSort import insertionSort
from algorithms.selectionSort import selectionSort
from algorithms.bogoSort import bogoSort
from algorithms.quickSort import quickSort
from algorithms.mergeSort import mergeSort
from algorithms.heapSort import heapSort

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

#Análise dos algoritmos:
#A análise deve ser feita sobre o número de comparações entre elementos do conjunto.
#Lembrem-se que os dados coletados devem ser organizados na forma de tabelas e a visualização
#destes dados na forma de gráficos facilita a análise e a leitura do texto final. A partir das tabelas e
#gráficos, desenvolva o texto sobre a análise dos algoritmos, um importante elemento do trabalho. Para
#comparação, relacione somente os algoritmos não eficientes e eficientes entre si. Por exemplo, não
#relacione, analise ou compare, o algoritmo BubbleSort com o QuickSort.

# Função que retorna um vetor de entradas de tamanho n, podendo ter números unicos ou não,
# de acordo com  o que for indicado na variável unique. Sendo inteiro ou float,indicado pela 
# variável type. E sendo um vetor ordenado, ordenado inversamente ou aleatório de acordo
# com o que for indicado pela variável order.

# Generates a random n size vector.
# unique = indicates if the numbers in the array should be unique or not
# type = indicates whether numbers should be float or integer
# order = indicates whether the returned array should be ordered, inverse ordered or random.
def generateEntries(n, unique, type, order):
    entries = []
    if unique == True:
        entries = random.sample(range(-10000, 10000), n)
    else:
        i = 0
        while i < n:
            entries.append(np.random.randint(-10000, 10000))
            i = i + 1
            
    if type == 'float':
        entries = [x/10 for x in entries]
        
    if order == 'ascending':
        entries.sort()
    elif order == 'descending':
        entries.sort(reverse=True)
        
    print(entries)
    print('\n')
    return entries
    

#PRINT
#alist = generateEntries(100, 'false', 'integer', 'random')
#startTimeBubbleSort = time.time()
#bubbleSort(alist)
#endTimeBubbleSort = time.time()
#print("BUBBLESORT",alist, "bubblesort time: ",endTimeBubbleSort-startTimeBubbleSort , " s" )

#alist = generateEntries(100, 'false', 'integer', 'random')
#startTimeInsertionSort = time.time()
#insertionSort(alist)
#endTimeInsertionSort = time.time()
#print("INSERTION SORT",alist, "insertion sort time: ",endTimeInsertionSort-startTimeInsertionSort , " s" )

#alist = generateEntries(100, 'false', 'integer', 'random')
#startTimeSelectionSort = time.time()
#selectionSort(alist)
#endTimeSelectionSort = time.time()
#print("SELECTION SORT",alist, "selection sort time: ",endTimeSelectionSort - startTimeSelectionSort, " s" )

alist = generateEntries(10, False, 'integer', 'random')
startTimeBogoSort = time.time()
bogoSort(alist)
endTimeBogoSort = time.time()
print("BOGO SORT",alist, "bogo sort time: ",endTimeBogoSort - startTimeBogoSort, " s" )

#alist = generateEntries(100, 'false', 'integer', 'random')
#startTimeQuickSort = time.time()
#quickSort(alist)
#endTimeQuickSort = time.time()
#qsTime= endTimeQuickSort-startTimeQuickSort
#print("QUICK SORT",alist, "quicksort time: ",qsTime , " s" )


#alist = generateEntries(100, 0, 'integer')
#startTimeMergeSort = time.time()
#mergeSort(alist)
#endTimeMergeSort = time.time()
#msTime = endTimeMergeSort - startTimeMergeSort
#print("MERGESORT",alist , "mergesort time: ", msTime, " s" )


#alist = generateEntries(100, 0, 'integer')
#startTimeHeapSort = time.time()
#heapSort(alist)
#endTimeHeapSort = time.time()
#hsTime = endTimeHeapSort - startTimeHeapSort
#print("HEAPSORT",alist , "heapsort time: ", hsTime, " s" )
#PRINT 


# Data for plotting
#t = np.arange(0.0, 2.0, 0.01)
#s = 1 + np.sin(2 * np.pi * t)

#fig, ax = plt.subplots()
#ax.plot(t, s)

#ax.set(xlabel='time (s)', ylabel='Iteration',
#       title='Time x Entries graph')
#ax.grid()

#fig.savefig("test.png")
#plt.show()