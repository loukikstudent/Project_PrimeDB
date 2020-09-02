import math
import logging

def mersenne_prime(number):
    p = math.log(number+1,2)
    print(type(p))
    if p.is_integer():
        logging.debug("Number %d is a Mersenne Prime number",number)
        return p
    else:
        logging.info("Number %d is not a Mersenne Prime number",number)
        return False

def lucas_lehmer(number):
    p=mersenne_prime(number)
    if p:
        logging.debug("Executing lucas_lehmer for %d",number)


    else:
        lucas()

def lucas():
    pass



if __name__=='__main__':
    while True:
        print(mersenne_prime(int(input())))