import time
import threading


def thread_1(i):
    time.sleep(2)
    print("Number of active threads:", threading.active_count())
    print('Value by Thread 1:', i)


def thread_2(i):
    time.sleep(5)
    print("Number of active threads:", threading.active_count())
    print('Value by Thread 2:', i)


def thread_3(i):
    print("Number of active threads:", threading.active_count())
    print("Value by Thread 3:", i)


thread1 = threading.Thread(target=thread_1, args=(1,))
thread2 = threading.Thread(target=thread_2, args=(2,))
thread3 = threading.Thread(target=thread_3, args=(3,))

print("Number of active threads in the starting:", threading.active_count())
print("The active threads in the starting is 1 which is the main thread that executes till the program runs")

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()