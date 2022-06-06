'''t=int(input())

while t>0:    

    n,m = map(int, input().split())   

    maximum = 0    

    for i in range(n):        

        str = input()          
 
        hash = str.count("#")        

        if maximum < hash:            

            maximum = hash    

            print(maximum)    

t -=1        
'''

t = input()
n =[]
for i in range(int(t)):
    x = input().split(' ')
    n.append(x)
    countHash = 0
    for j in range(int(n[i][0])):
        m = input()
        if countHash<m.count("#"):
            countHash = m.count("#")
    print(countHash)