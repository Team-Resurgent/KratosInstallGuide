# Hardware Pinout Reference

A reference for the connectors and buttons on the Kratos boards. The installation parts tell you what to plug in and when - this page is here for when you want to identify something on a board itself. Click any diagram for a full-size version.

Left and right are as you face the front of the console, the same convention used in [Part 4](hardware-4-preparing-the-controller-ports.md).

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

### Power

The board has two 5V rails, which is what the **5V (PRIMARY)** and **5V (SECONDARY)** pins in the diagram refer to:

- **5V primary** powers the ESP32-S3, **RGB1**, **RGB2** and **ADDON2**.
- **5V secondary** powers **ADDON1**.

The **5V STDBY** pad on the back of the board is an alternative feed for the primary rail. That is what makes it useful for keeping Kratos powered while the console is off - required on a 1.6 console ([Part 6b](hardware-6b-refitting-the-front-panel-1-6.md)) and optional on 1.0 to 1.5 ([Part 6a](hardware-6a-refitting-the-front-panel-1-0-1-5.md)).

### Other Points of Interest

- **ESP32-S3** - The module that runs Kratos, including its WiFi.

## Kratos Left Controller Board

[![Pinout diagram of the Kratos left Controller Board](images/pinout/controller-left-pinout.png)](images/pinout/controller-left-pinout.png)

- **RGB1** - Takes the Controller Board Connection Cable from **RGB1** on the main board, plugged in during [Part 5](hardware-5-preparing-the-kratos-main-board.md).
- **OUT** - The pass-through header, carrying 5V, RGB and GND on from this board.
- **5V ALT** - A pad for feeding in 5V from the controller ports. Only the right board uses it - the left board has no 5V source of its own and runs on the 5V arriving from the right board.
- **Solder links** - There is one beside each header. Bridge the one beside **RGB1** and leave the one beside **OUT** alone.

## Kratos Right Controller Board

[![Pinout diagram of the Kratos right Controller Board](images/pinout/controller-right-pinout.png)](images/pinout/controller-right-pinout.png)

- **RGB2** - Takes the Controller Board Connection Cable from **RGB2** on the main board, plugged in during [Part 5](hardware-5-preparing-the-kratos-main-board.md).
- **OUT** - The pass-through header, carrying 5V, RGB and GND on from this board.
- **5V ALT** - Where the 5V wire from the port 4 controller port board is soldered, as covered in [Part 4](hardware-4-preparing-the-controller-ports.md).
- **Solder links** - There is one beside each header. Bridge the one beside **RGB2** and leave the one beside **OUT** alone.

---

[← Back to Main Guide](README.md) | [Hardware Installation](hardware-installation.md)
