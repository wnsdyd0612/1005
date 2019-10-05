import sys

input_file = "supplier_data.csv"
output_file = "output_data.csv"

with open(input_file, 'r') as filereader:
        with open(output_file, 'w') as filewriter:
            header = filereader.readline()
            header = header.strip()
            header_list = header.split()
            print(header_list)
            filewriter.write(','.join(map(str, header_list))+'\n')
            for row in filereader:
                row = row.strip()
                row_list = row.split(',')
                print(row_list)    
                filewriter.write(','.join(map(str, row_list))+'\n')