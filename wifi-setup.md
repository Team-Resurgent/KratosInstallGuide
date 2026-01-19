# WiFi Setup

This guide will help you configure the WiFi connection for your Kratos front button panel.

## Overview

Kratos supports two methods for WiFi configuration:
- **Normal WiFi Setup** - Connect using your network SSID and password
- **WPS (Wi-Fi Protected Setup)** - Quick connection using the WPS button on your router

Both methods can be configured through the Xbox interface or via the web interface after initial setup.

## Setup Methods

### Method 1: Normal WiFi Setup (SSID & Password)

This is the standard method for connecting to a WiFi network.

#### Step 1: Access Kratos WiFi Settings in PrometheOS

[![Step 1: Access Kratos WiFi Settings in PrometheOS](images/wifisetup/setp1.png)](images/wifisetup/setp1.png)

**Description:** Navigate to the Kratos settings menu in PrometheOS. From the main PrometheOS menu, select Kratos configuration options and choose "WiFi Setup" or "Network Configuration" to begin the WiFi setup process.

---

#### Step 2: Scan and Select WiFi Network

[![Step 2: Scan and Select WiFi Network](images/wifisetup/step2.png)](images/wifisetup/step2.png)

**Description:** Kratos will automatically scan for available WiFi networks. A list of detected networks (SSIDs) will be displayed. Use the controller to navigate and select your WiFi network from the list. Networks are typically sorted by signal strength.

---

#### Step 3: Enter WiFi Password

[![Step 3: Enter WiFi Password](images/wifisetup/step3.png)](images/wifisetup/step3.png)

**Description:** After selecting your network, you'll be prompted to enter the WiFi password. Use the on-screen keyboard to type your network password. Pay attention to case sensitivity and special characters. Press the confirm/enter button when finished.

---

#### Step 4: WiFi Connection Success

[![Step 4: WiFi Connection Success](images/wifisetup/step4.png)](images/wifisetup/step4.png)

**Description:** Once successfully connected, PrometheOS will display a confirmation screen showing your connected network name (SSID) and the assigned IP address. Note down the IP address as you'll need it to access the Kratos web interface. Your Kratos is now connected and ready to use.

---

### Method 2: WPS (Wi-Fi Protected Setup)

WPS provides a quick and easy way to connect without entering a password.

#### Prerequisites

- Your router must support WPS
- WPS must be enabled on your router (check router settings if needed)

#### WPS Setup Steps

1. **Access WiFi Configuration** - Navigate to the Kratos WiFi setup menu from your Xbox dashboard
2. **Select WPS Option** - Choose the WPS connection method from the WiFi setup menu
3. **Activate WPS on Router** - Press the WPS button on your router (usually a physical button on the router)
4. **Wait for Connection** - The Kratos will automatically connect to your network within the WPS time window (typically 2 minutes)
5. **Confirmation** - You'll see a confirmation screen once the connection is established

**Note:** WPS connection must be completed within the router's WPS window (usually 2 minutes after pressing the WPS button).

---

## Web Interface Access

After successful WiFi setup, you can access the Kratos web interface by:

1. Finding the IP address assigned to your Kratos (displayed on the confirmation screen or in the Xbox settings)
2. Opening a web browser on any device connected to the same network
3. Navigating to the Kratos IP address

## Changing WiFi Settings via Web Interface

You can also change WiFi settings after initial setup through the web interface:

1. Access the Kratos web interface using the IP address
2. Navigate to **System Configuration**
3. Scroll to the **WiFi Configuration** section
4. Update your SSID, password, hostname, or Alexa name
5. Click **Save Configuration** to apply changes

**Note:** After changing WiFi settings, you may need to reconnect to the new network if the SSID or password changed.

## Troubleshooting

### Normal WiFi Setup Issues

- **Can't find network:** Ensure your router is broadcasting the SSID and is within range
- **Connection fails:** Double-check your password and ensure your network is 2.4GHz compatible (if applicable)
- **Wrong password:** Verify the password is correct and check for case sensitivity

### WPS Setup Issues

- **WPS not working:** Some routers require WPS to be enabled in router settings first
- **Connection timeout:** Make sure you press the router's WPS button within the setup window
- **WPS not available:** If your router doesn't support WPS, use the normal WiFi setup method instead
- **Router WPS disabled:** Check your router's admin panel to ensure WPS is enabled

## Next Steps

Now that WiFi is configured, you can proceed to [Customization](customization.md) to personalize your Kratos RGB LEDs and settings.

---

[← Back to Main Guide](README.md) | [← Hardware Installation](hardware-installation.md) | [Next: Customization →](customization.md)

