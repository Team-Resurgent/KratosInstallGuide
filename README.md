# Kratos Installation Guide

Welcome to the Kratos installation guide! This guide will walk you through installing and configuring your Kratos front button panel replacement for the original Xbox.

## About Kratos

KRATOS is the ultimate OGX front button panel replacement, crafted in collaboration between Team Resurgent and EqUiNoX Mods. It packs a modern feature set into a clean, drop-in upgrade for your original Xbox setup.

## Features

### Lighting

- **The whole front of the console lights up** - fully customizable RGB across the front panel and both controller ports, and each controller board passes the lighting on outwards, so you can carry on into more LEDs beyond the console
- **An optional RGB ring**, running its own effect independently of the panel
- **The Kratos Light Synthesizer** - lighting is built the way a synth builds a sound, so it is not a fixed list of animations. Choose a palette of up to ten colours, pick the source that drives them (a sweep or scanner, random twinkles, or drifting noise like plasma and lava), then shape it with an envelope of fade in, hold and fade out. The combinations do not run out
- **18 built-in presets** - Aurora, Breathing Rainbow, Candy Cane, Confetti, Cyber, Fire, Halloween, Knight Rider, Lava, Marquee, Ocean, Pacifica, Plasma, Purple Haze, Rainbow, Sunset, Twinkle and Xbox Green
- **Save your own presets**, and export or import them to share
- **Try before you keep it** - presets and effects play on the real LEDs as you browse them, and nothing is saved until you say so
- **Your console's real status, in your own colours** - Kratos reads the original green, red and amber status signals and shows them however you like
- Brightness, hue and effect speed adjust independently for the panel and the ring

### Everyday Use

- **Power and eject work exactly like the original panel** - the buttons are where you expect them and behave the same
- **Buzzer tones** on power on, power off and eject
- **Teach it your existing remote** - the original Xbox DVD remote works, as do ordinary NEC remotes, and up to 64 buttons can be learned. A button can be taught power on, off or toggle, eject, or brightness, hue and speed for the panel, the ring, or both at once

### Voice and Smart Home

- **Shows up in Apple Home, Google Home and Amazon Alexa** over Matter
- **Three devices, not one** - the front panel as a colour light, the ring as a second colour light, and the Xbox itself as a power switch
- **Turn your Xbox on by voice**, or from your phone anywhere in the house. This needs the standby feed fitted during installation, covered in [Part 6a](hardware-6a-refitting-the-front-panel-1-0-1-5.md) and [Part 6b](hardware-6b-refitting-the-front-panel-1-6.md)
- Alexa can also find Kratos on its own for power on and off, without Matter

### On Your Network

- **Set it up before you install it** - Kratos runs from USB-C on its own, so it can be on your WiFi and proven working on the desk before the console is ever opened, as covered in [Part 1](hardware-1-before-you-start.md)
- **Three ways to connect** - type in your details, press the WPS button on your router, or let Kratos host its own setup hotspot
- **Reachable by name** at `http://kratos-xbox.local`, and the hostname is yours to change
- **Stays awake while the Xbox is off**, which is what lets it answer a voice command or a tap in an app

### Updates and Recovery

- **Over-the-air updates** - new firmware arrives over your network, no cables and no disassembly
- **A separate recovery firmware** sits alongside the main one, so an update that goes wrong is not a dead panel
- **Recovery without a computer** - the onboard boot button brings back the setup hotspot or starts WPS if the WiFi details are ever wrong
- **A factory reset that keeps your WiFi** - put the lighting and settings back to stock without having to get Kratos back on the network afterwards, or clear everything if that is what you want

### Expansion

- **Two add-on headers** - one takes an IR receiver and a PC speaker buzzer, the other drives the LED ring, with a spare IO line left over
- **Room to grow** - Kratos already carries a setting for a future add-on board that will play audio on power on, power off, eject and more
- **Longer LED runs** from the pass-through header on each controller board - up to 128 LEDs per side, and up to 64 on the ring
- **Ordinary strips work** - standard WS2812 and SK6812 LEDs, with a colour order setting per strip so an off-the-shelf reel does not come out with its reds and greens swapped
- **A separate brightness control** for everything past the bezel, so an external string does not have to match the panel

### Hidden Extras

- There are a few things in the web interface we have not listed here. Have a poke around.

## Configuring Kratos

Three ways in, depending on where you are and what you are doing:

- **The Kratos Settings Utility, on the Xbox** - a controller-driven app that talks to the board over the console's own internal bus, so it works before WiFi is set up. Changes preview on the real LEDs before you save them. This is where [WiFi Setup](software-wifi-setup.md) happens
- **The web interface, from any browser** - the full set of options from a computer, phone or tablet on your network, plus a web API if you would rather drive Kratos from your own scripts
- **[The Kratos Service Utility](https://github.com/Team-Resurgent/KratosServiceUtility/), on a computer** - firmware flashing over USB and a serial log viewer, running on Windows, macOS and Linux. You will not need it for a normal installation; it is there for manual updates and for getting out of trouble. Download it from the [releases page](https://github.com/Team-Resurgent/KratosServiceUtility/releases)

The web interface carries its own documentation, so the details travel with the hardware rather than living in a download somewhere. There is a guide to building your own effects with the synthesizer, a full web API reference for automating Kratos from your own scripts or home automation, and the protocol Kratos speaks to the console over its internal bus.

## What's Included

Each Kratos kit includes:
- 1x Kratos Main Board
- 2x Kratos Controller Boards
- 1x SMBus Harness - the single-ended 3-wire JST lead for the **INPUT** header
- 2x Controller Board Connection Cables

## Installation Guide Sections

This guide is organized into the following sections:

1. **[Hardware Installation](hardware-installation.md)** - Step-by-step guide for physically installing the Kratos board and components
2. **[WiFi Setup](software-wifi-setup.md)** - Configure your Kratos WiFi connection
3. **[Pinout Reference](reference-pinout.md)** - Identify the connectors, buttons and pads on all three Kratos boards

## Getting Started

Before you begin, make sure you have:
- Your Kratos kit with all components
- Basic tools for opening your Xbox
- Optional WiFi network available

Start with the [Hardware Installation](hardware-installation.md) guide to begin your installation.
