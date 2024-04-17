from multiprocessing import Pool

def f(x):
    return "Hello "+str(x)

if __name__ == '__main__':
    p = Pool(4)
    print(p.map(f, [1, 2, 3, 7, 8, 9]))
