# Intro
This Python script will allow to translate MQTT topics posted from Shelly EM to topics compatible with OpenEnergyMonitor EmonHub/EmonCMS (https://docs.openenergymonitor.org/emoncms/index.html)
Allow the use af a Shelly EM device  (which should be configured to post values on a local MQTT broker instead of cloud) in association to EmonCMS installed on a raspberry without any other hardware (EmonTX, emonBase)

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
   Using systemd: This is a more modern init system used by many Linux distributions. You can create a systemd service file to run your script at startup.
   Using init.d: This is an older init system still used by some distributions. You can create a script file to be placed in the /etc/init.d directory.
    
# Uninstall
    cd ~
    rm -rf shelly2emoncms

    
# Notes / References
  For an explanation on MQTT see http://www.steves-internet-guide.com/client-connections-python-mqtt/
  Install EmonCMS on a raspberry https://docs.openenergymonitor.org/emonsd/download.html
  Shelly EM https://kb.shelly.cloud/knowledge-base/shelly-em
