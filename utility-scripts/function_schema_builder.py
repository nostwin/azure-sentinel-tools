'''

Script that generates functions to replicate Azure LAW built-in table schemas.

// Extract Table column-type dict
IdentityInfo
| getschema
| extend pack = bag_pack(ColumnName, ColumnType)
| summarize make_bag(pack)
'''
import csv
import json
import os
from typing import Optional

MODE = 'auto'  # modes: auto, manual (lowercase)

# for auto mode
CSV_DIR: str = './schemas'

# for manual mode
column_type_dict: list[dict] = [

]

def get_files(dir_path: str) -> list[str]:
    files = []
    for file in os.listdir(dir_path):
        if file.endswith('.csv'):
            files.append(os.path.join(dir_path, file))
    return files


def get_schemas(file_list: list[str]) -> list[dict]:
    column_type_dict = []
    for file in file_list:
        with open(file, newline='') as csvfile:
            rows = list(csv.reader(csvfile))
            data = json.loads(rows[1][0])
        column_type_dict.append(data)
    return column_type_dict


def generate_function_schemas(column_type_dict: list[dict], file_name_list: Optional[list[str]] = None):
    function_list = []
    for table in column_type_dict:
        datatable_schema = ""
        for column_name, column_type in table.items():
            datatable_schema += f"{column_name}:{column_type},"
        function = f"datatable({datatable_schema}) []"
        function_list.append(function)
        print(function)
    export_to_file(function_list, file_name_list)


def export_to_file(function_list: list[str], file_name_list: [list[str]]):
    tracker = 0
    with open('schemas.txt', 'w') as file:
        for function in function_list:
            if file_name_list:
                file.write(f"{file_name_list[tracker]}:\n{function}\n")
            else:
                file.write(f"Function {tracker}:\n{function}\n")
            tracker += 1
    print("Function Schemas Successfully generated")


if __name__ == '__main__':
    match MODE:
        case 'manual':
            generate_function_schemas(column_type_dict)
        case 'auto':
            file_list = get_files(CSV_DIR)
            column_type_dict = get_schemas(file_list)
            generate_function_schemas(column_type_dict, file_list)


