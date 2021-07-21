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

#This is the main ADT of the project, it creates the entries and runs each algorithm based
# on the parameters receveid.
class Test(object):
    """Constructor"""
    def __init__(self, n, unique, type, order, algorithm):
        self.n = n
        self.unique = unique
        self.type = type
        self.order = order
        self.algorithm = algorithm
        
        
    # Generates a random n size vector. The numbers in the vector will be in range between -10000 and 10000.
    # unique = indicates if the numbers in the array should be unique or not
    # type = indicates whether numbers should be float or integer
    # order = indicates whether the returned array should be ordered, inverse ordered or random.
    def generateEntries(self):
        entries = []
        if self.unique == True:
            entries = random.sample(range(-10000, 10000), self.n)
        else:
            i = 0
            while i < self.n:
                entries.append(np.random.randint(-10000, 10000))
                i = i + 1
                
        if type == 'float':
            entries = [x/10 for x in entries]
            
        if self.order == 'ascending':
            entries.sort()
        elif self.order == 'descending':
            entries.sort(reverse=True)
            
        print(entries)
        print('\n')
        return entries
    
    # Run the algorithm for the given parameters
    def runTest(self):
        entries = self.generateEntries()
        startTime = time.time()
        #each algorithm returns the numbers of comparisons made
        count = self.algorithm(entries)
        endTime = time.time()
        print("Numbers to orderes: ", entries, 'Execution Time: ', endTime - startTime, "s", "Number of Comparisons: ", count)
        
        




# Data for plotting
#A ideia é que cada ponto da curva seja fotmado por um valor de n (tamanho do vetor)
# e o respectivo tempo de processamento (ou numero de comparações).

#Como vocês precisarão analisar diferentes eixos, para cada eixo, vocês devem ter diferentes conjuntos de entrada, 
# seja pelo tamanho, tipo ou configuração (ordenado, não ordenado ou quase ordenado), 
# sendo que precisarão de datasets com tamanhos diferentes dentro de cada eixo.

# ------------------------------ BUBBLE SORT ------------------------------ 

test = Test(10, False, 'integer', 'random', bubbleSort)
test.runTest()

#t = np.arange(endTimeBubbleSort-startTimeBubbleSort, 2000.0, 300000.0)
#s = np.arange(count, 20000,123123 )

#fig, ax = plt.subplots()
#ax.plot(t, s)

#ax.set(xlabel='Tempo (s)', ylabel='N° Comparações',
#       title='Bubble Sort')
#ax.grid()

#fig.savefig("graphs/bubblesort/test.png")
#plt.show()

#https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html#sphx-glr-gallery-lines-bars-and-markers-categorical-variables-py


# data from United Nations World Population Prospects (Revision 2019)
# https://population.un.org/wpp/, license: CC BY 3.0 IGO
# year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2018]
# population_by_continent = {
#     'africa': [228, 284, 365, 477, 631, 814, 1044, 1275],
#     'americas': [340, 425, 519, 619, 727, 840, 943, 1006],
#     'asia': [1394, 1686, 2120, 2625, 3202, 3714, 4169, 4560],
#     'europe': [220, 253, 276, 295, 310, 303, 294, 293],
#     'oceania': [12, 15, 19, 22, 26, 31, 36, 39],
# }

# fig, ax = plt.subplots()
# ax.stackplot(year, population_by_continent.values(),
#              labels=population_by_continent.keys())
# ax.legend(loc='upper left')
# ax.set_title('World population')
# ax.set_xlabel('Year')
# ax.set_ylabel('Number of people (millions)')

# plt.show()