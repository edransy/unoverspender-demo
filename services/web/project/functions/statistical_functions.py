def calcualte_mean(l):
    if (len(l) != 0):
        mean = 0
        for i in l:
            mean += i
        
        mean = mean / len(l)
    
        return mean
    
    else:
        return 0