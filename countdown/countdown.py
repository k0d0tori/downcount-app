from datetime import datetime
import re
import eel
import sys
import os

# Restaring the app
@eel.expose
def restart():
    os.execv(sys.executable, ['python'] + sys.argv)

# Computes the downcount each second, then passes it onto JS
@eel.expose
def infou(d):
    d = datetime.strptime(d, '%d/%m/%Y %H:%M:%S')
    while True:
        dt = str(d - datetime.now())
        if re.findall(r'(.*) day', dt):
            dt = re.findall(r'(.*) day', dt)[0] + ':' + re.findall(r', (.*)\.', dt)[0]
            dt = dt.split(':')
            dt = '<b>' + dt[0] + '</b> days, ' + '<b>' + dt[1] + '</b> hours, ' + '<b>' + dt[2] + '</b> minutes, ' + '<b>' + dt[3] + '</b> seconds'
        else:
            dt = (dt.split('.')[0]).split(':')
            dt = '<b>0</b> days, ' + '<b>' + dt[0] + '</b> hours, ' + '<b>' + dt[1] + '</b> minutes, ' + '<b>' + dt[2] + '</b> seconds'

        eel.countdown(dt)
        if len(re.findall(r'0' , dt)) == 6:
            eel.countdown('DownCount Over')
            break
        eel.sleep(1)

# Starting the app
eel.init('Web')
eel.start('index.html', size = (950, 650))
