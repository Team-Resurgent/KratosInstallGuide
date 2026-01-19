# WiFi Setup

This guide will help you configure the WiFi connection for your Kratos front button panel.

## Overview

Kratos supports two methods for WiFi configuration:
- **Normal WiFi Setup** - Connect using your network SSID and password
- **WPS (Wi-Fi Protected Setup)** - Quick connection using the WPS button on your router

Both methods can be configured through PrometheOS's interface.

## Navigation to WiFi Configuration

Follow these steps to access the WiFi configuration menu in PrometheOS:

### Step 1: Navigate to System

From the PrometheOS home page, select **System** to access system configuration options.

[![Step 1: Navigate to System](images/wifisetup/setp1.png)](images/wifisetup/setp1.png)

---

### Step 2: Navigate to Settings

From the System page, select **Settings** to access device settings.

[![Step 2: Navigate to Settings](images/wifisetup/step2.png)](images/wifisetup/step2.png)

---

### Step 3: Navigate to Kratos Editor

From the Settings page, select **Kratos Editor** to access Kratos-specific configuration options.

[![Step 3: Navigate to Kratos Editor](images/wifisetup/step3.png)](images/wifisetup/step3.png)

---

### Step 4: Navigate to WiFi Details

From the Kratos Editor page, select **WiFi Details** to access WiFi configuration options.

[![Step 4: Navigate to WiFi Details](images/wifisetup/step4.png)](images/wifisetup/step4.png)

---

## Method 1: Standard WiFi Configuration

Once you've reached the WiFi Details page, you can configure your WiFi connection using your network credentials:

1. Enter your **SSID** (WiFi network name) in the SSID field
2. Enter your **Password** (WiFi network password) in the Password field
3. Press **X** to apply the settings and connect

Kratos will attempt to connect to the specified network. You'll see connection status information displayed on the screen.

[![Method 1: Standard WiFi Configuration](images/wifisetup/step5.png)](images/wifisetup/step5.png)

---

## Method 2: WPS (Wi-Fi Protected Setup) Configuration

WPS provides a quick and easy way to connect without entering a password. This method is ideal if your router supports WPS and you want to avoid typing the password.

### Prerequisites

Before using WPS, ensure:
- Your router supports WPS (Wi-Fi Protected Setup)
- WPS is enabled on your router (check your router's admin settings if needed)

### Step 1: Navigate to WPS

From the Kratos Editor page, select **WPS** to access the WPS connection option.

[![Step 1: Navigate to WPS](images/wifisetup/step6.png)](images/wifisetup/step6.png)

---

### Step 2: Connect using WPS

To complete the WPS connection:

1. **Press the WPS button on your router** - This is usually a physical button on your router (may be labeled "WPS" or have a WPS icon)
2. **Press A on your Xbox controller** - This initiates the WPS connection process on Kratos

Kratos will automatically connect to your network. The connection typically completes within 2 minutes. You'll see connection status information on the screen.

[![Step 2: Connect using WPS](images/wifisetup/step7.png)](images/wifisetup/step7.png)

**Important:** The WPS connection must be completed within your router's WPS window (typically 2 minutes). Make sure to press the router's WPS button and then immediately press A on your controller.

---

## Web Interface Access

After successful WiFi setup, you can access the Kratos web interface from any device on your network:

1. **Find the IP address** - The IP address assigned to your Kratos is displayed at the top of the Kratos Editor page
2. **Open a web browser** - On any device connected to the same WiFi network (computer, phone, tablet, etc.)
3. **Navigate to Kratos** - Enter the IP address in your browser's address bar, or use the hostname with `.local` (e.g., `http://kratos-xbox.local`)

The Kratos web interface provides advanced configuration options and additional features not available through PrometheOS.

## Changing WiFi Settings via Web Interface

You can also change WiFi settings after initial setup through the web interface, which provides a more convenient way to update network credentials:

1. Access the Kratos web interface using the IP address or hostname
2. Navigate to **System Configuration** from the main menu
3. Scroll to the **WiFi Configuration** section
4. Update your SSID, password, hostname, or Alexa name as needed
5. Click **Save Configuration** to apply the changes

**Note:** After changing WiFi settings (especially SSID or password), you may need to reconnect your device to the new network to continue accessing the web interface.

## Troubleshooting

### Standard WiFi Setup Issues

- **Can't find network:** Ensure your router is broadcasting the SSID and that your Xbox is within WiFi range. Try moving closer to the router if possible.
- **Connection fails:** Double-check your password for accuracy and ensure your network is 2.4GHz compatible (Kratos may not support 5GHz-only networks)
- **Wrong password:** Verify the password is correct, paying attention to case sensitivity and special characters. Some passwords are case-sensitive.

### WPS Setup Issues

- **WPS not working:** Some routers require WPS to be explicitly enabled in the router's admin settings. Check your router's configuration page.
- **Connection timeout:** Make sure you press the router's WPS button and then immediately press A on your controller within the 2-minute WPS window
- **WPS not available:** If your router doesn't support WPS, use Method 1 (Standard WiFi Configuration) instead
- **Router WPS disabled:** Access your router's admin panel and ensure WPS is enabled in the wireless settings

## Next Steps

Now that WiFi is configured, you can proceed to [Customization](customization.md) to personalize your Kratos RGB LEDs and settings.

---

[← Back to Main Guide](README.md) | [← Hardware Installation](hardware-installation.md) | [Next: Customization →](customization.md)

