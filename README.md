# Cosmo Network Discovery API 
Documentation for The OpenSource Cosmo Network Discovery API 

This is the main implemtation written in python. For other implementations see [Implemtations](implemtations.md)
and for a description on the API and Protocol see [API Docs](apidocs.md)

### Installation

You can Install it with Pip and PyPi
```
python3 -m pip install cosmodiscovery
```
or with Pip and Github without PyPi
```
python3 -m pip install git+https://github.com/SamHDev/CosmoDiscovery.git
```

### Usage
Import the libary
```py
import cosmodiscovery as discovery
```
#### A Discovery Server
```py
server = discovery.DiscoveryServer()
server.listen()
```
Yep! Thats it! 

If you want a custom `scheme` or `port` you can do it like this:

```py
server = discovery.DiscoveryServer(port=12892, scheme="_discovery._cosmo.home_device"))
```
Sending Custom Data with the discovery reply. `cls` is a `DiscoveryRequestMessage` Object
```py
@server.discovery_callback
def on_msg(cls):
cls.reply(data={})
```

#### A Discovery Client

Create a DiscoveryClient Object like this
```py
server = discovery.DiscoveryServer()
```
Or with Paramaters like so
```py
client = discovery.DiscoveryClient(port=12892, scheme="_discovery._cosmo.home_device"))
```

One Created you can run this
```py
results = client.discovery()
```
This function returns a list of `DiscoveryResult` objects. If the list is empty, then no devices were found.

If you wish to add arguments such as custom data to send within the Discovery Request or shorten the discovey reply wait time
you can do so like this:
`
results = discovery(timeout=1, data={})
`
Again! Its that simple

#### Further Documentation
For Further Documentation see docs.md

---

Written for [CosmoHome](https://cosmosmarthome.com) by [SamHDev](https://github.com/SamHDev/). [License]([LICENSE])

