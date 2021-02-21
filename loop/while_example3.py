import time

message = '''
Detected keyboard input
End the process'''

try:
    print('Start the process')
    while True:
        time.sleep(1)
        print('zzz')
except KeyboardInterrupt:
    print(message)
