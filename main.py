#Created by: Camila Vieira e Lucas Piazzi

import matplotlib.pyplot as plt
import numpy as np
import time  
import random
import copy
from algorithms.bubbleSort import bubbleSort
from algorithms.insertionSort import insertionSort
from algorithms.selectionSort import selectionSort
from algorithms.bogoSort import bogoSort
from algorithms.quickSort import quickSort
from algorithms.mergeSort import mergeSort
from algorithms.heapSort import heapSort

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
        # create the entries once
        self.entries = {
            10: self.generateEntries(10), 
            100: self.generateEntries(100), 
            1000: self.generateEntries(1000), 
            10000: self.generateEntries(10000),
            100000: self.generateEntries(100000)
        }
    
    # each test runned stores it's information in the following variables
    executionTimes = []
    comparisons = []
    sizes = []
    algorithms = []
    
    # Generates a random n size vector. The numbers in the vector will be in range between -10000 and 10000.
    # unique = indicates if the numbers in the array should be unique or not
    # type = indicates whether numbers should be float or integer
    # order = indicates whether the returned array should be ordered, inverse ordered or random.
    def generateEntries(self, n):
        entries = []
        if self.unique == True:
            entries = random.sample(range(-10000, 10000), self.n)
        else:
            i = 0
            while i < n:
                entries.append(np.random.randint(-10000, 10000))
                i = i + 1
                
        if type == 'float':
            entries = [x/10 for x in entries]
            
        if self.order == 'ascending':
            entries.sort()
        elif self.order == 'descending':
            entries.sort(reverse=True)
        return entries
    
    # Run the algorithm for the given parameters
    def runTest(self):
        # check if the entry already exists in the dictionary, if not, creates
        # a new n size entry and stores in the dictionary
        if self.n in self.entries :
            entry = copy.deepcopy(self.entries[self.n])
        else:
            entry = self.generateEntries(self.n)
            self.entries[self.n] = entry
            
        startTime = time.time()
        #each algorithm returns the numbers of comparisons made
        count = self.algorithm(entry)
        endTime = time.time()
        executionTime = endTime - startTime
        # saves the data generated from the execution in the class variables
        self.executionTimes.append(executionTime)
        self.comparisons.append(count)
        self.sizes.append(self.n)
        self.algorithms.append(self.algorithm.__name__)
        
        print(self.algorithm.__name__, " --> Numbers to order: ", self.n, 'Execution Time: ', executionTime, "s", "Number of Comparisons: ", count)
        
    # draw a graph based on the tests runned
    def drawGraph(self):
        print('Graph Generated')
        # x axis
        x = list(self.comparisons)
        # y axis
        y = list(self.executionTimes)
        
        i = 0
        while i < len(self.algorithms):
            plt.plot(np.linspace(0,x[i], 100), np.linspace(0, y[i], 100), label=self.algorithms[i] + ' (N = ' +  str(self.sizes[i]) + ')')
            i = i + 1
        
        plt.xlabel('N° Comparações')
        plt.ylabel('Tempo de execução (s)')
        plt.title("")
        plt.legend()
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

t = Test(100, True, 'float', 'random', bubbleSort)
t.runTest()
t.setTest(100, True, 'float', 'random', selectionSort)
t.runTest()
t.setTest(100, True, 'float', 'random', insertionSort)
t.runTest()
t.setTest(5, True, 'float', 'random', bogoSort)
t.runTest()

t.drawGraph()

