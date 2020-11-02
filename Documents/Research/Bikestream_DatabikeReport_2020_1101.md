# Databike report

## Outline
1. Parts bought and cost (also mention where people can do simulations)
2. Converting bike to ebike to databike (just mention parts changed and their placement (if needed), and then how SBC is connected to CA3 to act as a datalogger and where it is placed on the bike) (also expected time of conversion with 2 people with basic parts)
3. Databike configuration (describe RPi 3 and configuration, CA3 configuration and controller configuration)
4. Data collection (how data is shared between phone and RPi and between RPi and CA3), specification (how CA3 data and GPS data is structured together into JSON), and sharing (Python program and Streamr)
5. Operation of bike (turning on parts and getting them to work together)
6. Mention trials of just actual uses
7. Additional sensors that can be added
8. Issues

## Definitions

|Term| Definition|
|----|-----------|
|Onframe Hardware| Computer hardware we needed to attach to the bicycle frame|
| RPi-3B+| Raspberry Pi Model 3 B+ |
| Smartphone | Nexus 5x |
|CA3| Cycle Analyst 3|
| Controller | Infineon Controller |
| e-bike | Electric bicycle |
| Databike | An e-bike with a SBC that can collect, store, manipulate, and share data |
| SBC | Single Board Computer |

## Materials 

### Physical and Hardware Materials

- Bicycle
  - Cycleforce Mountain Bike
    - 26" rim
- e-bike Parts
  - Cycle Analyst 3
    - USB-to-TTL adapter
  - Right twist throttle
  - e-brakes (pair)
  - Predator 48V battery
  - Infineon Controller
  - Mac Motor 
	  - 26" rim
- Single Board Computer
  - Raspberry Pi 3+ (RPi-3B+)
  - Keyboard
  - Monitor
- Smartphone 
  - Nexus 5x (Android)
- Miscellaneous
  - Zip Ties
  - Tire pump
  - Set of Allen Keys
  - Pliers

### Software Materials

