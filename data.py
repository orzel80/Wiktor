from datetime import datetime
from time import sleep


while True:
    data = datetime.now()
    sleep(3)
    print(data.strftime('%H:%M:%S'))
