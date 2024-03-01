import datetime
debug = True

logPath = 'log.txt'

def log(message):
    with open(logPath, 'a') as f:
        f.write(message + f'{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second} '+ '\n')
        f.close()

def start():
    with open(logPath, 'w') as f:
        f.write('Log file cleared.' + f'{datetime.datetime.now()} ' + '\n')
        f.close()