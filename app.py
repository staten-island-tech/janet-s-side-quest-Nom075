## This function opens the CSV for You!
def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)

    return data_list


file_path = "SalesData.csv"  
data = csv_to_list(file_path)

#Assignment 1
""" def average(data):
    total = 0
    for rows in data[1:]:
        for index, number in enumerate(rows[1:], start = 1):
            total = total + int(number)
        print(f"The average sales for {rows[0]} is {round(total/index)}")
average(data)
 """

#assignment 2
""" def average(data):
    sorted = []
    for rows in data[1:]:
        total = 0
        average = 0
        for index, number in enumerate(rows[1:], start = 1):
            total = total + int(number)

        average = round(total/index)
        store_name = rows[0]
        sorted.append((store_name, average))
        sorted.sort(key = lambda x: x[1])

        print(sorted)
        

average(data) """

#assignment 3   
""" def average(data):
    sorted = []
    for rows in data[1:]:
        total = 0
        average = 0
        for index, number in enumerate(rows[1:], start = 1):
            total += int(number)

        average = round(total/index)
        store_name = rows[0]
        sorted.append((store_name, average))
        sorted.sort(key = lambda x: x[1])

    print(sorted)
    all_average = sum(x[1] for x in sorted)/len(sorted)
    print(all_average)
        

average(data)
 """

""" #assignment 4
def average(data):
    sorted = []
    for rows in data[1:]:
        total = 0
        average = 0
        for index, number in enumerate(rows[1:], start = 1):
            total += int(number)

        average = round(total/index)
        store_name = rows[0]
        sorted.append((store_name, average))
        sorted.sort(key = lambda x: x[1])

    print(sorted)
    all_average = sum(x[1] for x in sorted)/len(sorted)
    print(f"All store average: {all_average}")
    for value in sorted:
        if value[1] < 0.8*all_average:
            print(f"{value[0]} is in danger of being closed.")

        

average(data) """

#master function
def average(data):
    sorted = []
    for rows in data[1:]:
        total = 0
        average = 0
        for index, number in enumerate(rows[1:], start = 1):
            total += int(number)

        average = round(total/index)
        store_name = rows[0]
        sorted.append((store_name, average))
        sorted.sort(key = lambda x: x[1])

    print(sorted)
    all_average = sum(x[1] for x in sorted)/len(sorted)
    print(f"All store average: {all_average}")
    for value in sorted:
        if value[1] < 0.8*all_average:
            print(f"{value[0]} is in danger of being closed.")

        

average(data)
