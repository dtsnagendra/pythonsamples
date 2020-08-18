def squr():
    n = 1
    while n>0 :
      n = int(input("Enter the number "))
      if n>0:
        a=n**2
        print(a)
      else:
        print("Enter the +ve number ")


def sum_even_odd():
    n = int(input("Enter a number :"))
    sumeve = 0
    sumodd = 0
    i=1
    for i in range (1,n+1):
        if i%2==0:
            sumeve = sumeve+i
        else:
            sumodd = sumodd+i
        i=i+1    
    print(sumeve)
    print(sumodd)


def half_pyiramid():
    n=int(input("Enter the number :"))
    a=input("Enter the char :")
    for i in range(1,n+1):
      for j in range(1,i+1):
        if a == "" :
            print(j,end='\t')
        else:
            print(a,end='\t')
      print('\n')

