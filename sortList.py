#sorting the list


def checkIfNotNumeric(*args):
    for x in args:
        if not(isinstance(x, (int, float))):
            return False
    return True

#find min value of the list
def findMin(L):
    m = L[0]
    idx = 0
    counter = 0 
    for x in L:
        if x < m:
            m = x
            idx = counter
        counter += 1
    return m, idx

#swaping the values
def swapValues(L, idx1, idx2):
    tmp = L[idx1]
    L[idx1] = L[idx2]
    L[idx2] = tmp
    return L

#sort the list
def sortList(L):
    for i in L:
        if not(checkIfNotNumeric(i)):
            print("Error: List does not contain numeric values")    
        else:
            counter = 0
            for x in L:
                m,idx = findMin(L[counter:])
                L = swapValues(L,(idx+counter),counter)            
                counter +=1
            return L
     




