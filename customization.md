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

A **palette** is a collection of colors that work together to create visual effects. Configure up to 10 colors for your LED effect palette. These colors are used in various dynamic effects and will cycle through or blend together depending on your effect settings.

- **Color 1** through **Color 10** - Individual palette colors

**Tip:** Choose colors that complement each other for smoother, more visually appealing effects. You can create themes like warm colors (reds, oranges, yellows) or cool colors (blues, greens, purples).

### Destination Color

Set a destination color used in color transitions and effects. This is the target color that animations will transition toward or blend with. It's particularly useful for effects that fade between colors.

### Shift Configuration

Control how colors shift and move across the LED strip. **Shifting** refers to how colors move along the LED array.

- **Shift Type:**
  - **Rotate Left/Right** - Colors move in a circular pattern, wrapping around from one end to the other (like a rotating wheel)
  - **Scroll Left/Right** - Colors move linearly across the strip, with new colors appearing at one end as others disappear at the opposite end
  - **Randomize** - Colors change positions randomly, creating a chaotic, dynamic effect

- **Amplitude** - Controls the intensity or distance of the shift effect (0-65535). Higher values create more dramatic movements, while lower values create subtle shifts. Think of it as controlling how far or how much the colors move with each animation step.

### Easing Functions

**Easing** (also called interpolation) controls how animations accelerate and decelerate, making movements feel natural rather than mechanical. Instead of moving at a constant speed, easing creates smooth acceleration and deceleration curves.

Think of it like a car: **Linear** easing is like constant speed, while **Ease In** is like slowly accelerating from a stop, and **Ease Out** is like gradually braking to a stop. **Ease In Out** combines both for a smooth start and finish.

Each easing type can be configured with:

- **Speed (ms)** - Duration of the easing animation in milliseconds (0-65535). Lower values make animations faster, higher values make them slower. For example, 1000ms = 1 second.

- **Easing Type** - Choose from 34 different easing functions that control the acceleration curve:
  - **Start** - Animation begins immediately at full speed
  - **End** - Animation maintains speed until the end
  - **Linear** - Constant speed throughout (no acceleration/deceleration)
  - **Random** - Speed varies randomly
  - **Sine Ease In/Out/In Out** - Smooth, gentle curves using sine wave mathematics (very natural feeling)
  - **Quad/Cubic/Quart/Quint Ease In/Out/In Out** - Progressively stronger acceleration curves (Quad = squared, Cubic = cubed, etc.)
  - **Exponent Ease In/Out/In Out** - Exponential curves for very dramatic acceleration
  - **Circle Ease In/Out/In Out** - Circular curves for smooth, rounded transitions
  - **Back Ease In/Out/In Out** - Creates a slight "overshoot" effect, like a rubber band
  - **Elastic Ease In/Out/In Out** - Bouncy, spring-like effect with oscillation
  - **Bounce Ease In/Out/In Out** - Bouncing effect at the end, like a ball hitting the ground

- **Ping Pong** - Enable to make the animation reverse direction when it reaches the end, creating a back-and-forth motion instead of looping from the beginning

#### Available Easing Configurations

Kratos provides four separate easing controls for different aspects of the LED effects:

1. **Shift Easing** - Controls how the shift effect animates (how colors move along the LED strip)
2. **Palette Easing** - Controls how the system transitions between different palette colors
3. **Movement Easing** - Controls general movement animations and positional changes
4. **Cross Fade Easing** - Controls how colors blend together when transitioning (cross-fading is when one color gradually fades out while another fades in)

### Effect Options

Additional effect toggles:

- **Mirror Effect** - Mirror the LED pattern across the center of the LED strip. This creates a symmetrical effect where the left and right sides reflect each other, like looking in a mirror. Perfect for creating balanced, visually pleasing patterns.

- **Interpolate Fill** - Enable smooth color interpolation between palette colors. **Interpolation** means calculating intermediate colors between two palette colors to create smooth gradients. Without this, colors might change abruptly; with it enabled, you get smooth color transitions that blend naturally between your palette colors.

## WiFi Configuration

Configure WiFi and network settings:

- **SSID** (Service Set Identifier) - Your WiFi network name that appears when scanning for networks (max 31 characters). This is the name you see when looking for WiFi networks on your phone or computer.

- **Password** - Your WiFi network password (max 63 characters). The security key required to connect to your WiFi network.

- **Hostname** - Network hostname for your Kratos device (max 63 characters). This is the name your Kratos will use on your local network. Other devices can use this name to find your Kratos instead of using the IP address. For example, if set to "kratos-xbox", you might access it at `http://kratos-xbox.local` instead of `http://192.168.1.100`.

- **Alexa Name** - Name used for Alexa integration (max 63 characters). This is the name you'll use when giving voice commands to Alexa to control your Kratos. For example, "Alexa, turn on [Xbox Original]".

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

**OTA** (Over-The-Air) updates allow you to update your Kratos firmware wirelessly without needing physical access to the device. Update your Kratos firmware over-the-air:

1. Navigate to **Firmware Update** from the main menu
2. Upload a new firmware file
3. The system will update automatically
4. Your configuration settings are preserved during updates

**Note:** Keep your Kratos powered on and connected to WiFi during the update process. Do not power off or interrupt the update.

### Credits & About

View the Amiga-style cracktro with:
- SID music playback
- Plasma visual effects
- Development credits

Navigate to **Credits & About** from the main menu.

## Tips for Customization

- **Start Simple** - Begin with basic colors and gradually add effects. It's easier to understand how each setting works when you change one thing at a time.

- **Use the Load Button** - Always load current config before making changes to see existing settings. This helps you understand what's currently configured and avoid losing your work.

- **Experiment with Easing** - Different easing functions create unique animation feels:
  - Use **Sine Ease In Out** for smooth, natural movements
  - Use **Elastic** or **Bounce** for playful, energetic effects
  - Use **Linear** for consistent, mechanical movements
  - Use **Back Ease** for a subtle overshoot effect

- **Palette Colors** - Create harmonious color palettes for smoother effects. Colors that are close together on the color wheel (like blue and purple, or red and orange) will create smoother transitions.

- **Ping Pong Mode** - Great for creating back-and-forth animations that feel more dynamic than simple loops.

- **Mirror Effect** - Perfect for symmetrical LED layouts. Works especially well when you have an equal number of LEDs on each side.

- **Speed Settings** - Start with medium speeds (1000-3000ms) and adjust from there. Very fast speeds (<500ms) can be hard to see, while very slow speeds (>10000ms) may feel sluggish.

- **Amplitude** - Start with moderate values and adjust based on your LED count. More LEDs can handle higher amplitude values for more dramatic effects.

## Troubleshooting

- **Settings Not Saving** - Ensure you're connected to the same WiFi network as your Kratos
- **Colors Not Updating** - Try reloading the configuration page and loading current settings
- **Effects Not Visible** - Check that LED counts are set correctly for your hardware
- **WiFi Changes** - After changing WiFi settings, you may need to reconnect to the new network

---

[← Back to Main Guide](README.md) | [← WiFi Setup](wifi-setup.md)
