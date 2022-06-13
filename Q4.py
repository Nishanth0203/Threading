 #que 4
import threading
arraysize=threading.Semaphore(5)
availablesemaphore=5
data=[]
arrayemptylock=threading.Event()
arrayfulllock=threading.Event()
def producer():
    global availablesemaphore
    global data
    for i in range(5):
        if availablesemaphore==0:
            arrayfulllock.wait()
            arrayfulllock.clear()
        arraysize.acquire()
        data.append(i)
        print(f"producer produced {i}")
        availablesemaphore-=1
        arrayemptylock.set()
def consumer():
    global availablesemaphore
    global data
    for i in range(5):
        if availablesemaphore==5:
            arrayemptylock.wait()
            arrayemptylock.clear()
        arraysize.release()
        a=data.pop(0)
        print(f"consumer consumed {a}")
        availablesemaphore+=1
        arrayfulllock.set()
t1=threading.Thread(target=producer)
t2=threading.Thread(target=consumer)
t1.start()
t2.start()