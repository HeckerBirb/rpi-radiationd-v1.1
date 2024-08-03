# rpi-radiationd-v1.1
RadiationD v1.1 Python POC for Raspberry-Pi 5

This POC produces a simple web service with Flask that can be scraped by Prometheus (for displaying graphs on Grafana).

## Requirements:
* `sudo apt remove python3-rpi.gpio`
* `python3 -m pip install rpi-lgpio flask`

## Connecting the board to the Raspberry-Pi 5
* Connect the pins as shown in the two images below. I connected GND and 5V to any GND and 5V on the RPi, and VIN (which is actually the output pin, not the input pin!) to the RPi GPIO pin 7 (GPIO 4). (Oh, and apologies for using gray and white cables in the same setup. :) )
![RadiationD pins](/images/radiationd-pins.jpg)
![RPi pins](/images/rpi-5-pins.jpg)


## Run the POC:
* `./cpm-readings.py` (or possibly `python cpm-readings.py` if you have not set execute permissions or are using Windows)
* Navigate to the endpoint /metrics, e.g., http://127.0.0.1/metrics


## More resources:
* Migrating from RPi 4 GPIO scripts to 5: https://gpiozero.readthedocs.io/en/stable/migrating_from_rpigpio.html
* RPi 5 GPIO library: https://pypi.org/project/rpi-lgpio/
* Lots of detailed information about the RadiationD board: https://github.com/SensorsIot/Geiger-Counter-RadiationD-v1.1-CAJOE-

