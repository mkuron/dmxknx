This is a gateway between DMX and KNX to allow control of KNX lighting systems using DMX light controllers.

Introduction
------------

**KNX** (also called **EIB**) is a building control bus system commonly used in large buildings.
It might be used to control lights, blinds or heating systems.

**DMX** is used to control stage lighting and special effects, and is the industry standard worldwide for this purpose.

In a theater or other concert venue, it's very useful to be able to control the house lights from the same light board as your stage lights.
If you're planning the electrical installation in a new building, you could just buy dimmers for the house lights which can be controlled via both KNX and DMX (for example, by using dimmers that are addressed in an analog fashion with 0-10 volt and using 0-10 volt demuxers for both protocols).

If you're retrofitting DMX control into a KNX building, things get a bit more difficult:
KNX is rather narrowband (9600 bits per second) and thus cannot dim as smoothly as DMX (which sends all its 512 channels 40 times per second).
So any conversion between DMX and KNX needs to make sure that not more than ~50 messages are sent to the KNX bus.

Requirements
------------
- USB to DMX interface with DMX input. We are using the [Digital Enlightenment](http://www.digital-enlightenment.de/usbdmx.htm)/[FX5](http://www.fx5.de) interface.
- USB to KNX interface. We are using the [Busware TUL](http://busware.de/tiki-index.php?page=TUL)
- Raspberry Pi
- [FHEM](http://fhem.de/fhem.html)
- [usbdmx](https://github.com/fx5/usbdmx) Driver

Installation
------------
- Hook up the interfaces to your DMX and KNX wiring and connect them to the Raspberry Pi. 
- Install the FHEM debian package.
- [Configure FHEM for KNX](http://www.fhemwiki.de/wiki/EIB_/_KNX) and have it auto-discover all your KNX lights by turning each of them on and off using the light switch. Then give a descriptive name to each KNX light and set their *model* attribute to *percent* if they dim or leave it if they don't.
- Compile usbdmx, including the Python interface.
- Map FHEM devices to DMX channels in config.py
- Start saallicht.py
