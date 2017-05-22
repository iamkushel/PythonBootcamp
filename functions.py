def isprime(num):
    for i in range(2, num):
        if num%i == 0:
            print("Not a prime")
            break
    else:
         print("It is prime")

isprime(14)
