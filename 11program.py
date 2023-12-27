def uniqueelements(inputlist):

    uniqueset = set(inputlist)
    
 
    uniquelist = list(uniqueset)
    
    return uniquelist


originallist = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
result = uniqueelements(originallist)
print(result)
