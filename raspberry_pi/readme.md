- logon to pi using VNC(Virtual Network Computer) - see and control the Raspberry Pi OS desktop from another computer
   on your network using a VNC client;
- Raspberry Pi Software Configuration Tool
  - ```sudo raspi-config```
- Interfaces tab 
  - The Interfaces tab holds settings which control the hardware interfaces available on Raspberry Pi.
    - Camera: Enables or disables the Camera Serial Interface (CSI), for use with a Raspberry Pi Camera Module.
    - SSH: Enables/disables the Secure Shell (SSH) interface; it allows you to open a commandline interface on Raspberry Pi from another computer on your network using an SSH client.
    - VNC: Enables/disables the Virtual Network Computing (VNC) interface; it allows you to view 
      - the desktop on Raspberry Pi from another computer on your network using a VNC client.
    - SPI: Enables or disables the Serial Peripheral Interface (SPI), used to control some hardware add-ons which connect to the GPIO pins.
    - I2C: Enables or disables the Inter-Integrated Circuit (I²C) interface, used to control some hardware add-ons which connect to the GPIO pins.
    - Serial Port: Enables or disables Raspberry Pi’s serial port, available on the GPIO pins.
    - Serial Console: Enables or disables the serial console, a command-line interface available on the serial port. 
      - This option is only available if the Serial Port setting above is set to Enabled.
    - 1-Wire: Enables or disables the 1-Wire interface, used to control some hardware add-ons which connect to the GPIO pins.
    - Remote GPIO: Enables or disables a network service which allows you to control Raspberry Pi’s GPIO pins from another computer on your network using the GPIO Zero library. 
      - More information on remote GPIO is available from gpiozero.readthedocs.io.
- Raspberry pi starter kit
  - breadboard
  - jumper cables
  - switch
  - led
  - Resistors
  - piezoelectric buzzer?
  - motors
  - infrared (IR) SENSORS
  - humidity sensor
  - soil moisture sensor
  - temperature sensor
  - light dependent resistors(LDRs)
  - sense HAT
  - camera
- Raspberry Pi models:
  1. Raspberry Pi 1 Model A and B:
      - CPU: Broadcom BCM2835, 700 MHz ARM1176JZF-S
      - RAM: 256 MB (Model A), 512 MB (Model B)
      - Ports: 2 USB 2.0, HDMI, GPIO pins, Ethernet (Model B), and more.
  2. Raspberry Pi 2 Model B:
      - CPU: Broadcom BCM2836, 900 MHz quad-core ARM Cortex-A7
      - RAM: 1 GB
      - Ports: 4 USB 2.0, HDMI, GPIO pins, Ethernet, and more.
  3. Raspberry Pi 3 Model B:
      - CPU: Broadcom BCM2837, 1.2 GHz quad-core ARM Cortex-A53
      - RAM: 1 GB
      - Ports: 4 USB 2.0, HDMI, GPIO pins, Ethernet, Wi-Fi, Bluetooth, and more.
  4. Raspberry Pi 3 Model B+:
      - CPU: Broadcom BCM2837B0, 1.4 GHz quad-core ARM Cortex-A53
      - RAM: 1 GB
      - Ports: 4 USB 2.0, HDMI, GPIO pins, Gigabit Ethernet, Wi-Fi, Bluetooth, and more.
  5. Raspberry Pi 4 Model B:
      - CPU: Broadcom BCM2711, 1.5 GHz quad-core ARM Cortex-A72
      - RAM: 2 GB, 4 GB, or 8 GB options
      - Ports: 2 USB 3.0 and 2 USB 2.0, dual micro HDMI, GPIO pins, Gigabit Ethernet, Wi-Fi, Bluetooth, and more.
  6. Raspberry Pi Zero and Zero W:
      - CPU: Broadcom BCM2835, 1 GHz single-core ARM1176JZF-S
      - RAM: 512 MB (Zero W), 256 MB (Zero)
      - Ports: Mini HDMI (Zero W), HDMI adapter (Zero), micro-USB, GPIO pins, Wi-Fi (Zero W).
- The Raspberry Pi Pico is a microcontroller board released by the Raspberry Pi Foundation. 
  - It's a departure from the traditional Raspberry Pi single-board computers and is designed for embedded systems and microcontroller projects. 
  - Here are some key specifications of the Raspberry Pi Pico:
    1. Microcontroller: RP2040
        - Dual-core ARM Cortex-M0+ processor running at up to 133 MHz.
        - 264KB of SRAM.
    2. GPIO Pins: 26 programmable GPIO pins.
        - These pins can be used for digital input/output, PWM, UART, I2C, SPI, and more.
    3. Peripherals:
        - 2 × UART, 2 × SPI controllers, 2 × I2C controllers, 3 × 12-bit ADCs, 16 × controllable PWM channels.
    4. Input Voltage: 1.8V to 5.5V.
        - This makes it compatible with a wide range of power sources.
    5. USB Connectivity: Micro USB for power and data.
        - The Pico can be programmed using MicroPython, C/C++, and other programming languages.
    6. Flash Memory: 2MB of onboard QSPI Flash memory.
        - This is where you can store your program and data.
    7. Programmability:
        - Can be programmed using MicroPython, CircuitPython, C/C++, and various other development environments.
    8. Dimensions: 51mm x 21mm.
    - The Raspberry Pi Pico is a versatile and affordable microcontroller that's great for a wide range of projects, 
    - from simple LED blinking to more complex IoT and robotics applications. 
    - It's often used in combination with other components and sensors to build custom electronics projects.
