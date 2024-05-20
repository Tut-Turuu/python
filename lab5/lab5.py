import csv
import json



def multiplication():
    with open("input1.txt", "r") as file:
        data = map(int, file.read().split(" "))
    
    result = 1
    for i in data:
        result *= i

    
    with open("output1.txt", "w") as file:
        file.write(str(result))

def sort_from_file():
    with open("input2.txt", "r") as file:
        data = map(int, file.read().split("\n"))
    
    data = sorted(data)

    with open("output2.txt", "w") as file:
        for i in data:
            file.write(str(i))
            file.write("\n")


def kindergarten():
    with open("kindergarten.txt", "r") as file:
        children = [i.split(" ") for i in file.read().split("\n")]

    children.sort(key = lambda x: int(x[2]))
    print(children)
    with open("oldest.txt", "w") as file:
        file.write(' '.join(children[-1]))
    
    with open("youngest.txt", "w") as file:
        file.write(' '.join(children[0]))


def json2csv():



    with open("Sample-employee-JSON-data.json", "r") as file:
        data = json.load(file)


    with open("Sample-employee-CSV-data.csv", "w", newline = "") as file:
        writer = csv.DictWriter(file, data["Employees"][0].keys())
        writer.writeheader()
        writer.writerows(data["Employees"])


multiplication()
sort_from_file()
kindergarten()
json2csv()