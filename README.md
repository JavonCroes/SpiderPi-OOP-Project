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

## 2. Automatisering: Bash Verbindingsscript in de SpiderPi terminal
In plaats van handmatige configuratie kun je onderstaand bash script gebruiken om snel te connecten.

### Stap 1: Maak het script aan
```bash
nano connect_school.sh
```
### Stap 2 Plak deze code erin (Verander de SSID en PASS)
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
```bash
chmod +x connect_school.sh
```
## Stap 4 Run de script
```bash
./connect_school.sh
```

Zodra de verbinding is omgezet naar iotroam kun je de robot op je laptop vinden via:
```bash
    ping raspberrypi.local
```
