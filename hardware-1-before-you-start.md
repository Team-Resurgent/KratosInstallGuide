# Part 1: Before You Start

This guide covers one recommended way of installing Kratos. It is not the only way to wire it up, but it is the route we suggest.

The approach here takes the 5V feed from the controller ports, which is fused on the Xbox. If anything shorts, that fuse takes the hit rather than the console.

## Optional: Get Kratos Onto Your WiFi First

Kratos runs happily from USB-C power on its own, so you can get it onto your WiFi and confirm it is working before the console is ever opened up. If you would rather leave it, WiFi can also be set up from the Xbox afterwards - see [WiFi Setup](software-wifi-setup.md).

Connect a USB-C cable to the Kratos Main Board to power it up. From there, there are two ways to get it onto your network.

## Method 1: Kratos Setup Access Point

1. Short press the boot button - the LED breathes white to show Kratos is in setup mode
2. On your phone or computer, connect to the **kratos-setup** WiFi network
3. Browse to [http://192.168.4.1](http://192.168.4.1), enter your WiFi details and save
4. Switch your phone or computer back to your home WiFi
5. Browse to [http://kratos-xbox.local](http://kratos-xbox.local) to confirm Kratos is online

## Method 2: WPS

1. Long press the boot button to start WPS - the LED blinks white while WPS mode is active
2. Press the WPS button on your router - the connection has to complete inside the router's WPS window, typically 2 minutes
3. Browse to [http://kratos-xbox.local](http://kratos-xbox.local) to confirm Kratos is online

---

[← Hardware Installation](hardware-installation.md) | [Next: Part 2 - Opening Your Xbox →](hardware-2-opening-your-xbox.md)
