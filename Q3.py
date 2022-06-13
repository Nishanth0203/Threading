#threads que3
from threading import *
def printThread(i):
    print("Hello from Thread",i);
def threadNumber(i):
    if(i<50):
        i+=1;
        thread = Thread(target = threadNumber, args=(i,))
        thread.start()
        thread.join()
        printThread(i)
i=0;
threadNumber(i)