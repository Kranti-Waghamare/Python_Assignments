def ChkPrime(Data):
    Value = 2
    Count = 0
    
    for No in Data : 
        if((No % Value) != 0):
            Count += 1

    return Count
        

def ListPrime(Data):

    Sum = 0

    for No in Data:

        if(No < 2):
            continue

        IsPrime = True

        for i in range(2, No):

            if(No % i == 0):
                IsPrime = False
                break

        if(IsPrime == True):
            Sum = Sum + No

    return Sum


