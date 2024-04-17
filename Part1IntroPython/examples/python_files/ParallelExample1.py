from multiprocessing import Pool

def sumFunction(n):
    mySum=0
    for i in range(n):
        mySum+=i
    return mySum

if __name__ == '__main__':
    p = Pool(processes=4)
    print(p.map(sumFunction, [10000, 1000, 2000, 2030, 1040, 1000, 1000, 1000]))