import time
from pywinauto import Desktop
import subprocess
import schedule


def trigger_script2(file_path):
    
    print(f"Triggering script with file path: {file_path}")
    subprocess.run(["python", file_path]) 



def trigger_script(file_path):
    
    print(f"Triggering script with file path: {file_path}")
    subprocess.run(["python", file_path])  




def main():

    file_path = "C:\Pas\Pas_Device_Updater.py"
    file_path2 = "C:\Pas\Record\Record_player.py"
    trigger_script2(file_path2)
    time.sleep(10)
    trigger_script(file_path)
    schedule.every(8).hours.do(main)

if __name__ == "__main__":
    main()

