# Hardware Pinout Reference

A reference for the connectors and buttons on the Kratos Main Board. The installation parts tell you what to plug in and when - this page is here for when you want to identify something on the board itself. Click the diagram for a full-size version.

## Kratos Main Board

[![Pinout diagram of the Kratos Main Board](images/pinout/mainboard-pinout.png)](images/pinout/mainboard-pinout.png)

### Connectors

- **FRONT PANEL** - The 9-pin header for the console's front panel cable. The connector is salvaged from the original front panel board and soldered on in [Part 5](hardware-5-preparing-the-kratos-main-board.md).
- **INPUT** - The 3-pin header carrying the SMBus lines and 5V. Its harness is wired to the console's SMBus in [Part 7](hardware-7-connecting-kratos-to-the-smbus.md).
- **RGB1** and **RGB2** - The two 3-pin JST headers for the Controller Board Connection Cables, one per Kratos Controller Board. The connectors are keyed, so they only go in one way. Fitting these is covered in [Part 5](hardware-5-preparing-the-kratos-main-board.md).
- **ADDON1** and **ADDON2** - Expansion headers. Nothing in the standard kit plugs into these.

### Buttons

- **POWER** - The console power button.
- **EJECT** - The DVD drive eject button.

### Other Points of Interest

- **ESP32-S3** - The module that runs Kratos, including its WiFi.
- **5V STDBY** - An always-on 5V pad on the back of the board. Required on a 1.6 console ([Part 6b](hardware-6b-refitting-the-front-panel-1-6.md)) and optional on 1.0 to 1.5 ([Part 6a](hardware-6a-refitting-the-front-panel-1-0-1-5.md)).

---

[← Back to Main Guide](README.md) | [Hardware Installation](hardware-installation.md)
