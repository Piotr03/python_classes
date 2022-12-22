import os
from csv import reader
from csv import writer


# variable for a directory storing stock exchange file 
directory = 'C:\\Users\\augus\\Downloads\\python_hw'

# loop for iterating over all files in the above directory
for filename in os.listdir(directory):
    fullpath = (directory + '\\' + filename)
    # check if a given file is a csv file
    if filename[-4:] == '.csv':
        with open(fullpath, 'r') as read_obj, \
                open(fullpath.replace('.csv', '_new.csv'), 'w', newline='') as write_obj:
            csv_reader = reader(read_obj)
            csv_writer = writer(write_obj)
            #loop for each row in a currently iterated csv file
            for i, row in enumerate(csv_reader):
                # for header row 
                if i == 0:
                    row.append('Change')
                else:
                    newcol = (float(row[4]) - float(row[1])) / float(row[1])
                    row.append(newcol)
                # adding rows one by one to the new file 
                csv_writer.writerow(row)