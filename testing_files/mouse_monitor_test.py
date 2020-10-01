from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    
    if pressed:
        print(f'Mouse clicked at {x}, {y} with {button}')
    if not pressed:
        # return False
        listener.stop()
    
    


with Listener(on_click=on_click) as listener:
    listener.join()