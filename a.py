""" To print the pattern:
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * * """

n=int(input("enter the number :"))
for i in range(1,n+1):
  print("*"*n)
  
  
""" To print the pattern:
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * * """

num = int(input("Enter the number:"))
for i in range (1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()   

""" To print:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
7 7 7 7 7 7 7
8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10 """

num = int(input("Enter the number:"))
for i in range (1,num+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    

""" To print:
* * * * * * * * * *
* * * * * * * * *
* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
* """
n = int(input("Enter the number:"))
for i in range(n,0,-1):
    print("* "*i)
print()   
#or
""" for i in range(n):
    for j in range(n-i):
        print("*",end = " ")
    print()   """  
    

""" To print:-
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3
4 4 4 4 4 4 4
5 5 5 5 5 5
6 6 6 6 6
7 7 7 7
8 8 8
9 9
10 """

n = int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(n+1-i):
        print(i,end = " ")
    print()    
    

""" To print:
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1 """
n = int(input("Enter the number:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end = " ")
    print()   
    
""" TO print:
10 10 10 10 10 10 10 10 10 10
9 9 9 9 9 9 9 9 9
8 8 8 8 8 8 8 8
7 7 7 7 7 7 7
6 6 6 6 6 6
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
 """

n = int(input("Enter the number:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end = " ")
    print()   
    
    

""" To print:
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2
10 9 8 7 6 5 4 3
10 9 8 7 6 5 4
10 9 8 7 6 5
10 9 8 7 6
10 9 8 7
10 9 8
10 9
10 """

n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    for j in range(n, n - i, -1):
        print(j, end=" ")
    print()  
     #or
""" n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(n - j + 1, end=" ")
    print()     """