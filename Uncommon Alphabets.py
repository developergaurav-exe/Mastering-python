'''def unique_array(input1, input2):
    total1 = 0
    i = max(len(input1), len(input2))
    
    if i == len(input1):
        for element in input2:
            if element in input1:
                input1.remove(element)
        for element in input1:
            total1 += ord(element)
    
    elif i == len(input2):
        for element in input1:
            if element in input2:
                input2.remove(element)
        for element in input2:
            total1 += ord(element)

    return (total1 - 1) % 9 + 1 if total1 > 0 else 0

print(unique_array(['A','B','C'], ['B','C','D']))

logical error'''

def unique_array(input1, input2):
    i,total1 = 0,0
    
    for element in input2:
        if element in input1:
            input1.remove(element)
    
    for element in input1:
        total1 += ord(element)

    return (total1 - 1) % 9 + 1 if total1 > 0 else 0

print(unique_array(['A','B','C'], ['B','C']))

'''input2 should always be lesser to avoid errors'''
