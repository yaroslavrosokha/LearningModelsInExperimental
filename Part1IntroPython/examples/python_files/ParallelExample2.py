from multiprocessing import Pool
import time

def sumFunction(n):
    mySum=0
    for i in range(n):
        mySum+=i
    return mySum

if __name__ == '__main__':
    for i in range(1,10):
        p = Pool(processes=i)
        startTime=time.time()
        p.map(sumFunction, [20000000 for x in range(12)])
        endTime=time.time()
        p.close()
        print("Using ",i," processors it took", endTime-startTime, " seconds")