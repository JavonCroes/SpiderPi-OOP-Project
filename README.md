# 🕷️ SpiderPi OOP Project

Deze repository bevat de documentatie en code voor het SpiderPi robotproject.

---

## 1. Initiële Verbinding (AP-modus)
De SpiderPi start standaard op in **Access Point (AP) Modus**. Dit stelt je in staat om direct verbinding te maken met de robot zonder extern netwerk.

### Verbindingsgegevens
| Onderdeel | Waarde |
| :--- | :--- |
| **SSID** | Begint met `HW-` |
| **Wachtwoord** | `hiwonder` |
| **VNC IP-adres** | `192.168.149.1` |
| **SSH/VNC User** | `pi` |
| **SSH/VNC Pass** | `raspberrypi` |

> **Note:** Gebruik een VNC Viewer (zoals RealVNC) om toegang te krijgen tot de grafische interface via het bovenstaande IP-adres.

---

## 2. Brug naar Persoonlijke Hotspot (STA-modus)
Om de robot internettoegang te geven of via een lokaal netwerk te bereiken, schakelen we over naar de **Station (STA) Modus**.

1. **Terminal:** Open de terminal binnen de VNC-omgeving.
2. **NMTUI:** Typ `nmtui` in de console voor de netwerkmanager.
3. **Activeer:** Kies *'Activate a connection'* en zoek je eigen hotspot/Wi-Fi.
4. **Configuratie:** Mocht de verbinding verbreken, herstart de spiderpi en gebruik dan nmtui nog een keer maar selecteer dan *'Edit a connection'* en zet je wachtwoord van je hotspot erin probeer dan stap 3 nog een keer.

---

## 3. Automatisering: Bash Verbindingsscript
In plaats van handmatige configuratie kun je onderstaand script gebruiken om snel te schakelen.

### Stap 1: Maak het script aan

nano connect_hotspot.sh

### Stap 2 Plak deze code erin
```bash
#!/bin/bash

# --- CONFIGURATIE ---
SSID="JOUW_SSID"
PASS="JOUW_WACHTWOORD"

echo "------------------------------------------"
echo "Stap 1: Wifi aanzetten..."
nmcli radio wifi on

echo "Stap 2: Forceer een netwerk-scan (even geduld...)"
nmcli device wifi rescan
sleep 5 

echo "Stap 3: Beschikbare netwerken controleren..."
nmcli device wifi list | grep "$SSID"

echo "Stap 4: Verbinden met $SSID..."
nmcli device wifi connect "$SSID" password "$PASS"

echo "------------------------------------------"
echo "Klaar! Jouw IP adres is:"
hostname -I
echo "------------------------------------------"
```
ctrl + o dan enter 

ctrl + x

### Stap 3 Maak het script uitvoerbaar
chmod +x connect_hotspot.sh

## Stap 4 Run de script
./connect_hotspot.sh