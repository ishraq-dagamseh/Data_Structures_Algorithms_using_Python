def fact(n):
    if n==0:
        return 1
    
    print("n before is:",n)
    result=n*fact(n-1)
    print("n after is:",n)

    return result
print(fact(9))