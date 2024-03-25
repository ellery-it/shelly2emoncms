# Intro
Allows the use af a Shelly EM device  (which should be configured to post values on a local MQTT broker instead of cloud) in association to EmonCMS installed on a raspberry without any other hardware (EmonTX, emonBase). 
This Python script will allow to translate MQTT topics posted from Shelly EM to topics compatible with OpenEnergyMonitor EmonHub/EmonCMS

# Prerequisites
  
  pip3 install paho-mqtt

# Install
*connect with ssh (i.e. putty) to emonpi (default hostname: `emonpi` ) from the same LAN and login with username and password (es: pi/emonsd )*

    cd ~
    git clone https://github.com/ellery-it/shelly2emoncms.git
    cd shelly2emoncms
    
# Configuration
    adjust parameters (mqtt broker and shelly device configuration)
    nano  mqtt_forwarder.py
    
# Test
    python3 mqtt_forwarder.py

# Install as service
    todo
    see https://gist.github.com/emxsys/a507f3cad928e66f6410e7ac28e2990f
    
# Uninstall
    cd ~
    rm -rf shelly2emoncms

    
# Notes / References
  - For an explanation on MQTT see http://www.steves-internet-guide.com/client-connections-python-mqtt/
  - OpenEnergyMonitor EmonHub/EmonCMS (https://docs.openenergymonitor.org/emoncms/index.html)
  - Install EmonCMS on a raspberry https://docs.openenergymonitor.org/emonsd/download.html
  - Shelly EM:
      - https://kb.shelly.cloud/knowledge-base/shelly-em
      - https://shelly-api-docs.shelly.cloud/gen1/#shelly-em-mqtt
      - https://support.shelly.cloud/en/support/solutions/articles/103000044280-how-can-i-enable-the-mqtt-feature-
  - for an alternative approach see also Node-Red https://iot.stackexchange.com/questions/5215/i-need-to-transform-mqtt-topic-is-it-possible
