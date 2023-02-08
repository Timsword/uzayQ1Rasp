import time
from pymavlink import mavutil

def komutDinle(iha):
    # Listen for `STATUSTEXT` messages
    @iha.on_message('STATUSTEXT')
    def handle_statustext_message(self, name, message):
        text = message.text
        if text.startswith("commandGCS:"):
            # Process the message
            print("Received command:", text)
            # You can add your own logic here to handle the received message

    # Wait for messages
    while True:
        time.sleep(1)