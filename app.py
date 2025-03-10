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
    sum = 0
    for rows in data[1:]:
        for index, number in enumerate(rows[1:], start = 1):
            sum = sum + int(number)
        print(f"The average sales for {rows[0]} is {round(sum/index)}")
average(data)
 """

#assignment 2
def average(data):
    sorted = []
    for rows in data[1:]:
        sum = 0
        average = 0
        for index, number in enumerate(rows[1:], start = 1):
            sum = sum + int(number)

        average = round(sum/index)
        print(f"The average sales for {rows[0]} is {average}")
        for index in enumerate[sorted]:
            if average > sorted[index]:
                sorted.insert(index, average)
        print(sorted)
        

average(data)

    
