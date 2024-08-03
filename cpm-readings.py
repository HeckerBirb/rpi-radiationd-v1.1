#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO
from flask import Flask


app = Flask(__name__)

# Counts Per Minute. Anything below ~270 (give or take) 
# is considered fine [citation needed].
cpm = (-1)
counts = 0

current_time = int(time.time())
avg_over = 10  # seconds - pick one of 5, 10, 15, 30, 60


@app.route("/metrics")
def cpm_metric():
    return f'''\
# HELP radiationd_counts_per_min Ambient temperature in celcius
# TYPE radiationd_counts_per_min gauge
radioationd_counts_per_min {cpm}'''


def on_event(channel):
    global counts, cpm, current_time
    counts = counts + 1

    if current_time + avg_over < int(time.time()):
        current_time = int(time.time())
        cpm = counts * (60 // avg_over)
        counts = 0
    # Debug - uncomment to see live counting
    #print(f'Counts: {counts}')


GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.add_event_detect(7, GPIO.FALLING, callback=on_event)


if __name__ == '__main__':
    # Do not run this in production. For testing only.
    app.run(host="0.0.0.0", debug=False, port=80)

