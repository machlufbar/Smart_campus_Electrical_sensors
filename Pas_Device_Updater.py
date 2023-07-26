import csv
import json
import os
import requests
import schedule
import time
import pyodbc
import subprocess

def export_mdb_columns_to_csv(mdb_file_path, csv_file_path, column_names):
    conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + mdb_file_path
    connection = pyodbc.connect(conn_str)
    cursor = connection.cursor()

    select_columns = ','.join(f'[{column}]' for column in column_names)
    select_query = f'SELECT {select_columns} FROM [RT Data Log #0]'

    cursor.execute(select_query)
    rows = cursor.fetchall()

    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(column_names)

        for row in rows:
            if len(row) == len(column_names):
                writer.writerow([str(row[index]) if row[index] is not None else "" for index in range(len(column_names))])
            else:
                writer.writerow(["" for _ in range(len(column_names))])

    connection.close()



def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as file:
        csv_data = csv.DictReader(file)
        json_data = [row for row in csv_data]

    with open(json_file, 'w') as file:
        json.dump(json_data, file)
    print("Data has been Converted to a Json File ")            


    

def run_cmd_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    print("The data sended successfully")
    return output, error

def export_and_send_data():
    mdb_file_path = "C:\Pas\Samples\Sampless.mdb"  
    csv_file_path = "C:\Pas\Samples\Sampless_csv"  
    column_names = ["V1", "V2", "V3", "I1", "I2", "I3", "kWh IMPORT"]  
    device_id = "6f24b7e0-f4c7-11ed-a00e-098052e37df7" 
    thingsboard_url = "https://app.hittest.smarty.camp" 
    access_token = "DieqiYpQeb3sOvPfDUwi"
    command ='curl -X POST https://app.hittest.smarty.camp/api/v1/DieqiYpQeb3sOvPfDUwi/telemetry -H "Content-Type: application/json" -d "@C:\Pas\Samples\Sampless_json"'

    export_mdb_columns_to_csv(mdb_file_path, csv_file_path, column_names)
    print(f"Data from columns '{', '.join(column_names)}' has been exported to '{csv_file_path}'.")
    csv_to_json('C:\Pas\Samples\Sampless_csv', 'C:\Pas\Samples\Sampless_json')
    run_cmd_command(command)

def main():
    export_and_send_data()

if __name__ == "__main__":
    main()

