import threading
import time
def print_num():
    for i in range(5):
        time.sleep(2)
        print(i)
def print_let():
    for i in "abcde":
        time.sleep(2)
        print(i)
 # creating threads
t1 = threading.Thread(target=print_num)
t2 = threading.Thread(target=print_let)
t = time.time()
# starting threads
t1.start()
t2.start()
# joining threads after completion of process
t1.join()
t2.join()
end_time = time.time() - t
print(end_time)