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

#This is the main ADT (Abstract Data Type) of the project, it creates the entries and runs each algorithm based
# on the parameters receveid.
class Test(object):
    
    """Constructor"""
    def __init__(self, n, unique, type, order, algorithm):
        self.n = n
        self.unique = unique
        self.type = type
        self.order = order
        self.algorithm = algorithm
    
    # each test runned stores it's information in the following variables
    executionTimes = []
    sizes = []
    comparisons = []
    
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
        executionTime = endTime - startTime
        
        # saves the data generated from the execution in the class variables
        self.executionTimes.append(executionTime)
        self.sizes.append(self.n)
        self.comparisons.append(count)
        
        print("Numbers to orderes: ", entries, 'Execution Time: ', executionTime, "s", "Number of Comparisons: ", count)
        
    # draw a graph based on the tests runned
    def drawGraph(self):
        print('Graph Generated')
        names = list(self.comparisons)
        values = list(self.sizes)

        fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
        axs[0].bar(names, values)
        axs[1].scatter(names, values)
        axs[2].plot(names, values)
        fig.suptitle('Categorical Plotting')
        plt.show()
     
    # sets a new test based on the parameters 
    def setTest(self, n, unique, type, order, algorithm):
        self.n = n
        self.unique = unique
        self.type = type
        self.order = order
        self.algorithm = algorithm




# Data for plotting
#A ideia é que cada ponto da curva seja fotmado por um valor de n (tamanho do vetor)
# e o respectivo tempo de processamento (ou numero de comparações).

#Como vocês precisarão analisar diferentes eixos, para cada eixo, vocês devem ter diferentes conjuntos de entrada, 
# seja pelo tamanho, tipo ou configuração (ordenado, não ordenado ou quase ordenado), 
# sendo que precisarão de datasets com tamanhos diferentes dentro de cada eixo.

# ------------------------------ BUBBLE SORT ------------------------------ 

test = Test(10, False, 'integer', 'random', bubbleSort)
test.runTest()
test(100, False, 'integer', 'random', bubbleSort)
test.runTest()
test.drawGraph()

