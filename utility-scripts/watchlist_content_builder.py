'''
Script used to generate the rawContent value for watchlist templates
1. Specify the file path of the csv.
2. Copy and paste the output in the rawContent value.
'''

import csv

FILE_PATH: str = '../test.csv'


def csv_to_string(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        print(repr(reader))
        rows = list(reader)

    header = rows[0]
    data = rows[1:]

    output = ','.join(header) + '\r\n'
    output += '\r\n'.join([','.join(row) for row in data])

    return output


if __name__ == '__main__':
    output_string = csv_to_string(FILE_PATH)
    # Must delete \' and "
    output_string.replace(r"\'", "").replace("'", "")

    with open("../output.txt", 'w') as file:
        file.write(repr(output_string))