- Streamr Commandline Interface (CLI)
- Python program for data collection, storage,  manipulation and sharing
- Commandline command to start the Python program and Streamr CLI at start-up
- Python Libraries:
  - Pandas
  - [Pynmea2](https://github.com/Knio/pynmea2)
  - JSON
  - Serial
  - PyPi
- Bluetooth2GPS 
  - Android application to stream GPS data from Smartphone to RPi-3B+


## Parts Bought and Costs

Refer to [Bikestream Expenses Sheet](https://docs.google.com/spreadsheets/d/17jbUsjJREUYRPEIt2wY_w-89ypXyV2_iFkHinWlip3c/edit?usp=sharing)

For simulations of builds, please refer to Grin Tech's e-bike simulator. 

## Build 

### Materials
The driving factor behind our choice of materials was the cost of building the prototype e-bike. We decided not to purchase a pre-assembled e-bike (with parts we considered desirable) because the cost was too high, the warranty would be voided as soon we started tinkering with the internal parts, and we needed to make sure that we had a baseline understanding of converting traditional bicycles to e-bikes for ourselves.

We purchased our e-bike conversion parts from EM3ev and Luna Cycles (only a battery bag which we eventually did not need to use) based on comment threads found on eBike- and cycling-related subreddits on Reddit and threads on Endlesssphere, a bicycle-enthusiast forum. Our review of the comment threads led us to believe that we could purchase quality parts for an e-bike conversion from EM3ev (We did not find out about Luna Cycles until we had already purchased the e-bike conversion kit T_T).

### Bike to eBike

The bicycle we used for the e-bike conversion was the Cycle Force Rigid Mountain Bike, (26 in wheels, 18 in frame, Men's Bike, Blue) (* CycleForce-MTB*), purchased from Walmart. 

We chose a cheap bicycle because we wanted to mofidy the bike as much as possibel without worrying about a warranty and if we made any mistakes or had any mishaps, we would not be in tto much trouble because the cost of the bike would not dramatically hurt our ability to complete the build. 

Concerning the conversion, I will only mention the parts we modified on the bicycle. 

#### Conversion

We made the following modifications to the CycleForce-MTB:

1. We replaced the rear tire with a new rim of the same size which included an opening for a motor. The tire from the original rear tire was removed and placed on the new rim
2. We replaced the brakes with e-brakes 
3. We placed the battery on the bike by mounting it in the L-shape (in reverse) through the bolt-ons
4. We placed the Infineon Controller ("Contoller") on the frame, right in front of the seat handle (and subsequently connected all the parts to the controller in this area with zip-ties)
5. We replaced the tube on the right handlebar with a twist throttle and placed an on/off switch on the right handlebar
6. We placed the Cycle Analyst 3 (CA3) on the handlebar 

### eBike to databike

Converting from an e-bike to a databike was a very simple procedure. 

To convert the e-bike to a databike, we palced a Raspberry Pi 3 B+ (RPi-3B+) at the stem of the e-bike, secured with zip-ties, and powered by the battery via a USB-to-MicroUSB cord. This is a very similar procedure to adding the datalogger that accompanies the CA3. 

### Timeline

Once we had purchased all of the parts in the first round, we started converting the bicycle into an e-bike. We began the conversion of the bicycle in early 2020 and did not finish until April 2020. Our purchase of the CycleForce-MTB came unassembled (i.e., as parts), which reuqired us to assemble the parts together to form a complete bike. While assembling the parts for the Cycleforce-MTB, we also started attaching the e-bike parts to the frame. After attaching the e-bike parts to the CycleForce-MTB, we attached the RPi-3B+ to the frame of the e-bike (and thus, turning our e-bike into a databike).

After April 2020, we mostly conducted maintenance on the e-bike, configured the Infinieon Controller and CA3, configured the RPi-3B+ to work with Streamr, the Smartphone and CA3, and tested the e-bike to ensure it worked as expected. The e-bike conversion took approximately 2 - 3 weeks of work to complete because of conflicting schedules, the need for maintenance on the CycleForce-MTB, and the realization that we needed extra parts (mostly arising from switching from the CA2 to CA3) to complete the conversion and to increase the diversity of data.

For an expected timeframe for the conversion (including assembling the bicycle), I would suggest reserving 1 - 2 weeks worth of time. 

## Databike configuration (describe RPi 3 and configuration, CA3 configuration and controller configuration)

The parts that we needed to  configure were the:

1. RPi-3B+, 
2. Controller, and
3. CA3.

We needed to match the configurations of the CA3 and Controller so that the databike would be operational. 

You can find our configurations for the CA3 and Controller below (both are in images).

We modified the CA3 configuration via the USB-to-TTL cord provided with the CA3 and the app provided by Grin Tech. 

Modifying the Controller was problematic because we could not necessarily find the app we needed to modify its settings. 

We had to look through a couple threads on Endlesssphere before finally finding an application to modify the Controller's configuration.

We set up the RPi-3B+ with basic settings (RaspbianOS as the operating system (OS)). 

We needed to conigure the RPi-3B+ to handle the following tasks:

1. Reading (i.e., collecting) data from the CA3 (sensor data) and Smartphone (geolocation data)
2. Processing the data in real-time in headless-mode (i.e., without a monitor or keyboard) with a Python program ("Program"), and
3. Sharing the data via Streamr.

To do so, we modified the RPi-3B+ configuation so that at start-up, it would run our Program and stream our data to our Streamr stream.

## Data collection (how data is shared between phone and RPi and between RPi and CA3), specification (how CA3 data and GPS data is structured together into JSON), and sharing (Python program and Streamr)

### RPi-3B+

We used the RPi-3B+ to be our datalogger rather than purchasing the datalogger from Grin Tech to connect to the CA3 because it was cheaper and we can more easily program the RPi-3B+ to process data and for other functions if needed.

### Connecting CA3 and Smartphone to RPi-3B+
The RPi-3B+ collects data from two sources:

1. Nexus 5x ("Smartphone")
2. CA3

The Smartphone provides geolocation data via it's internal GPS sensor while the CA3 provides sensor data from the electrical bike components.

The RPi-3B+ collects GPS sensor data from the Smartphone via Bluetooth2GPS (offered for free and premium; we chose the free version to trial the app and to save money), an Android application for sharing GPS sensor data from an Andorid device (here being the Smartphone) with another device via a Bluetooth connection. 

We followed the directions provided in the Bluetooth2GPS app to connect the Smartphone to the RPi-3B+ (we also added the connection via bluetooth into the configuration for start-up), which ulitmately ended up in a one-line command in the commandline to create the connection (`if you are having issues connecting, make sure to check all your connections`) between the RPi-3B+ (as the master) and the Smartphone (as the SPP SLAVE).

For the CA3, we connected the CA3 to the RPi-3B+ via the USB-to-TTL cord and read in the connection as a USBserial connection. 

Both sources are recognized as serial streams.

To capture the data in the streams, we opened a connection as a serial stream (a connection for each stream) with the PySerial library. 

### Data Specification
#### CA3 Data Format

The CA3 collects the following information:

- Volts, 
- Speed,
- Amps, 
- Amp-hours, 
- %regen, 
- Watt-hours/km 
- Distance
- Human watts
- PAS Rotations per minute (RPM)
- PAS Torque Newton meters
- Throttle In voltage
- Throttle Out voltage
- Temperature degrees in Celsius
- Auxiliary Analog
- Auxiliary Digital
- Flags
  - 1/2/3= Preset #
  - X= Throttle Fault
  - B= Brake
  - A= Amp Limiting
  - W= Watt Limiting
  - T= Temp Limiting
  - V= Low Volts Limiting
  - S= Speed Limiting
  - s= Low Speed Limiting

Most of the data is streamed as a string (but there are certain bytes you may have to worry about because they cannot be interpeted in UTF-8).

The flags are also a great feature for getting some insight into the specific actions cyclists are taking during their trip (e.g., B for brake informs us when a cyclist is breaking or slowing down).

#### Smartphone Data format

The GPS data streamed from the Smartphone via the Bluetooth2GPS Android app are [National Marine Electronics Association (NMEA) sentences](https://www.gpsinformation.org/dale/nmea.htm#nmea). NMEA sentences are a standard data format for GPS data. For more information, please refer to the NMEA 0183 protocol. 

The first word describes the data type (starting with a *$*), and the rest of the sentence is information that is interpreted based on the data type. 

[Sample](https://www.gpsinformation.org/dale/nmea.htm#RMC):

```
RMC - NMEA has its own version of essential gps pvt (position, velocity, time) data. It is called RMC, The Recommended Minimum, which will look similar to:

$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A

Where:
     RMC          Recommended Minimum sentence C
     123519       Fix taken at 12:35:19 UTC
     A            Status A=active or V=Void.
     4807.038,N   Latitude 48 deg 07.038' N
     01131.000,E  Longitude 11 deg 31.000' E
     022.4        Speed over the ground in knots
     084.4        Track angle in degrees True
     230394       Date - 23rd of March 1994
     003.1,W      Magnetic Variation
     *6A          The checksum data, always begins with *
```

The following NMEA data types are streamed from the Nexus 5x via the Bluetooth2GPS app:

- GLGSV
- HCHDG
- HCHDT
- GPMDA
- IIMMB
- YXXDR
- GPRMC
- GPGGA
- GNGSA
- GPGSV


The essential data for geolocation is the latitude and longitude, which can easily be found through the GPRMC sentence. 

The NMEA sentences are streamed as strings (data type).

#### Initial File Formats

Initially, the CA3's serial stream provides data in  a tab-delimited value (TSV) format while the Nexus 5x's serial stream provides data in a comma-separated value (CSV) format. 

Because neither stream is in the JavaScript Object Notation (JSON) format needed to share with our stream on Streamr, there was a need to develop the Program to manipulate the data into JSON.

`JSON notation is often a dictionary of key-value pairs in the following syntax: {key: value}`

#### Final File Formats

To process the serial streams, we utilized the Pandas library. 

`We also experimented with the PyNMEA2 library to parse NMEA sentences into descriptive strings but we kept having issues with certain bytes from the stream causing the Program to fail.`

After the Program processes the the data into Pandas dataframes, the dataframes are combined and exported as JSON. 

### Real-time Streaming with Web3 
We desired to use Web3 technologies because of the promise of data sovereigny that oculd be provided from blockchain-based services and to use the benefits of blockchain to ensure that data could only be accessed on the user's term or with the user's permission. 

The characteristics of blockchain we desired for real-time data streaming were: 

We prmarily focused on two Web3 technology services built on the Ethereum blockchain for real-time data streaming:

1. Streamr, and
2. Ocean Protocol.

We settled on Streamr because the project is aimed more at real-time data streaming and it was the easiest service to set up. Additionally, Streamr also provided the following features we found attractive:

- Quick setup of a marketplace for related data
  - Multiple streams can be included into one product
  - The marketplace can be controlled by one user or organization
- Ability to control accessibility of data
- Multitple options for validating data
- It's own network for transporting data
- Aility to make data accesible public or private
- Ability to make data analytics tools on Streamr Core

#### Streamr 

Streamr is a service built on top of the Ethereum blockchain for real-time streaming of data, with applications involving Internet-of-Things (IoT) devices.

We created a data stream and marketplace product on Streamr.

Our data stream is the [Databike Pilot Community Stream](https://streamr.network/marketplace/products/ebc580eb3eee4052b332fe558fa85cc8c6c75d319959489f8fed905d19128bdf/streamPreview/LzP4JBc9RoWdCsmDediy2A), and can be found here:

- [Databike Pilot Community Stream](https://streamr.network/marketplace/products/ebc580eb3eee4052b332fe558fa85cc8c6c75d319959489f8fed905d19128bdf/streamPreview/LzP4JBc9RoWdCsmDediy2A)
  - Stream ID: LzP4JBc9RoWdCsmDediy2A

The description for our stream is the following:

> Sensor and Geolocation data from electric-assisted bicycles that are run by a mobility data cooperative


Our data specification for the Databike Pilot Community Stream is a JSON that combines the sensor data and geolocation data.

The data itself is specified in the following formats (with the field as the key, and the value as the field type):

- GLGSV:  List
- HCHDG: List
- HCHDT: List
- GPMDA: List
- IIMMB: List
- YXXDR: List
- GPRMC: List
- GPGGA: List
- GNGSA: List
- GPGSV: List
- Ah: String
- V: String
- A: String
- S: String
- D: String
- Deg: String
- RPM: String
- HW: String
- Nm: String
- ThI: String
- ThO: String
- AuxA: String
- AuxD: String
- Flgs: String

The field types as defined on [Streamr](https://streamr.network/docs/streams/intro-to-streams):

> **String** is a sequence of zero or more alphabetical characters.
> **List** is an ordered collection of zero or more elements. List is equivilent to an array.

Though, field types do not need to be known beforehand (and this also helped us out during testing and when the Program outputs the data in the wrong format).

Additionally, any data streamed to our stream is timestamped (Additionally, this is also accomplished in the NMEA sentences, e.g., in the GPRMC sentence). 

We setup our stream with basic security for testing purposes. Thus, we might change our secueirty setting (and also needed verification or proof of data) as the project progresses and we become more knowledgeable about Streamr.

Our marketplace product is the [Mobility Data Cyclist Association](https://streamr.network/marketplace/products/ebc580eb3eee4052b332fe558fa85cc8c6c75d319959489f8fed905d19128bdf), and can be found here:

- [Mobility Data Cyclist Association](https://streamr.network/marketplace/products/ebc580eb3eee4052b332fe558fa85cc8c6c75d319959489f8fed905d19128bdf)

The description for the Mobility Data Cyclist Association is as follows:


> This cyclist association is created pursuant to the Databike Pilot Project, a research project investigating how to incentivize the creation and offering of micro-mobility data from electric-assisted bicycles (e-bikes) via collective-owned organization models and Web 3 technologies.

The product is in the transpotration category. 

The basic terms and conditions applied to using our stream are the **Basic terms**: " Redistribution, commercial use, reselling & storage are not permitted."

In the Mobility Data Cyclist Association product, anyone can add their stream to our product so that we can pool our data together (on Streamr, this is often referred to as a Data Union (though we would like this to officially be a Data Cooperative)) and offer it to third parties for remuneration (i.e., we can monetize our data together and the more data we have (i.e., movign towards Big Data), the more valuable the data pool becomes. Thus, the datapool can serve as datasets to be used in data analytics and machine learning (ML) related applications. 

We decided to use Streamr's CLI to connect to our stream because we needed to stream data from the RPi 3+ to the stream in headless mode (i.e., without a monitor nor a keyboard), and we needed the stream to start as soon as the RPi 3+ finished booting up.

Unfortunately, we did not have enough time to develop a [canvas](https://streamr.network/docs/canvases/intro-to-canvases) and a [dashboard](https://streamr.network/docs/dashboards) as of writing. 

#### Streamr CLI

We decided to use Streamr's CLI to connect to our stream because we needed to stream data from the RPi 3+ to the stream in headless mode (i.e., without a monitor nor a keyboard), and we needed the Program to pipe its output from stdout to the stream at start-up. 


## Operating the Databike

### Prototype
We have named our PoC the Databike Zeta 001 (DBZ-001). 

We have found that the DBZ-001 is very easy to operate from the perspective of a cyclist.

### Manual

1. Connect the MicroUSB-to-USB cord from the RPi 3+'s power port to the external USB port on the battery.
2. Connect the USB-to-TTL adapter from the CA3 to one of the RPi 3+'s USB ports. 
3. Turn on the battery by holding on to the power button for ~3 - 5 seconds (there should be flash of green light from the LED indicator)
4. Switch on the on/off switch for the e-bike parts by pushing the switch forward and up.
5. Start the Bluetooth2GPS Android app on the Smartphone and ensure the Smartphone's bluetooth connection is on. 
6. Ensure the RPi-3B+ is powered on by determining whether the power light is flashing green.
7. Turn on the Smartphone's mobile hotspot (only if you do not have a mobile data connection or WiFi connection for the RPi-3B+)
8. Wait ~2 - 5 minutes for the RPi 3+ to finishing booting up and if the RPi 3+ shows up on the Bluetooth2GPS homescreen on the Smartphone, then the RPi-3B+ is connected to the Smartphone and is working properly. 
9. Now you can operate the DBZ-001 as you would normally for an e-bike or traditional bicycle.

### Checklist

1. If the RPi-3B+ is not powering on, try removing and reattaching the MicroUSB-to-USB cord from the RPi-3B+'s power port to the external USB port on the battery until the power light is flashing green. 
2. If the RPi-3B+ is not showing up on the Bluetooth2GPS home screen on the smartphone, try restarting the RPi-3B+ by following Step 1. 
3. Reset trip data on the CA3 before you begin a new trip.
4. Check the battery life before embarking on your trip. 
5. Conduct a short trip (less then 15 feet) to check on the operation of the twist throttle and the e-brakes. If the throttle is unresponsive, you may need to adjust your Throttle In (ThI) or Throttle Out (ThO) settings. If the e-brakes are not cutting off the motor, you may need to adjust your e-brake settings. Any issues regarding the throttle or e-brakes should be visible on the home screeen of the CA3. If the throttle and e-brakes are shown to be working properly on the CA3 home screen but the motor is not turning, you may need to adjust the settings on the Infinieon controller or the CA3's settings.



~~The Program would read in the data from the Smartphone and CA3, combine the data into a JSON format, and send to stdout.



## Issues
These are some of the issues we ran into during operation of the DBZ-001 and also from setting up the RPi-3B+'s connection to the CA3 and the Smartphone.

1. Sometimes the RPI does not stream
2. The processing of days does not get into the right format
3. To much data is obtained; (need to limit amount of info either by size or increasing time intervals)
4. RPi-3B+ has a small amount of Random Access Memory (RAM) so you might need a SBC with more RAM
5. Not truly on-premise because of use of smartphone; need to get sensors directly on the RPi
6. The data streamed from both sources can be inconsistent  and variable (in time and quantity (sometimes would get shorter lines than expected)) or lag for indefinite amounts of time.

## Possible Improvements

- Create an analytics dashboard on Streamr
- Use the Python library for Streamr
- Optimize the Python programs
- Find more mitigation strategies for performance issues
- Adding another RPi-3B+ to the databike for data storage and manipulation
- Add more sensors to collect more varied data:
	- Cadence Sensor: To collect pedaling rate data (i.e., how fast someone is pedaling)
	- Heart Rate Monitor: To collect heart rate data (e.g., beats per minute)
	- Temperature Sensor: To collect temperature-related data from the e-bike parts
	- Torque Sensor: To collect pedaling rate data (i.e., the human power being applied)
	- Acceloremeter Sensor: To collect vibration data from the road surface (the sensor would be attached to the RPi- 3B+)

### Additional options we can test with our current setup

- Connecting the CA3 to the Nexus 5x and storing, processing and transmitting data to the stream on Streamr
- Recording and sharing acceloremeter sensor data from the Nexus 5x with the RPi 3+ to obtain vibration data from the road surface 
- Creating multiple streams for the DBZ-001 for each type of serial data or sensor.
- Connecting the CA3 to the Smartphone to record GPS output as NMEA strings and storing the information on the RPi-3B+.
  - i.e., trying out the more experimental firmwares of the CA3.
- Recording acceloremeter sensor data from the Nexus 5x
- Assessing more data and standards related to e-bikes and electric vehicles in general
- Controlling the CA3 or microcontroller with the RPi 3+
- Adding the Open Mobility Foundation's (OMF) data specification or the General BikeSharing Feed (GBFS) data specification to our stream. 

RPi-3B+

## Future Proofs-of-Concepts 

Two new PoCs we have considered after the databike PoC are:

1. Solar-powered databikes; and
2. Autonomous (i.e., self-cycling) databikes.

--- 

# Sample Datasets

You may find our sample datasets in our [datasets folder](https://github.com/Ledgerback/Bikestream/tree/master/Datasets).

Sample NMEA strings in JSON format

```

$GLGSV,2,2,7,72,21,205,18,77,01,309,00,84,04,123,00,,,,*69
$HCHDG,175.8,,,011.6,E*24
$HCHDT,187.3,T*24
$GPMDA,27.061,I,0.9164,B,,C,,C,,,,C,,T,,M,,N,,M*05
$IIMMB,27.061,I,0.9164,B*41
$YXXDR,P,0.9164,B,Pressure*6C
$GPRMC,052346,A,3608.33915,N,11519.58857,W,000.0,,100420,011.6,E,A*2A
$GPGGA,052346,3608.33915,N,11519.58857,W,1,09,0.9,876.000,M,,M,,*4B
$GNGSA,A,3,10,13,15,16,18,20,21,27,29,,,,1.2,0.9,0.8*28
$GPGSV,3,1,10,10,33,241,19,13,22,052,22,15,45,077,20,16,21,292,17*7D
$GPGSV,3,2,10,18,61,045,14,20,63,267,20,21,67,001,25,27,09,319,14*73
$GPGSV,3,3,10,29,42,150,23,26,20,261,00,,,,,,,,*73
```

Sample CA3 string in JSON format
```

{"Ah":"-0.0114","V":"52.66","A":"0.00","S":"0.00","D":"0.0000","Deg":"0.0","RPM":"0.0","HW":"0","Nm":"0.0","ThI":"0.86","ThO":"1.20","AuxA":"0.00","AuxD":"0.00","Flgs":"1"}

```