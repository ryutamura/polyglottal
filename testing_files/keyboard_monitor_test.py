from pynput.keyboard import Listener

def on_release(key):
    strkey = str(key)
    print(type(key))
    print(strkey)
    print(type(strkey))
    print(f'{key} key released')
    if key == 'q':
        return False


with Listener(on_release=on_release) as listener:
    listener.join()