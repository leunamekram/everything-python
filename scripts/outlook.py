import psutil
import time
import os

def is_outlook_running():
    for p in psutil.process_iter(attrs=['pid', 'name']):
        if "OUTLOOK.EXE" == p.info['name']:
            print("Yes", p.info['name'], "is running")
            break
    else:
        print("No, Outlook is not running")
        os.startfile("outlook")
        print("Outlook is starting now...")
    # time.sleep(10)
    # os.system("taskkill /f /im outlook.exe")

def is_teams_running():
    for p in psutil.process_iter(attrs=['pid', 'name']):
        if "Teams.exe" == p.info['name']:
            print("Yes", p.info['name'], "is running")
            break
    else:
        print("No, Teams is not running")
        # os.startfile("Teams.exe")
        os.system('C:/Users/msapunga/AppData/Local/Microsoft/Teams/Update.exe --processStart "Teams.exe"')
        print("Teams is starting now...")
    # time.sleep(10)
    # os.system("taskkill /f /im Teams.exe")

if __name__ == '__main__':
    is_outlook_running()
    is_teams_running()