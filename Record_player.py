import time
from pynput.mouse import Controller as MouseController
from pynput.mouse import Button

def replay_mouse_record(record_file_path):
    mouse = MouseController()
    with open(record_file_path, 'r') as file:
        events = []
        for line in file:
            line = line.strip()
            if line:
                event = line.split(" - ")
                if len(event) == 4:
                    timestamp = float(event[0].split(": ")[1])
                    x = int(event[1].split(": ")[1])
                    y = int(event[2].split(": ")[1])
                    action = event[3].split(": ")[1]
                    events.append((timestamp, x, y, action))

        if events:
            start_time = time.time()
            total_duration = events[-1][0] - events[0][0]  # Total duration of the recording
            print("Playback started at:", start_time)
            for i, event in enumerate(events):
                timestamp, x, y, action = event

                current_time = time.time()
                elapsed_time = current_time - start_time
                remaining_time = total_duration - elapsed_time

                print("Event:", "Timestamp: {} - X: {} - Y: {} - Action: {}".format(timestamp, x, y, action))
                print("Current Time:", current_time)
                print("Elapsed Time:", elapsed_time)
                print("Remaining Time:", remaining_time)

                if i < len(events) - 1:
                    next_event = events[i + 1]
                    next_timestamp = next_event[0]
                    time.sleep(next_timestamp - timestamp)

                if action == "move":
                    print("Moving Mouse to ({}, {})".format(x, y))
                    mouse.position = (x, y)
                elif action == "scroll":
                    print("Scrolling")
                    mouse.scroll(0, int(x))  # Adjust the scroll amount as needed
                elif action == "click":
                    print("Clicking")
                    mouse.position = (x, y)
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                # Add more conditions for other actions (press, release) if necessary

    print("Mouse record replay completed.")

def main():
    record_file_path = "C:/Pas/Record/record.txt"
    replay_mouse_record(record_file_path)


if __name__ == "__main__":
    main()
