# SpiderPi-OOP-Project

## 1. Initiële Verbinding (AP-modus)
De SpiderPi start standaard op in Access Point (AP) Modus.

    Verbind met het netwerk: Verbind je laptop met de Wi-Fi SSID die begint met HW-.

    Wachtwoord: hiwonder

    Toegang tot de Desktop: Open VNC Viewer en verbind met de standaard gateway: 192.168.149.1.

        Gebruikersnaam: pi

        Wachtwoord: raspberrypi

 2. Brug slaan naar Persoonlijke Hotspot (STA-modus)

Om de robot internettoegang te geven en te laten communiceren met een laptop op een breder netwerk, moet deze worden omgeschakeld naar Station (STA) Modus.

    Open Terminal (in de robot): Open de terminal binnen de VNC-omgeving en typ nmtui.

    Activeer Verbinding: Kies "Activate a connection" en zoek je eigen telefoon-hotspot.

    Configuratie: Als de verbinding verbreekt, herstart de robot. Gebruik de GUI (Wi-Fi icoon) om via "Connect to Hidden Network" de verbinding te forceren en het wachtwoord op te slaan.

    Verificatie: Zodra zowel de robot als je laptop op dezelfde hotspot zitten, krijgt de robot een nieuw IP-adres toegewezen.

 3. De Robot lokaliseren op het netwerk

Omdat het IP-adres verandert in STA-modus, gebruiken we nmap op een linux-systeem om de IP te vinden.

    Zoek het IP van je laptop:
    Bash

    hostname -I

    Scan de netwerk-range:
    Als je eigen IP bijvoorbeeld 10.x.x.217 is, scan dan het subnet (vervang x door je eigen getallen):
    Bash

    sudo nmap -sn 10.x.x.0/24

    Identificeer de robot: Zoek naar het apparaat met de label Raspberry Pi (Trading) of Hiwonder.

