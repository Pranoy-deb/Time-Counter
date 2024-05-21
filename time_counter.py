import time
from guizero import App, Text, PushButton, Box

def update_time():
    if running:
        elapsed_time = int(time.time() - start_time)
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_text.value = f"{hours:02}:{minutes:02}:{seconds:02}"
        app.after(1000, update_time)

def toggle_timer():
    global running, start_time, elapsed_time
    if running:
        running = False
        elapsed_time = int(time.time() - start_time)  # Store elapsed time when stopped
        toggle_button.text = "Start"
    else:
        start_time = time.time() - elapsed_time  # Continue from where it was stopped
        running = True
        update_time()
        toggle_button.text = "Stop"

running = False
start_time = time.time()
elapsed_time = 0

app = App(title="Time Counter", width=240, height=150,bg="black")

# Time display text
time_text = Text(app, text="00:00:00", size=24, font="Arial", color="white")

# Create a horizontal box to hold the buttons
button_box = Box(app, layout="horizontal")

# Add the toggle button to the box
toggle_button = PushButton(button_box, toggle_timer, text="Start", width=8)
toggle_button.bg = "orange"

app.display()

