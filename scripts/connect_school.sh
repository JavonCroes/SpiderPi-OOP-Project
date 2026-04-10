#!/bin/bash

SSID="iotroam"
PASS="SpiderPi01"

echo "? Bezig met scannen naar beschikbare netwerken..."
# Dwing de Wi-Fi chip om een nieuwe scan te doen
sudo nmcli device wifi rescan
sleep 2 # Geef de chip even tijd om de lijst bij te werken

# Check of iotroam in de lijst staat
VISIBLE=$(nmcli -t -f SSID dev wifi | grep -w "$SSID")

if [ -z "$VISIBLE" ]; then
    echo "? Fout: Netwerk '$SSID' niet gevonden in de buurt."
    echo "Beschikbare netwerken zijn:"
    nmcli -t -f SSID dev wifi | sort -u
else
    echo "? '$SSID' gevonden! Verbinden..."
    sudo nmcli dev wifi connect "$SSID" password "$PASS"
    
    echo "-------------------------------------------"
    echo "? Nieuw IP-adres op schoolnetwerk:"
    hostname -I | cut -d' ' -f1
    echo "-------------------------------------------"
    echo "??  SSH kan nu bevriezen. Maak opnieuw verbinding."
fi
