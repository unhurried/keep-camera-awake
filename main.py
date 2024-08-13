import subprocess
import pyautogui
import time
import psutil

subprocess.run('start "" "microsoft.windows.camera:"', shell=True)

pid = None
for proc in psutil.process_iter(['pid', 'name']):
    if 'WindowsCamera' in proc.info['name']:
        print(proc.info)
        pid = proc.info['pid']

while True:
    if not psutil.pid_exists(pid):
        break
    try:
        pyautogui.leftClick()
        time.sleep(15)
    except:
        pass
