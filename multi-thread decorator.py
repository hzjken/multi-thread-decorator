# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 17:53:13 2018

@author: Ken Huang
"""

import threading

def eachThread(func, num, partList, localVar, outputList):
    '''A helper function for each thread.'''
    output = ''
    localVar.num = num
    localVar.partList = partList
    localVar.output = output
    for i in range(len(num)):
        try:
            output = func(partList[i])
            outputList.append((num[i],output))
        except:
            outputList.append((num[i],None))


def multiThread(func, List, threadNum = 20):    
    '''A multi threading decorator.
       func: the function to be implemented in multi-threaded way.
       List: the input list.
       threadNum: the number of threads used, can be adjusted for different tasks.
    '''
    List = list(List)
    localVar = threading.local()
    outputList = []
    line = []
    for i in range(threadNum):
        num = range(i,len(List),threadNum)
        partList = [List[j] for j in num]
        t = threading.Thread(target= eachThread, args=(func, num, partList, localVar, outputList))
        line.append(t)
        t.start()
    for t in line:
        t.join()    
    outputList = sorted(outputList, key = lambda x:x[0])
    outputList = [x[1] for x in outputList]
    
    return outputList