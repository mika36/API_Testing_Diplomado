import math

def isPrimeNumber(number):
    initialNumber = number-1
    secNumber = initialNumber - 1
    while(secNumber>1):
        multiplier = initialNumber*secNumber
        initialNumber = multiplier
        secNumber = secNumber - 1
    numberToVerify = initialNumber + 1

    if(numberToVerify % number == 0):
        print("El numero " + str(number) + " es primo")
    else:
        print("El numero " + str(number) + " no es primo")
isPrimeNumber(12)