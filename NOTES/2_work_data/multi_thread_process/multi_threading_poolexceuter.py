from concurrent.futures import ThreadPoolExecutor
import time
def print_num(num):
    time.sleep(2)
    return f"number : {num}"
nums = [1,2,3,4,5,6,7,8,9]
with ThreadPoolExecutor(max_workers=3) as executer:
    reslts = executer.map(print_num,nums)
for i in reslts:
    print(i)