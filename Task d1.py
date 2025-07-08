'''
try:
    with open("sample.txt", "r") as file:
        print("Reading file content:")
        for line_num, line in enumerate(file, start=1):
            print("Line ",line_num,": ",line.strip())


except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
'''


try:
    with open("sample.txt", "r") as file:
        print("Reading file content:")
        line_num = 1
        for line in file:
            print("Line", line_num, ":", line.strip())
            line_num += 1


except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
