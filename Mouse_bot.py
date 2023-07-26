import time
from pynput.mouse import Listener, Button

record_file_path = "C:/Pas/Record/record.txt"

def on_click(x, y, button, pressed):
    if pressed:
        with open(record_file_path, 'a') as file:
            timestamp = time.time()
            action = "click"
            file.write("Timestamp: {} - X: {} - Y: {} - Action: {}\n".format(timestamp, x, y, action))

def on_scroll(x, y, dx, dy):
    with open(record_file_path, 'a') as file:
        timestamp = time.time()
        action = "scroll"
        file.write("Timestamp: {} - X: {} - Y: {} - Action: {}\n".format(timestamp, dx, dy, action))

def on_move(x, y):
    with open(record_file_path, 'a') as file:
        timestamp = time.time()
        action = "move"
        file.write("Timestamp: {} - X: {} - Y: {} - Action: {}\n".format(timestamp, x, y, action))

def start_recording():
    start_time = time.time()
    end_time = start_time + 60  # Record for 30 seconds
    listener = Listener(on_click=on_click, on_scroll=on_scroll, on_move=on_move)
    listener.start()

    while time.time() < end_time:
        pass

    listener.stop()

def main():
    start_recording()

if __name__ == "__main__":
    main()
