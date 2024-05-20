import csv
import random
import os

def Show(rows_n, type = "top", separator = ', '):
    with open("Titanic.csv", "r") as csvfile:
        data = list(csv.reader(csvfile))

        header = data[0]
        print("===========================\n", separator.join(header), "\n===========================")
        printed = 0

        if type == "top":
            for row in range(1, len(data)):
                if (printed == rows_n): break
                print(separator.join(data[row]))
                printed += 1
        
        elif type == "bottom":
            for row in reversed(data):
                if (printed == rows_n): break

                print(separator.join(row))
                printed += 1
        
        elif type == "random":
            required = set()

            while len(required) != rows_n:
                required.add(1 if random.randint(0, len(data) - 1) == 0 else random.randint(0, len(data) - 1))
            for i in required:
                print(separator.join(data[i]))


def Info():
    with open("Titanic.csv") as csvfile:
        data = list(csv.reader(csvfile))
        header = data[0]
        print(str(len(data) - 1) + "x" + str(len(header)))

        vals_in_fileds = {}
        for i in header:
            vals_in_fileds[i] = 0
        for row in range(1, len(data)):
            for i in range(len(header)):
                if data[row][i] != '':
                    vals_in_fileds[header[i]] += 1

        valueType = {"PassengerId":"int", 
                 "Survived":"bool", 
                 "Pclass":"int", 
                 "Name":"str", 
                 "Sex":"str", 
                 "Age":"float", 
                 "SibSp":"int", 
                 "Parch":"int", 
                 "Ticket":"str", 
                 "Fare":"float", 
                 "Cabin":"str", 
                 "Embarked":"str"}

        for i in header:

            print(i, vals_in_fileds[i], valueType[i])

def DelNaN():
    with open("Titanic.csv", "r") as csvfile:
        data = list(csv.reader(csvfile))
    

    i = 0
    while(i != len(data)):
        needToDelete = False
        for j in data[i]:
            if j == "":
                needToDelete = True
                break
        if needToDelete:
            data.pop(i)
        else:
            i += 1

    with open("Titanic.csv", "w") as csvfile:


        writer = csv.writer(csvfile)
        writer.writerows(data)

def MakeDS():
    if not os.path.exists("workdata"):
        os.mkdir("workdata")
    if not os.path.exists("workdata/Learning"):
        os.mkdir("workdata/Learning")
    if not os.path.exists("workdata/Testing"):
        os.mkdir("workdata/Testing")

    trainFile = open("workdata/Learning/train.csv", "w")
    testFile = open("workdata/Testing/test.csv", "w")

    with open("Titanic.csv", 'r') as csvfile:
        data = list(csv.reader(csvfile))

        header = data.pop(0)

        trainWriter = csv.writer(trainFile)
        testWriter = csv.writer(testFile)

        trainWriter.writerow(header)
        testWriter.writerow(header)

        for i in data:
            if random.randint(0,9) < 7:
                trainWriter.writerow(i)
            else:
                testWriter.writerow(i)


        testFile.close()
        trainFile.close()
        
            
        



Show(3, "random")
Info()
DelNaN()
MakeDS()
