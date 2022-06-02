from threading import Thread
from time import sleep

def threaded_function(arg, awal):
    hasil = awal
    for i in range(arg):
        hasil= hasil + i
    print(hasil)
        # sleep(1)


if __name__ == "__main__":
    thread = Thread(target = threaded_function, args = (3, 1))
    thread.start()
    thread.join()
    print("thread finished...exiting")