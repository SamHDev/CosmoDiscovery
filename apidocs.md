

# Cosmo Network Discovery API 
Documentation for The Custom OpenSource Cosmo Network Discovery API 

#### What is the Discovery API?
The Discovery API is a implementation of UDP Sockets to broadcast and receive messages across a network.
The Discovery API is used to find devices on a Network and is Currently used to find fellow CosmoHome Devices
on the network for communication and data sharing purposes. Its also used for Finding Devices for the Setup on
The User's Current Mobile Device Network as pre set-up devices and for Finding the Device IP on the Device's 
Hotspot for communication with the Device Web API. 

##### Implementations
The Discovery API has a Python Server and Client wrapper and a Java client wrapper. 

If there is no Implementation for your preferred language Feel Free to write your own wrapper and send over to us!
or ask us to write one for you.

---

#### The Protocol
##### API Description
The Cosmo Discovery API uses UDP Sockets to send, receive and broadcast messages across the Network.

The Default port for handling communications is `12892`. In reality this should stay the same throughout
all instances for the Protocol due to the use of the `scheme` parameter. However there is the option
to change it if need be, as customisation is at the forefront of the protocol.

To Broadcast on the network the IP/Host `255.255.255.255` is used. This should 'Broadcast' the message
across the network. This may change depending on your network settings. 

##### API Format

The Protocol is in a JSON format with every message should follow the Message Object Guidelines as per below.
Bytes should be sent in a UTF-8 Encoded Format.

###### Message Object (Root)

| Key | Type | Description |
| --- | ---- | ----------- |
| `proto` | string | Protocol Name, This should stay as `_cosmo.discovery` Used as a way to check Protocol |
| `scheme` | string | Scheme Name, Used to restrict message which client finds who. Default `_discovery._cosmo.default` |
| `request` | RequestMethod | Request Name, The Operation for the Client or Server to Complete |
| `host` | HostObject | A Object that contains sender address data |
| `data` | object | Additional Custom Message Data |

Each Message Object contains a Host Object. This contains data about the message sender.
This comes in handy when communicating over a different API such as a WEB API

###### Host Object (Root)

| Key | Type | Description |
| --- | ---- | ----------- |
| `ip` | string | The Sender IP |
| `port` | integer | The Port the message was sent on |
| `mask` | string | The Mask or Host that was used to send the message |
| `mac` | string | The MAC address of the Sender Device |
| `name` | string | The Hostname of the sender device. (Not Custom Name) |

The Request Methods Control the Server/Client and control the reply

###### Request Methods

| Key | Type | Description |
| --- | ---- | ----------- |
| `discovery.find` | string | Discovery Request for clients with the same scheme |
| `discovery.reply` | string | A Reply to a Discovery Request |
| `client.error` | string | null, Basically should never be used |


