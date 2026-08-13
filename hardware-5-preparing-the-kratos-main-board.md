# Part 5: Preparing the Kratos Main Board

The Kratos Main Board uses the same 9-pin connector as the original front panel board, so the connector has to be transferred across before the board can go in. It is soldered in place and its wires sit in slot contacts, so this step needs patience rather than force.

**You will need:** a soldering iron, solder, desoldering braid or a solder sucker, flux, isopropyl alcohol with a soft brush for cleaning up afterwards, and a fine pick or side cutters for the harness in Step 5.

**Use plenty of flux.** Fresh flux makes the old solder flow at a lower temperature and for longer, so you spend less time heating the pads and are far less likely to lift one. It is worth using on both the desoldering and the soldering.

## Step 1: Unclip the Original Board from the Front Panel

The original front button panel board clips into the back of the front panel you removed in Part 3. Release the clips and lift the board away - it should come out without any force.

## Step 2: Desolder the 9-Pin Connector

The connector needs to come off the original board intact so it can be reused on the Kratos Main Board. It is the white 9-pin header marked JP1, at the end the yellow cable comes out of.

[![The original front panel board with the 9-pin connector and yellow cable](images/mainboard/step2.png)](images/mainboard/step2.png)

**Do not try to free it by pulling on the cable.** The wires are held in slot contacts, so pulling will drag the wires out of the connector housing instead of lifting the connector off the board.

Instead:

1. Apply flux to all nine joints on the underside of the board, and add a little fresh solder to each one - mixing new solder into the old joints helps them melt more evenly
2. Heat the solder joints from the underside of the board
3. As the solder softens, use a blade or the tip of a pair of side cutters to gently lever the connector body up from underneath
4. Work along the pins a little at a time, easing the connector up gradually rather than trying to lift it in one go

## Step 3: Solder the Connector to the Kratos Main Board

The salvaged connector fits the matching footprint on the Kratos Main Board.

[![The Kratos Main Board showing the 9-pin connector footprint](images/mainboard/step3.jpg)](images/mainboard/step3.jpg)

1. Clear any leftover solder from the connector pins with braid so they drop cleanly into the holes
2. Flux the pads on the Kratos board
3. Seat the connector fully so it sits flush against the board and check the orientation matches the footprint
4. Solder all nine pins, aiming for shiny, cone-shaped joints that fill the hole

## Step 4: Clean Up and Check

Flux residue is sticky and can be mildly corrosive, so clean it off once you are done. Brush the joints with isopropyl alcohol (99% works best) and a soft brush, wipe away the residue, and let the board dry fully before it goes anywhere near power.

With the connector fitted and cleaned up, the Kratos Main Board should look like this and is ready to install:

[![The Kratos Main Board with the 9-pin connector fitted](images/mainboard/step4a.jpg)](images/mainboard/step4a.jpg)

[![Another view of the assembled Kratos Main Board](images/mainboard/step4b.jpg)](images/mainboard/step4b.jpg)

## Step 5: Prepare the SMBus Harness

The SMBus harness is the single-ended 3-wire JST lead - a connector on one end, bare wires on the other. It plugs into the header marked **INPUT**, and its two SMBus wires are soldered to the console's SMBus later in [Part 7](hardware-7-connecting-kratos-to-the-smbus.md).

Kratos is powered from the controller ports in this install, wired up in [Part 4](hardware-4-preparing-the-controller-ports.md), so the harness only needs its two SMBus wires. That leaves the third one, on the 5V pin, with nothing to do, and it is worth taking off rather than leaving a bare end loose inside the console.

The **INPUT** header is SCL, SDA, then 5V, so the 5V wire is the one on the end - check it against the [Pinout Reference](reference-pinout.md) first. To take it out, lift the small retention tab inside the connector housing with a fine pick and slide the contact out. If you would rather not disturb the housing, cut the wire off flush at the connector and insulate the stub instead.

## Step 6: Connect the Cables and Clip the Board In

The two Controller Board Connection Cables are the 3-wire JST leads. Plug one into the header marked **RGB1** and the other into **RGB2** - the connectors are keyed, so they only go in one way. Route each cable towards the controller port it will feed.

Plug the SMBus harness into **INPUT**, then clip the Kratos Main Board into the front panel using the same clips that held the original board.

[![The Kratos Main Board clipped into the front panel with the RGB cables connected](images/mainboard/step5.jpg)](images/mainboard/step5.jpg)

---

[← Previous: Part 4 - Preparing the Controller Ports](hardware-4-preparing-the-controller-ports.md) | [Next: Part 6 - Refitting the Front Panel →](hardware-6-refitting-the-front-panel.md)
