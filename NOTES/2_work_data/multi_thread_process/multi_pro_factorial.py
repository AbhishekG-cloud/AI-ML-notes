'''
We know factorial calc is CPU bounded for large numbers to make it easy we can use 
multi-processing
'''
import multiprocessing
import math
import sys
import time
## increase the max number of digits to snusre system dont consider it as an attack
sys.set_int_max_str_digits(10000)
# creating the function
def fact_num(num):
    result =  math.factorial(num)
    print(f"factorial of {num} is {result}")
    return results
if __name__ == " __main__":
    numbers = [500,600,700]
    start = time.time()
    ## creating pool of workers i.e our cores
    with multiprocessing.Pool() as pool:
        results = pool.map(fact_num,numbers)
    end_time = time.time()
    print(f"results are {results}")
    print(f"time taken: {start-end_time} sec")