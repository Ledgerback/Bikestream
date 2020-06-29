# Proof of Concept

Our first Proof-of-Concept (PoC) for the Bikestream project is the creation of an electric bicycle (e-bike) that can store, manipulate and transmit e-bike and geolocation data in real-time to an external system where the owner has control over how the data is accessed.

## Definitions

|Term| Definition|
|----|-----------|
|Onframe Hardware| Computer hardware we needed to attach to the bicycle frame|
| RPi 3+| Raspberry Pi 3+ |

## Physical and Hardware Materials

- Bicycle
  - Cycleforce Mountain Bike
    - 26" rim
- e-bike Parts
  - Cycle Analyst 3
    - USB-to-TTL adapter
  - Right twist throttle
  - e-brakes (pair)
  - Predator 48V battery
- Single Board Computer
  - Raspberry Pi 3+ (RPi 3+)
  - Keyboard
  - Monitor
- Smartphone 
  - Nexus 5x
- Miscellaneous
  - Zip Ties
  - Tire pump
  - Set of Allen Keys
  - Pliers
## Software Materials

- Streamr Commandline Interface (CLI)
- Python program for data storage and manipulation
- Commandline command to start the Python program and Streamr CLI at start-up
- Python Libraries:
  - Pandas
  - [Pynmea2](https://github.com/Knio/pynmea2)
  - JSON
  - Serial
  - PyPi
- Bluetooth2GPS 
  - Android application to stream GPS data from smartphone to RPi 3+

## e-bike conversion

The driving factor behind our choice of materials was the cost of building the prototype e-bike. We decided not to purchase a pre-assembled e-bike (with parts we considered desirable) because the cost was too high, the warranty would be voided as soon we started tinkering with the internal parts, and we needed to make sure that we had a baseline understanding of converting traditional bicycles to e-bikes for ourselves.

We purchased our e-bike conversion parts from EM3ev and from LunaCycles based on comment threads found on eBike- and cycling-related subreddits on Reddit and threads on endlesssphere, a bicycle forum. Our review of the comment threads led us to believe that we could purchase quality parts for an e-bike conversion from both sellers. 


###### This Section is currently being edited

```
We purchased the following parts based on EM3ev's e-bike conversion kit:

Product

Quantity

Price

Upgrade Mac Ebike Kit with 48/52V Battery Option (~1500W Max) (#BUNDLE_MAC-48V30A)

1

$853.00

Throttle Type - Right Half Twist (#WUX-HI_R_HT)

1

Subtotal: $10.00

Ebrake Type - Mechanical Ebrakes Lever (pair) (#WUX_EBK_PR)

1

Subtotal: $6.00

Mac Motor & Axle Type - Standard Rear, Freewheel, 135mm (#MAC_R135_FW)

1

Subtotal: $270.00

Mac Motor Wind - 8T 50KPH (30 MPH) at 48V/26" Rim (#MAC-8T-WINDING)

1

Subtotal: $0.00

Rim Type For Wheel Build (#AL_26_DH21D)

·         Rim Type:

26" Alex DH21 Disc

1

Subtotal: $27.00

Spoke Type For Wheel Build (#SAPIM_BL_SET)

·         Spoke Type:

13G Sapim Black (Please ensure you select a rim)

1

Subtotal: $25.00

Cycle Analyst Ebike Computer, CA-DPS Vers 2.4 (#CA2-DPS)

1

Subtotal: $100.00

Cycle Analyst Programme Cable (#CA-USB)

1

Subtotal: $18.00

Freewheel Type - 7sp Shimano (#SHIMANO_7SP)

1

Subtotal: $12.00

DNP Extractor Tool (#DNP-TOOL)

1

Subtotal: $6.00

48V (13S4P) Preditor L Options - 48V 11.8Ah Preditor (13S4P-30Q) High-Power (#13S4P-PRED_L-30Q)

1

Subtotal: $349.00

54.6V Charger (for 13S, 48V NCM/NCA Battery) - 54.6V 2A Plastic Case Charger (#54.6V2A_CHRG)

1

Subtotal: $30.00

AC Plug for Charger - USA (#USA_PLUG)

1

Subtotal: $0.00

Subtotal:

$853.00

Shipping:

$146.30 via USA Battery

Payment method:

PayPal

Total:

$999.30

9 FET IRFB3077 (30A) Infineon Sensored Controller: Fully Programmable For Motors With Hall Sensors (#BUNDLE-INFINEON-9FET-3077)

1

$97.50

Controller Battery Connections - Anderson 45PP (incl. battery side) (#BATT-ANDERSON_PP+)

1

Subtotal: $3.50

Phase Wire Connections - Anderson 45PP (incl. motor connections) (#PHASE-ANDERSON_PP+)

1

Subtotal: $5.00

Bar-Mounted Power Switch: For Infineon Controllers (#INFINEON-POWER-SWITCH)

1

Subtotal: $3.00

EB3 Infineon Program Lead: For Programming EB3 Infineon Controllers (Software included) - Do Not Connect To the CA3 PAS/Torque Connector (#EB3PRGM)

1

Subtotal: $10.00

DNP Extractor Tool (#DNP-TOOL)

1

$0.00

Product	Quantity	Price
CA3-DPS, Cycle Analyst Ebike Computer	1	$130.00
Ebrake Levers (mechanical cable-pull)	1	$12.00
Ebrake Type - Mechanical Ebrakes Lever (pair)	1	Subtotal: $10.00
Ebrake Connector Type - To CA3 (0.3m or as specified)	1	Subtotal: $2.00
Right Half Twist Throttle: The Premium Right Half Twist Throttle	1	$12.00
Throttle Type - Right Half Twist	1	Subtotal: $10.00
Throttle Connector Type - To CA3 (0.3m)	1	Subtotal: $2.00
Custom Non-Battery Item - Info to be added here
CA3 above to be compatible with the temperature sensor fitted to the Mac motor from Order 10053:
Standard Rear Mac Motor was purchased in March, 2019

1	$0.00
Subtotal:	$154.00
Shipping:	$19.17 via DHL/UPS USA (~3 days shipping time)
Payment method:	PayPal
Total:	$173.17

Luna Cycles Triangle Battery Bag Velcro
BAG-TRI-VELCRO	1	$24.95 USD	$24.95 USD
Subtotal:	$24.95 USD
Shipping:	$5.00 USD
Grand Total:	$29.95 USD


Our total cost was:

A good amount of our costs arose from having parts that did not have the proper connection and realizing we needed more data than would be avilabale with our setup based on the CA2.

Now, if we had gone about this in a better, more informed manner, as we know now at the end of the PoC, we believe our total costs would be (especially if we used LunaCycle to avoid high shipping costs):


However, we did not need to use the L-space battery bag holder from LunaCycle because we could attach the battery to the frame of the CycleForce BTM. 

```


Once we had purchased all of the parts in the first round, we started converting the bicycle into an e-bike. We began the conversion of the bicycle in early 2020 and did not finish until April 2020. Our purchase of the CycleForce MTB came as parts, which reuqired us to assemble the parts together to form a complete bike. While assembling the parts for the Cycleforce MTB, we also started attaching the e-bike parts to the frame. After attaching the e-bike parts to the CycleForce MTB, we attached the RPi 3+ to the frame of the e-bike (and thus, turning our e-bike into a databike). 

After April 2020, we mostly conducted maintenance on the e-bike, configured the Infinieon controller and CA3, and tested the e-bike to ensure it worked as expected.  The e-bike conversion took approximately 2 - 3 weeks of work to complete because of conflicting schedules, the need for maintenance on the e-bike, and the realization that we needed extra parts (mostly arising from switching from the CA2 to CA3) during the conversion. 

### e-bike Range

The range of the e-bike is signaifcnatly affected by your cycling habits and your road conditions (e.g., elevation). Most important thing to consider is your travelling speed and how that affects your battery usage. 

### e-bike simulations

We conducted ~2 -3 simulations of our converted e-bike on the [Grin Tech Ebike Simulator](http://www.ebikes.ca/tools/simulator.html).

We recommend simulating the performance of your expected converted e-bike before purchasing your parts individually or as part of an e-bike conversion kit. 

## Operation of DBZ-001

The DBZ-001 is very easy to operate from the perspective of a cyclist.

### Manual

1. Connect the MicroUSB-to-USB cord from the RPi 3+'s power port to the external USB port on the battery.
2. Connect the USB-to-TTL adapter from the CA3 to one of the RPi 3+'s USB ports. 
3. Turn on the battery by holding on to the power button for ~3 - 5 seconds (there should be flash of green light from the LED indicator)
4. Switch on the operating switch for the e-bike parts by pushing the switch forward and up.
5. Start the Bluetooth2GPS mobile application on the smartphone and ensure the smartphone's bluetooth connection is on. 
6. Ensure the RPi 3+ is powered on by determining whether the power light is flashing green.
7. Wait ~2 - 5 minutes for the RPi 3+ to finishing booting up and if the RPi 3+ shows up on the Bluetooth2GPS home screen on the smartphone, then the RPi 3+ is working properly. 
8. Now you can operate the databike as you would normally for an e-bike or traditional bicycle.

### Checklist

1. If the RPi 3+ is not powering on, try removing and reattaching the MicroUSB-to-USB cord from the RPi 3+'s power port to the external USB port on the battery until the power light is flashing green. 
2. If the RPi 3+ is not showing up on the Bluetooth2GPS home screen on the smartphone, try restarting the RPi 3+ by following 1. 
3. Reset trip data on the CA3 before you begin a new trip.
4. Check the battery life before embarking on your trip. 
5. Conduct a short trip (less then 30 feet) to check on the operation of the twist throttle and the e-brakes. If the throttle is unresponsive, you may need to adjust your Throttle In (ThI) or Throttle Out (ThO) settings. If the e-brakes are not cutting off the motor, you may need to adjust your e-brake settings. Any issues regarding the throttle or e-brakes should be visible on the home screeen of the CA3. If the throttle and e-brakes are shown to be working properly on the CA3 home screen but the motor is not turning, you may need to adjust the settings on the Infinieon controller or the CA3's settings.

## Real-time, User-controlled Data Streaming

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

### Streamr 

Streamr is a service built on top of the Ethereum blockchain for real-time streaming of data, prmarily from Internt-of-Things (IoT) devices.

We created a data stream and marketplace product on Streamr.

Our data stream is the Databike Pilot Community Stream, and can be found here:

- [Databike Pilot Community Stream](https://streamr.network/marketplace/products/ebc580eb3eee4052b332fe558fa85cc8c6c75d319959489f8fed905d19128bdf/streamPreview/LzP4JBc9RoWdCsmDediy2A)
  - Stream ID: LzP4JBc9RoWdCsmDediy2A

Our marketplace product is the Mobility Cyclist Association, and can be found here:

- [Mobility Data Cyclist Association](https://streamr.network/marketplace/products/ebc580eb3eee4052b332fe558fa85cc8c6c75d319959489f8fed905d19128bdf)

We decided to use Streamr's CLI to connect to our stream because we needed to stream data from the RPi 3+ to the stream in headless mode (i.e., without a monitor nor a keyboard), and we needed the stream to start as soon as the RPi 3+ finished booting up.

### Ocean Protocol 

## Setting up the Onframe Hardware

The Onframe Hardware we needed to set up included the:

- RPi 3+
- CA3
- Infinieon controller

The CA3 connected to the RPi 3+ via a USB-to-TTL adapter.

The Infineon controller connected to the CA3 via a direct plug from the Microcontroller to the CA3.

The Infineon controller connected to all the other e-bike parts via a direct plug.

The RPi 3+ received direct power from the battery's USB port. 

Our configuration for the CA3 is as follows:

Our configuration for the Microcontroller is as follows:

The only configuration change we made to the RPi 3+ is adding the commandline program for the Python program to pipe output to the Streamr CLI program.

## Types of Data
There are two types of data recorded with the PoC:

- e-bike internal information from sensors that is collected by the CA3
- Nexus 5x GPS sensor information

### CA3 Data

The CA3 collects and streams sensor information from the e-bike. 

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

### Nexus 5x Data

The GPS data streamed from the Nexus 5x via the Bluetooth2GPS Android application are [National Marine Electronics Association (NMEA) sentences](https://www.gpsinformation.org/dale/nmea.htm#nmea). For more information, refer to the NMEA standard. 

The first word describes the data type (starting with a *$*), and the rest of the sentence is information that is interpreted based on the data type. 

The following NMEA data types are streamed from the Nexus 5x via the Bluetooth2GPS app:

- GPGGA
- GPRMC
- GPGSA
- GPGSV
- GPRMB
- HCHDG


### Need for Data Manipulation

The CA3's serial stream provides data in a tab-delimited format while the Nexus 5x's serial stream provides data in a comma-separated value format. 

To publish with the Streamr CLI, the data must be in a JavaScript Object Notation (JSON) format. 

To convert the CA3 data and Nexus 5x data into JSON, a Python program was developed to access the serial streams from the CA3 and the Nexus 5x, convert the streams into one single JSON file, and push the JSON-formatted file to the console where it would be piped to the Streamr CLI for publishing data. 

### Current Data Specification

Our current data specification combines the CA3 data with the GPS data into one unified JSON format. 

The specification is as follows:



## Prototype Fleet

Our prototype for this PoC is the [DBZ-001](Documents/Prototype_Fleet/Databike_Zeta_001_2020_0605.jpg)




# Trials

We conducted two preliminary trials to determine if our configuration was appropriate enough to operate the DBZ-001, and to test the bounds of operating the DBZ-001.


# Status

We have proved our PoC by building Databike Zeta 001 (DBZ-001), a bicycle that was converted into an electric bicycle (e-bike) with e-bike parts and strapped with two on-board computers, a CA3 (bike computer) and a RPi 3+ (single board computer), and the use of a free-hand Nexus 5x smartphone. The RPi 3+ stores and manipulates information from two sources:

1. The CA3 that records the internal information of the DBZ-001's sensors; and 
2. The Nexus 5x that records the GPS data from the Nexus 5x's GPS sensor.

The stored data is manipulated into a JSON format and then piped to the Streamr CLI program for publishing data to a stream. 

The commandline program for the Python program and Streamr CLI program is initiated during boot-up on the RPi 3+.

Once the commandline program is running, the data will be transmitted to the stream on Streamr.

# Improvement Options

A laundry list of tasks to improve the PoC. 

- Create an analytics dashboard on Streamr
- Use the Python library for Streamr
- Optimize the Python programs
- Find more mitigation strategies for performance issues
- Adding another RPi 3+ for data storage and manipulation

# Additional options we can test with our current setup

- Connecting the CA3 to the Nexus 5x and storing, processing and transmitting data to the stream on Streamr
- Recording and sharing acceloremeter sensor data from the Nexus 5x with the RPi 3+ to obtain vibration data from the road surface 
- Creating multiple streams for the DBZ-001 for each type of serial data or sensor.
- Connecting the CA3 to the Nexus 5x to record GPS output as NMEA strings and storing the information on the RPi 3+.
  - i.e., trying out the more experimental firmwares of the CA3.
 - Recording acceloremeter sensor data from the Nexus 5x
 - Assessing more data and standards related to e-bikes and electric vehicles in general
 - Controlling the CA3 or microcontroller with the RPi 3+

# Potential Expansion of PoC

The PoC was proven for e-bike data and geolocation data, but we can also expand our data collection efforts by adding the following sensors:

- Cadence Sensor: To collect pedaling rate data (i.e., the human power being applied)
- Heart Rate Monitor: To collect heart rate data (e.g., beats per minute)
- Temperature Sensor: To collect temperature-related data from the e-bike parts
- Torque Sensor: To collect pedaling rate data (i.e., the human power being applied)
- Acceloremeter Sensor: To collect vibration data from the road surface (the sensor would be attached to the RPi 3+)

If we add a torque sensor, we can also test out having a pedal assist e-bike ("pedelec") and a manual throttle e-bike.

We can expand our specification of data by adding the Open Mobility Foundation's (OMF) data specification or the General BikeSharing Feed (GBFS) data specification to our stream. 

Additionally, we can test out a QR code scanner function with the RPi 3+ via a touch screen. This application would be for testing out a dockless bikesharing solution. 

## New PoCs to consider
Two new PoCs we have considered after proving our databike PoC are:

- Solar-powered databikes; and
- Autonomous databikes.
