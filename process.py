log_file = open("um-server-01.txt")
# creating the variable log_file and making it open the server text file

def sales_reports(log_file):
# defining a function called sales_reports that takes in log_file as a parameter
    for line in log_file:
        # creating a for loop that loops through every line in the log_file, which is the server text file
        line = line.rstrip()
        # removing any white spaces at the end of each line
        day = line[0:3]
        # creating a day variable that holds the line at indexes 0-3
        if day == "Tue":
            # standard if statement checking if day is equal to the 'Tue' string
            print(line)
            # printing the line to the console


sales_reports(log_file)
# calling the sales_reports function and passing in the log_file as an argument
