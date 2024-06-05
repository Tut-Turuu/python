import numpy as np
import random
import scipy
import time


def task1():
    with open("text1.txt", "r") as file:
        matrix = np.array([[int(j) for j in i.split(", ")] for i in file.read().split("\n")])

    print("Sum:", matrix.sum())
    print("Max:", matrix.max())
    print("Min:", matrix.min())


def task2(x):

    a = []
    b = []

    prev = x[0]
    same_k = 1
    for i in range(1, len(x)):
        if x[i] == prev:
            same_k += 1
        else:
            a.append(prev)
            b.append(same_k)
            prev = x[i]
            same_k = 1
    a.append(prev)
    b.append(same_k)
    
    output = (np.array(a), np.array(b))

    print("Input:", x)
    print("Output:", output)


def task3():
    data = np.array([[int(random.normalvariate(mu=0.0, sigma=100.0)) for j in range(4)] for i in range(10)])

    standard_deviation = ((np.array([((i - (data.sum() / data.size)) ** 2) for i in data]).sum()) * (1 / data.size)) ** 0.5

    print("Data:", data)
    print("Min value:", data.min())
    print("Max value:", data.max())
    print("Mid value:", data.sum() / data.size)
    print("Standartnoe otklonenie:", standard_deviation)

    first5 = data[0:5]

def task4(x):
    
    prev = x[0]
    max_el = -100000
    for i in range(1, len(x)):
        if prev == 0:
            max_el = max(max_el, x[i])
        prev = x[i]

    print(x)
    if max_el == -100000:
        return print("None") 
    print("result:", max_el)



def task5(N, D):

    m = np.array([random.randint(1, 100) for i in range(D)])
    X = np.array([np.array([random.randint(1, 100) for i in range(D)]) for j in range(N)])
    C = np.array([np.array([0 for i in range(D)]) for j in range(D)])

    while True:
        for i in range(D):
            for j in range(i + 1):
                C[i][j] = random.randint(1, 100)
                C[j][i] = C[i][j]
        
        flag = True
        for i in range(1, D + 1):
            temp = np.array([np.array([0 for k in range(i)]) for j in range(i)])
            
            for j in range(i):
                for k in range(i):
                    temp[j][k] = C[j][k]

            if np.linalg.det(temp) < 0:
                flag = False
        
        if flag:
            break

    
    def Myltivariative_normal_logpdf(D, X, m, C):
        return -(D/2) * np.log(2 * np.pi) - 0.5 * np.log(np.linalg.det(C)) - 0.5 * np.sum((X - m) @ np.linalg.inv(C) * (X - m), axis = 1)
    
    print("X:", X)
    print("m:", m)
    print("C:", C)
    print("This: ", Myltivariative_normal_logpdf(D, X, m, C))
    print("Scipy: ", scipy.stats.multivariate_normal(m, C).logpdf(X))


    MyStart = time.time()

    for i in range(1000):
        Myltivariative_normal_logpdf(D, X, m, C)
    MyFinish = time.time()

    ScipyStart = time.time()

    for i in range(1000):
        scipy.stats.multivariate_normal(m, C).logpdf(X)
    ScipyFinish = time.time()

    print("My Time:", MyFinish - MyStart, "Scipy Time:", ScipyFinish - ScipyStart)


def task6():
    a = np.arange(16).reshape(4, 4)
    print("Array:", a)

    tmp = a[0].copy()
    a[0] = a[2]
    a[2] = tmp

    print("New array:", a)


def task7():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    iris = np.genfromtxt(url, delimiter=",", dtype = "object")
    unique = set()

    for i in iris:
        unique.add(i[4])
    
    print("Unique:", unique)
    print("Number of Unique:", len(unique))




def task8(x):

    res = []
    for i in range(len(x)):
        if x[i] != 0:
            res.append(i)

    print(res)


# task1()
# task2(np.array([random.randint(0, 6) for i in range(random.randint(1, 30))]))
# task3()
# task4(np.array([random.randint(0,10) for i in range(random.randint(1,20))]))


task5(  int(input("Enter N: ")),
        int(input("Enter D: "))
    )
# task6()
# task7()
# task8(np.array([random.randint(0,10) for i in range(random.randint(1,20))]))