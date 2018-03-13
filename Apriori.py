from numpy import *
import numpy as np

L1 = {}
path = './homework1.dat'


def takeCutSet(input_set, data, minsup=3):
    for key in input_set:
        SetItem = []
        for item in key:
            SetItem.append(item)
        for line in data:
            judge = True
            for item in SetItem:
                if item not in line:
                    judge = False
                    break
            if judge:
                input_set[frozenset(SetItem)] += 1
    output_set = {}
    for line in input_set.keys():
        if input_set[line] >= minsup:
            output_set[line] = input_set[line]
    return output_set


def readData(minsup=3):
    L1 = {}
    # O(mn)
    fileReader = open(path)
    fileReaderList = []
    for line in fileReader:
        lineList = line.split()
        fileReaderList.append(lineList)
        for element in lineList:
            if element not in L1:
                L1[element] = 1
            else:
                L1[element] += 1
    output_init_set = {}
    for key in L1.keys():
        if L1[key] >= minsup:
            output_init_set[key] = L1[key]
    return fileReaderList, output_init_set


def readSampleData(minsup=3):
    L1 = {}
    simpDat = [['r', 'z', 'h', 'j', 'p'],
               ['r', 'z', 'h', 'j', 'p'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    # O(mn)
    #fileReader = open(path)
    #fileReaderList = []
    #for line in fileReader:
    #    lineList = line.split()
    #    fileReaderList.append(lineList)
    #    for element in lineList:
    #        if element not in L1:
    #            L1[element] = 1
    #        else:
    #            L1[element] += 1
    for line in simpDat:
        for element in line:
            if element not in L1:
                L1[element] = 1
            else:
                L1[element] += 1
    output_init_set = {}
    for key in L1.keys():
        if L1[key] >= minsup:
            output_init_set[key] = L1[key]
    return simpDat, output_init_set


def join(input_set):
    output_set = {}

    for key1 in input_set.keys():
        for key2 in input_set.keys():
            if key1 != key2 and len(frozenset(set(key1) | set(key2))) == len(set(key1)) + 1:
                output_set[frozenset(set(key1) | set(key2))] = 0
    return output_set


def run_apriori():
    data, init_set = readData()
    print(data)
    print('The %d turns:' %1)
    print(init_set)
    ret_set = join(init_set)
    result = takeCutSet(ret_set, data)
    end_result = result
    i = 2
    while len(result.keys()) > 0:
        end_result = result
        print('The %d turns:' %i)
        print(result)
        ret_set = join(result)
        result = takeCutSet(ret_set, data)
    return end_result

end = run_apriori()
print(end)