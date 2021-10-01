print("Hello world")

#7 Prime Number Program in Python
def PrimeFunction(num):  
    if num > 1:  
        for j in range(2, int(num/2) + 1):  
            if (num % j) == 0:  
                print(a, "is not a prime number")  
                break  
        else:  
            print(num, "is a prime number")  
    # If the number is 1  
    else:  
        print(num, "is not a prime number")  

a = int(input("Enter number:"))  
PrimeFunction(a)  
