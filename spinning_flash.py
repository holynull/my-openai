import time

def spinning_slash():
    while True:
        for slash in ['/', '-', '\\', '|']:
            print('\r{}'.format(slash), end='', flush=True)
            time.sleep(0.1)

# 在主程序中调用 spinning_slash() 函数来展示不停转动的斜杠
spinning_slash()