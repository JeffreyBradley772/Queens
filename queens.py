'''
Author: Jeffrey Bradley and Will Meddick
Project #5
File Name: queens.py
Description:
This program places 8 queens on a standard chess board such that each
queen is "safe" from the others.
'''
if __name__ == '__main__':


    
    def diagonalCheck1(list1):
                    
        for n in range(0,len(list1)):
            item = list1[n]
            for i in list1:
                j = list1.index(item)
                t = list1.index(i)
                #print(item,i)
                #print(j,t)
                diff = j - t
                #print(diff)
                #print('-------')
                if diff != 0:
                    x = len(list1)
                        #print(x)
                    for P in range(1,x + 1):
                        if diff == -P or diff == P:
                            if i == item + P or i == item - P:
                                #print(diff, i, t, item, j)
                                #print("bad")
                                return None
                            #else:
                                #print("fine")
        return list1

            

    
    def rowcheck(list1):
        
        #print(len(list1))
        for n in range(0,len(list1)):
            count = 0
            k = 0
            x = list1[n]
            for i in list1:

                if x == i:
                    count += 1

                if count > 1:
                    #print(x,i,count,k)
                    #print("BAD")
                    return None
        
        return list1

    def iterate(list1):
        for i in range(0,rows):
            list1[i] += 1
            if list1[i] < rows:
                return list1
            else:
                list1[i] = 0
        





    
    def board(list1):
        
        #for i in list1:
         #   column = list1.index(i)
          #  row = i
            
        for n in range(rows):
            for j in list1:
                x = j
                if x == n:
                    place = list1.index(j)
                    #print(x,n)
                    #print(place)
                    print('----'*rows)

                    print('|   '*(place) + "| X " + '|   '*((rows-1)-place)+ '|')
        print('----'*rows)
                
    rows = int(input("Enter a number of rows great than or equal to 4: ",))
    list1 =[0 for x in range(rows)]
    count = 0
    while True:
        if count > 0:
            break


        iterate(list1)
        
        

        

        
        while True:
            x = rowcheck(list1)
            if x == None:
                break
            j = diagonalCheck1(list1)
            if j == None:
                break
            solution = j
            print(solution)
            board(solution)
            count+=1
            break
    
        
    
      
   
    
        
            
        
