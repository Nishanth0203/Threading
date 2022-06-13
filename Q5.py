#que5
import threading
import time
arraysize=threading.Semaphore(5)
availablesemaphore=5
data=[]
mainlock=threading.RLock()
arrayemptylock=threading.Event()
arrayfulllock=threading.Event()
def producer():
    global availablesemaphore
    global data
    global mainlock
    for i in range(5):
        if availablesemaphore==0:
            arrayfulllock.wait()
            arrayfulllock.clear()
        mainlock.acquire()
        data.append(i)
        print(f"producer produced {i}")
        availablesemaphore-=1
        mainlock.release()
        time.sleep(5)
        arrayemptylock.set()

def consumer():
    global availablesemaphore
    global data
    for i in range(5):
        if availablesemaphore==5:
            arrayemptylock.wait()
            arrayemptylock.clear()
        mainlock.acquire()
        a=data.pop(0)
        print(f"consumer consumed {a}")
        availablesemaphore+=1
        mainlock.release()
        time.sleep(3)
        arrayfulllock.set()
t1=threading.Thread(target=producer)
t2=threading.Thread(target=consumer)
t1.start()
t2.start()