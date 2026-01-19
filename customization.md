# Customization

This guide covers how to customize your Kratos front button panel using the web interface. All customization options are available through the System Configuration panel accessible from the main Kratos web interface.

## Accessing the Configuration Panel

1. After WiFi setup, access the Kratos web interface by navigating to the Kratos IP address in your browser
2. Click on **System Configuration** from the main menu
3. The configuration panel will load with all available options

## Front Panel Configuration

### Sound Settings

Configure the front panel sound output:

- **None** - No sound output
- **Buzzer** - Enable buzzer sound effects

### Status Color

Set the color for the front panel status indicator. This color is used for general status display.

### LED Count Configuration

Configure the number of LEDs on each side of the front panel:

- **Left LED Count** - Number of LEDs on the left side (0-255)
- **Right LED Count** - Number of LEDs on the right side (0-255)

### Main Colors

Configure the colors for different front panel states:

- **Main Color (Off)** - Color when the system is off
- **Main Color (Green)** - Color for green status indicator
- **Main Color (Red)** - Color for red status indicator
- **Main Color (Amber)** - Color for amber status indicator

Each color can be selected using the color picker interface.

## LED Effects Configuration

### Palette Colors

Configure up to 10 colors for your LED effect palette. These colors are used in various dynamic effects:

- **Color 1** through **Color 10** - Individual palette colors

### Destination Color

Set a destination color used in color transitions and effects.

### Shift Configuration

Control how colors shift and move across the LED strip:

- **Shift Type:**
  - Rotate Left
  - Scroll Left
  - Rotate Right
  - Scroll Right
  - Randomize

- **Amplitude** - Controls the intensity of the shift effect (0-65535)

### Easing Functions

Kratos supports extensive easing functions for smooth animations. Each easing type can be configured with:

- **Speed (ms)** - Duration of the easing animation (0-65535)
- **Easing Type** - Choose from 34 different easing functions:
  - Start
  - End
  - Linear
  - Random
  - Sine Ease In/Out/In Out
  - Quad Ease In/Out/In Out
  - Cubic Ease In/Out/In Out
  - Quart Ease In/Out/In Out
  - Quint Ease In/Out/In Out
  - Exponent Ease In/Out/In Out
  - Circle Ease In/Out/In Out
  - Back Ease In/Out/In Out
  - Elastic Ease In/Out/In Out
  - Bounce Ease In/Out/In Out
- **Ping Pong** - Enable to make the animation reverse direction when it reaches the end

#### Available Easing Configurations

1. **Shift Easing** - Controls how the shift effect animates
2. **Palette Easing** - Controls palette color transitions
3. **Movement Easing** - Controls movement animations
4. **Cross Fade Easing** - Controls color cross-fade transitions

### Effect Options

Additional effect toggles:

- **Mirror Effect** - Mirror the LED pattern across the center
- **Interpolate Fill** - Enable smooth color interpolation between palette colors

## WiFi Configuration

Configure WiFi and network settings:

- **SSID** - Your WiFi network name (max 31 characters)
- **Password** - Your WiFi network password (max 63 characters)
- **Hostname** - Network hostname for your Kratos device (max 63 characters)
- **Alexa Name** - Name used for Alexa integration (max 63 characters)

## Loading and Saving Configuration

### Loading Current Configuration

1. Click the **Load Current Config** button
2. The form will populate with all current settings from your Kratos device
3. A success message will confirm when the configuration is loaded

### Saving Configuration

1. Make your desired changes to any settings
2. Click the **Save Configuration** button
3. A success message will confirm when settings are saved
4. Your configuration will persist across reboots

**Note:** The configuration automatically loads when you open the configuration page, so you can see your current settings immediately.

## Web Interface Features

The Kratos web interface provides several additional features:

### Games Collection

Access retro arcade games directly from the web interface:
- **Asteroids** - Classic space shooter
- **Frogger** - Classic arcade game

Navigate to **Games Collection** from the main menu to play.

### Firmware Update (OTA)

Update your Kratos firmware over-the-air:

1. Navigate to **Firmware Update** from the main menu
2. Upload a new firmware file
3. The system will update automatically
4. Your configuration settings are preserved during updates

### Credits & About

View the Amiga-style cracktro with:
- SID music playback
- Plasma visual effects
- Development credits

Navigate to **Credits & About** from the main menu.

## Tips for Customization

- **Start Simple** - Begin with basic colors and gradually add effects
- **Use the Load Button** - Always load current config before making changes to see existing settings
- **Experiment with Easing** - Different easing functions create unique animation feels
- **Palette Colors** - Create harmonious color palettes for smoother effects
- **Ping Pong Mode** - Great for creating back-and-forth animations
- **Mirror Effect** - Perfect for symmetrical LED layouts

## Troubleshooting

- **Settings Not Saving** - Ensure you're connected to the same WiFi network as your Kratos
- **Colors Not Updating** - Try reloading the configuration page and loading current settings
- **Effects Not Visible** - Check that LED counts are set correctly for your hardware
- **WiFi Changes** - After changing WiFi settings, you may need to reconnect to the new network

---

[← Back to Main Guide](README.md) | [← WiFi Setup](wifi-setup.md)
