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
            
        if self.order == 'ascending':
            entry.sort()
        elif self.order == 'descending':
            entry.sort(reverse=True)
            
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
    def drawGraph(self, axes):
        
        if axes == 'execution time x number of comparisons':
            # x axis
            x = list(self.comparisons)
            # y axis
            y = list(self.executionTimes)
            
            # plot the data
            i = 0
            while i < len(self.algorithms):
                plt.plot(np.linspace(0,x[i], 100), np.linspace(0, y[i], 100), label=self.algorithms[i] + ' (N = ' +  str(self.sizes[i]) + ')')
                i = i + 1
            
            plt.xlabel('N?? Compara????es')
            plt.ylabel('Tempo de execu????o (s)')
            
        else:
            bubbleSortData = {'x': [], 'y': []}
            selectionSortData = {'x': [], 'y': []}
            insertionSortData = {'x': [], 'y': []}
            bogoSortData = {'x': [], 'y': []}
            heapSortData = {'x': [], 'y': []}
            mergeSortData = {'x': [], 'y': []}
            quickSortData = {'x': [], 'y': []}
            
            i = 0
            # set the X axe
            while i < len(self.algorithms):
                if(self.algorithms[i] == 'bubbleSort'):
                    bubbleSortData['x'].append(self.sizes[i])
                elif(self.algorithms[i] == 'selectionSort'):
                    selectionSortData['x'].append(self.sizes[i])
                elif(self.algorithms[i] == 'insertionSort'):
                    insertionSortData['x'].append(self.sizes[i])
                elif(self.algorithms[i] == 'bogoSort'):
                    bogoSortData['x'].append(self.sizes[i])
                elif(self.algorithms[i] == 'heapSort'):
                    heapSortData['x'].append(self.sizes[i])
                elif(self.algorithms[i] == 'mergeSort'):    
                    mergeSortData['x'].append(self.sizes[i])
                elif(self.algorithms[i] == 'quickSort'):
                    quickSortData['x'].append(self.sizes[i])
                i = i + 1
            
            # set the y axe 
            if axes == 'number of comparisons x size':
                i = 0
                while i < len(self.algorithms):
                    if(self.algorithms[i] == 'bubbleSort'):
                        bubbleSortData['y'].append(self.comparisons[i])
                    elif(self.algorithms[i] == 'selectionSort'):
                        selectionSortData['y'].append(self.comparisons[i])
                    elif(self.algorithms[i] == 'insertionSort'):
                        insertionSortData['y'].append(self.comparisons[i])
                    elif(self.algorithms[i] == 'bogoSort'):
                        bogoSortData['y'].append(self.comparisons[i])
                    elif(self.algorithms[i] == 'heapSort'):
                        heapSortData['y'].append(self.comparisons[i])
                    elif(self.algorithms[i] == 'mergeSort'):
                        mergeSortData['y'].append(self.comparisons[i])
                    elif(self.algorithms[i] == 'quickSort'):
                        quickSortData['y'].append(self.comparisons[i])
                    i = i +1
                    plt.ylabel('N?? Compara????es')
                    
            # set the y axe 
            elif axes == 'execution time x size':
                i = 0
                while i < len(self.algorithms):
                    if(self.algorithms[i] == 'bubbleSort'):
                        bubbleSortData['y'].append(self.executionTimes[i])
                    elif(self.algorithms[i] == 'selectionSort'):
                        selectionSortData['y'].append(self.executionTimes[i])
                    elif(self.algorithms[i] == 'insertionSort'):
                        insertionSortData['y'].append(self.executionTimes[i])
                    elif(self.algorithms[i] == 'bogoSort'):
                        bogoSortData['y'].append(self.executionTimes[i])
                    elif(self.algorithms[i] == 'heapSort'):
                        heapSortData['y'].append(self.executionTimes[i])
                    elif(self.algorithms[i] == 'mergeSort'):
                        mergeSortData['y'].append(self.executionTimes[i])
                    elif(self.algorithms[i] == 'quickSort'):
                        quickSortData['y'].append(self.executionTimes[i])
                    i = i +1
                    plt.ylabel('Tempo de execu????o (s)')
            
            plt.xlabel('Tamanho')
            # set the labels
            plt.plot(bubbleSortData['x'], bubbleSortData['y'], label='bubble sort')
            plt.plot(selectionSortData['x'], selectionSortData['y'], label='selection sort')
            plt.plot(insertionSortData['x'], insertionSortData['y'], label='insertion sort')
            plt.plot(bogoSortData['x'], bogoSortData['y'], label='bogosort')
            #plt.plot(heapSortData['x'], heapSortData['y'], label='heap sort')
            #plt.plot(mergeSortData['x'], mergeSortData['y'], label='merge sort')
            #plt.plot(quickSortData['x'], quickSortData['y'], label='quick sort')

            
        # unique = 'Unique' if self.unique else 'Non unique'
        # numberType = ' floats' if self.type == 'float' else ' integers' 
        # order =  ' numbers in ' + self.order + ' order'
        # plt.title(unique + numberType + order)
        
        plt.legend()
        plt.show()    
        print('Graph Generated')

    # sets a new test based on the parameters 
    def setTest(self, n, unique, type, order, algorithm):
        self.n = n
        self.unique = unique
        self.type = type
        self.order = order
        self.algorithm = algorithm
        


t = Test(10, False, 'integer', 'random', bubbleSort)
t.runTest()

t.setTest(100, False, 'integer', 'random', bubbleSort)
t.runTest()

t.setTest(1000, False, 'integer', 'random', bubbleSort)
t.runTest()

t.setTest(10, False, 'integer', 'random', selectionSort)
t.runTest()

t.setTest(100, False, 'integer', 'random', selectionSort)
t.runTest()

t.setTest(1000, False, 'integer', 'random', selectionSort)
t.runTest()

t.setTest(10, False, 'integer', 'random', insertionSort)
t.runTest()

t.setTest(100, False, 'integer', 'random', insertionSort)
t.runTest()

t.setTest(1000, False, 'integer', 'random', insertionSort)
t.runTest()


t.drawGraph('execution time x size')

