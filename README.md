# AWS_IoT_AnynetClick_RaspberyPi3_Python3_Weather
Example For Raspbery PI3 written in Python3 to read data from a Weather Click and publish to the AWS IoT Service using an Anynet Click cellular module

Readme for the preparation of the Raspberry Pi Click Modules

Required:

Raspberry Pi 3 Model B with SD Card with fresh raspbian install
(installation notes were prepared using 2017-11-29-raspbian-stretch.img

Click Modules:
Pi 3 click shield
AnyNet 2G click
Weather click

The AnyNet click module is plugged into slot 1 of the click shield for both demos.

The Weather click module plugs into slot 2 of the click shield.


1. On first boot open a terminal and run 'sudo raspi-config' this allows you to modify the hardware and boot parameters

Select '5 Interfacing Options' and

Enable P4 SPI

Enable P5 I2C

Disable the serial login shell option P6


2. We found we need to fully disable to login service to avoid UART problems, use the following commands:

sudo systemctl stop serial-getty@ttyS0.service
sudo systemctl disable serial-getty@ttyS0.service

Next, edit /boot/cmdline.txt and remove the part of the command line that references the serial login if it exists eg: console=serial0,115200

Edit the file /boot/config.txt to enable the UART
sudo nano /boot/config.txt

If it doesn't already exist, add the line:
enable_uart=1

You may just have to set the value to 1 from 0.


3. Reboot the Pi

4. Run the weather example

See the picture in <to be added> for click module slot configuration

python3.5 ./py3_aws_weather.py

This example publishes weather data to the topic WEATHER.
