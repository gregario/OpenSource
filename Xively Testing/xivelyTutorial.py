#!/usr/bin/env python
 
## This script does the minimum amount needed to take in data and publish it to xively ##
## This includes creating the feeds (done dynamically from the datastreams call)       ##
## Runs in an infinite loop until something breaks somewhere                           ##

# Import different packages needed for this tutorial
import xively, time, datetime, random

# Place your own unique Xively Feed ID and API key into the following array
dev=["FEED_ID","API_KEY"]

# main class
def run():
# Creates an infinite loop
  while True:
    now=datetime.datetime.utcnow() #Updates with system time to properly tie sensor recording with timestamp
    feed = xively.XivelyAPIClient(dev[1]).feeds.get(dev[0]) #Passes API key and Feed ID into the API wrapper 
    
    #Generates a bunch of random data. Insert real data here
    Variable1=random.randrange(0,10)
    Variable2=random.randrange(0,10)
    Variable3=random.randrange(0,10)
    Variable4=random.randrange(0,10)
    Variable5=random.randrange(0,10)
    Variable6=random.randrange(0,10)
    Variable7=random.randrange(0,10)
    Variable8=random.randrange(0,10)
    Variable9=random.randrange(0,10)
    Variable10=random.randrange(0,10)
    Variable11=random.randrange(0,10)
    Variable12=random.randrange(0,10)
    Variable13=random.randrange(0,10)
    Variable14=random.randrange(0,10)
    
    #Passes a bunch of datastream info to the xively package. 
    feed.datastreams = [
    xively.Datastream(id="Variable1",current_value=Variable1,at=now,unit=xively.Unit(label='Celsius',type='basicSI',symbol='Cel')),
    xively.Datastream(id="Variable2",current_value=Variable2,at=now,unit=xively.Unit(label='Celsius',type='basicSI',symbol='Cel')),
    xively.Datastream(id="Variable3",current_value=Variable3,at=now,unit=xively.Unit(label='Celsius',type='basicSI',symbol='Cel')),
    xively.Datastream(id="Variable4",current_value=Variable4,at=now,unit=xively.Unit(label='Celsius',type='basicSI',symbol='Cel')),
    xively.Datastream(id="Variable5",current_value=Variable5,at=now,unit=xively.Unit(label='Celsius',type='basicSI',symbol='Cel')),
    xively.Datastream(id="Variable6",current_value=Variable6,at=now,unit=xively.Unit(label='Celsius',type='basicSI',symbol='Cel')),
    xively.Datastream(id="Variable7",current_value=Variable7,at=now,unit=xively.Unit(label='Celsius',type='basicSI',symbol='Cel')),
    xively.Datastream(id="Variable8",current_value=Variable8,at=now,unit=xively.Unit(label='Celsius',type='basicSI',symbol='Cel')),
    xively.Datastream(id="Variable9",current_value=Variable9,at=now,unit=xively.Unit(label='Celsius',type='basicSI',symbol='Cel')),
    xively.Datastream(id="Variable10",current_value=Variable10,at=now,unit=xively.Unit(label='Celsius',type='basicSI',symbol='Cel')),
    xively.Datastream(id="Variable11",current_value=Variable11,at=now,unit=xively.Unit(label='Celsius',type='basicSI',symbol='Cel')),
    xively.Datastream(id="Variable12",current_value=Variable12,at=now,unit=xively.Unit(label='Celsius',type='basicSI',symbol='Cel')),
    xively.Datastream(id="Variable13",current_value=Variable13,at=now,unit=xively.Unit(label='Celsius',type='basicSI',symbol='Cel')),
    xively.Datastream(id="Variable14",current_value=Variable14,at=now,unit=xively.Unit(label='Celsius',type='basicSI',symbol='Cel')),
    ]
    
    # Attempts to update the feed and if it fails return an error
    try:
      feed.update()
      print "Feed updated"
    except requests.HTTPError as e:
      print "HTTPError({0}): {1}".format(e.errno, e.strerror)
      exit(0)

    time.sleep(10) # Sleeps between loops for 10 seconds

run() #Run main loop