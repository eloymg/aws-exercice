import time

def stillCPU():
    a = True
    t = time.time()
    while(a):
        time.sleep(0.00001)
        if (time.time() - t)>10:
            a=False

if __name__ == '__main__':
    stillCPU()
