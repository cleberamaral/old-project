def get_average():
    with open("data.txt", 'r') as file_local:
        data = file_local.readlines()
    values = data[1:] # remove header
    values = [float(i) for i in values]
    average_local = sum(values) / len(values)
    return average_local

def get_max():
    grades = [9.6, 9.2, 9.7]
    max_local = max(grades)
    return max_local

max_grade = get_max()
print(max_grade)

