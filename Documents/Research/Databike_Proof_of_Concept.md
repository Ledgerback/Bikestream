# Proof of Concept

Our first Proof-of-Concept (PoC) for the Bikestream project is the creation of an electric bicycle (e-bike) that can store, manipulate and transmit e-bike and geolocation data in real-time to an external system where the owner has control over how the data is accessed.

## Definitions

|Term| Definition|
|----|-----------|
|Onframe Hardware| Hardware we needed to attach to the bicycle frame|

## Physical and Hardware Materials

- Bicycle
  - Cycleforce Mountain Bike
    - 26" rim
- e-bike Parts
  - Cycle Analyst 3
  - Right twist throttle
  - e-brakes (pair)
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
  - Pynmea2
  - JSON
  - Serial
- Bluetooth2GPS 
  - Android application to stream GPS data from smartphone to RPi 3+

## Building the e-bike
......

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

Our data stream is the Databike stream and can be found here:

Our marketplace product is the Mobility Cyclist Association and can be found here:

We decided to use Streamr's CLI to connect to our stream because we needed to stream data from the RPi 3+ to the stream in headless mode (i.e., without a monitor nor a keyboard), and we needed the stream to start as soon as the RPi 3+ finished booting up.

### Ocean Protocol 

## Setting up the Onframe Hardware

The Onframe Hardware we needed to set up included the:

- RPi 3+
- CA3
- Microcontroller

The CA3 connected to the RPi 3+ via a USB-to-TTL adapter.

The Microctronller connected to the CA3 via a direct plug from the Microcontroller to the CA3

The Microcontroller connected to all the other e-bike parts via a direct plug.

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

### Nexus 5x Data

The GPS data streamed from the Nexus 5x via the Bluetooth2GPS app are NMEA strings. 

The following NMEA strings are streamed from the Bluetooth2GPS app:

### Need for Data Manipulation

The CA3's serial stream provides data in a tab-delimited format while the Nexus 5x's serial stream provides data in a comma-separated value format. 

To publish with the Streamr CLI, the data must be in a JavaScript Object Notation (JSON) format. 

To convert the CA3 data and Nexus 5x data into JSON, a Python program was developed to access the serial streams from the CA3 and the Nexus 5x, convert the streams into one single JSON file, and push the JSON-formatted file to the console where it would be piped to the Streamr CLI for publishing data. 





## Current Version

## Operation 



# Trials

We conducted two preliminary trials to determine if our configuration was appropriate enough to operate the DBZ-001.

We have conducted two trials so far to determine the bounds of the operation of the DBZ-001.

# Status

We have proved our PoC by building Databike Zeta 001 (DBZ-001), a bicycle that was converted into an electric bicycle (e-bike) with e-bike parts and strapped with two on-board computers, a CA3 (bike computer) and a RPi 3+ (single board computer), and the use of a free-hand Nexus 5x smartphone.  The RPi 3+ stores and manipulates information from two sources:

1. The CA3 that records the internal information of the DBZ-001's sensors; and 
2. The Nexus 5x that records the GPS data from the Nexus 5x's GPS sensor.

The stored data is manipulated into a JSON format and then piped to the Streamr CLI program for publishing data to a stream. 

The commandline program for the Python program and Streamr CLI program is initiated during boot-up on the RPi 3+.

Once the commandline program is running, the data will be streamed to the stream on Streamr.
