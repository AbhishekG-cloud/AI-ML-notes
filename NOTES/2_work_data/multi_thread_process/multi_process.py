import multiprocessing
import time
def print_num_sq():
    for i in range(5):
        time.sleep(2)
        print(i*i)
def print_let_cube():
    for i in range(5):
        time.sleep(2)
        print(i*i*i)
 # creating threads
if __name__ == "__main__":
    t1 = multiprocessing.Process(target=print_num_sq)
    t2 = multiprocessing.Process(target=print_let_cube)
    t = time.time()
    # starting threads
    t1.start()
    t2.start()
    # joining threads after completion of process
    t1.join()
    t2.join()
    end_time = time.time() - t
    print(end_time)