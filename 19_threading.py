import threading
import time
import random


# ----- THREADS -----
# Threads are blocks of code that takes turns
# executing
def execute_thread(sltime):
    # strftime or string formatted time allows you to
    # define how the time is displayed.
    # You could include the date with
    # strftime("%Y-%m-%d %H:%M:%S", gmtime())

    str_time = time.strftime("%H:%M:%S", time.gmtime())
    # Print when the thread went to sleep
    print("Thread {} sleeps at {}".format(sltime, str_time))

    # Generate a random sleep period of between 1 and
    # 5 seconds
    rand_sleep_time = random.randint(1, 5)

    # Pauses execution of code in this function for
    # a few seconds
    time.sleep(rand_sleep_time)

    str_time = time.strftime("%H:%M:%S", time.gmtime())
    # Print out info after the sleep time
    print("Thread {} stops sleeping at {}".format(sltime, str_time))


for i in range(10):
    # Each time through the loop a Thread object is created
    # You pass it the function to execute and any
    # arguments to pass to that method
    # The arguments passed must be a sequence which
    # is why we need the comma with 1 argument
    thread = threading.Thread(target=execute_thread, args=(i,))
    thread.start()

    # Display active threads
    # The extra 1 is this for loop executing in the main
    # thread
    print("Active Threads :", threading.activeCount())

    # Returns a list of all active thread objects
    print("Thread Objects :", threading.enumerate())
