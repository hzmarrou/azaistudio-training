# SBS en POS › Gasunie Transport Services

URL: https://www.gasunietransportservices.nl/shipper-trader/balanceringsregime/sbs-en-pos

SBS en POS › Gasunie Transport Services
Spring naar inhoud
Menu tonen
Menu sluiten
Op deze webpagina publiceren wij het
Systeem Balans Signaal
(SBS). Het
Systeem Balans Signaal
is een aggregatie van de
Portfolio
Onbalans Signalen (POS’en) van alle in ons netwerk actieve Shippers.
Wat is het SBS en wat is het POS?
Het balanceringsregime is gebaseerd op near real time informatie over de cumulatieve balanceerpositie van iedere Shipper (
portfolio onbalans signaal
of POS) en van het
systeem
(systeembalanssignaal of SBS) als geheel. Het SBS is gelijk aan de som van alle POS’en en geeft de balanspositie van het netsysteem weer.
Wanneer we “demping” definiëren als het verschil tussen de door een Shipper in een programma opgestuurde geplande exit en entry, leiden we hieruit een definitie af voor onbalans: onbalans is het verschil - op uurbasis - tussen de demping in het programma en het verschil tussen de gerealiseerde entry en exit. Voor programma’s zonder demping zijn de geplande entry en exit - óók op uurbasis - gelijk. De onbalans is dan het verschil tussen de near real time entry en exit allocaties.
De programma’s (en dus ook de demping) worden de dag vóór de feitelijke dag van het transport vastgelegd.
Al naar gelang het type entry- en exitpunten in een
portfolio
betekent “near real time” in de praktijk “met een vertraging van ongeveer 5 minuten”. Aan de hand van de near real time allocaties berekenen wij ieder
uur
voor ieder
portfolio
de definitieve near real time onbalans (wanneer een
portfolio
uit een entry- en een
exitprogramma
bestaat, wordt de netto onbalans berekend). De onbalans per
uur
wordt bij het POS van het vorige
uur
opgeteld om het POS voor dit
uur
te berekenen. Wanneer alle POS’en berekend zijn, wordt het SBS berekend als de som van alle POS’en.
Het POS wordt ongeveer 20 minuten na het
uur
definitief. Tijdens het
uur
berekenen wij elke 5 minuten het verwachte SBS op basis van de verwachte POS’en voor het einde van dat
uur
. De verwachte SBS wordt gebruikt om te bepalen of een balanceeractie wordt gestart op de
Gasbeurs
van ICE Endex.
Wanneer het
systeem
“long” is, worden
portfolio
's die long zijn, gedefinieerd als “veroorzakers” en
portfolio
's die “short” zijn, gedefinieerd als “helpers”. Wanneer het
systeem
daarentegen “short” is, worden
portfolio
's die “short” zijn, gedefinieerd als “veroorzakers” en
portfolio
’s die “long” zijn, gedefinieerd als “helpers”. Samen met het SBS worden de gecombineerde posities van “helpers” door ons bekend gemaakt. Door het totale POS-volume van de “helpers” en de “veroorzakers” bekend te maken, wordt de Shipper die een onbalans veroorzaakt in staat gesteld om het gasvolume (gekocht of verkocht op de
Gasbeurs
van ICE Endex) dat aan zijn
portfolio
wordt toegewezen te berekenen.
Het
Systeem Balans Signaal
is een aggregatie van de
Portfolio
Onbalans Signalen (POS’en) van alle in ons netwerk actieve Shippers.
Omdat het POS een commercieel gevoelig signaal betreft kan alleen de shipper zelf de stand van het individuele POS bekijken, dat kan via ons online platform GasPort.
Buffer zones
Op basis van de verwachte transportbelasting (afhankelijk van de programma’s die door de shippers geleverd zijn) maken wij uiterlijk twee
uur
voor start van de
gasdag
de omvang van de zones per
uur
bekend. Deze uurwaarden worden na de bekendmaking niet meer gewijzigd.
Rode zone
; Wanneer het voorspelde
Systeem Balans Signaal
(SBS) in de
rode zone
komt of blijft, zullen wij ook een "next hour" balanceringsactie ondernemen. Indien wij verwachten dat dit niet voldoende zal zijn om het
systeem
integer te houden, zullen wij bekend maken dat er sprake is van een noodsituatie.
GTS
is gerechtigd om shippers te instrueren de invoeding op de entry punten (inclusief entry punten met aangesloten gasopslagfaciliteiten) en – als laatste redmiddel – de afname op  exit punten te wijzigen.
Oranje zone
; Wanneer het voorspelde
Systeem Balans Signaal
(SBS) in de
oranje zone
komt of blijft, zullen wij een "next hour" balanceringsactie ondernemen.
Lichtgroene zone
; Wanneer het voorspelde
Systeem Balans Signaal
(SBS) in de
lichtgroene zone
komt of blijft, zullen wij een "end of day" balanceringsactie ondernemen.
Donkergroene zone
; Zolang het
Systeem Balans Signaal
(SBS) in de
donkergroene zone
blijft, zullen wij geen balanceringsactie ondernemen.
Hieronder publiceren wij de bufferzones voor de komende
gasdag
. Via de link ‘Actuele buffer zones’ zijn de grenswaarden van de donkergroene, lichtgroene en oranje zones te zien. De flexibiliteit van het landelijke
gastransportnet
varieert afhankelijk van de transportbelasting en is verdeeld in vier zones.
file-chart-line
Buffer zones (volledig scherm)
Grafiek SBS
Via ‘Actuele grafiek’ kan de laatste stand van het SBS worden verkregen. In de grafiek is een korte historie van het SBS te zien, evenals de voorspelling voor het komende
uur
(de prognose waarde). Naast het SBS worden ook de sommatie van helpers, de sommatie van de veroorzakers en de bufferzones getoond in de grafiek. De tijdsnotatie wordt weergegeven in CET!
file-chart-line
Actuele SBS (volledig scherm)
Een historie van 31 dagen van het SBS kan verkregen worden via de ‘Historische grafiek’. Door een deel van de grafiek te selecteren is het mogelijk om in te zoomen. De tijdsnotatie wordt weergegeven in CET!
Via "Meer opties" kan de historische data worden verkregen in een XML-file.
Opties
Historische SBS
file-chart-line
Historische SBS (volledig scherm)
Veelgestelde vragen
Is de SBS forecast voor de lange termijn beschikbaar?
Nee,
GTS
heeft een SBS forecast naar het eerstvolgende
uur
.
Als de zones een profiel over de dag hebben, kunnen we het profiel van zones dan downloaden door middel van een rapport? In het SBS rapport worden slechts zones voor één uur gegeven. Het DPM Information Exchange noemt verder een 'portal' waarin de zones g
Ja, er is een separate download voor de zones met daarin de zones voor één of meerdere gasdagen. In het SBS rapport staat inderdaad maar voor één
uur
zone-informatie. De specificaties voor de separate download staan onder de berichtdefinities op de website (GTS_InformationServices_R1)
Zal de WDBA aankondiging op Gasport  op alle schermen zichtbaar zijn? Het POS/SBS scherm staat bij ons altijd open. Welke informatie zal worden getoond?
De WDBA aankondiging in Gasport wordt onmiddellijk getoond als de SBS prognose aanleiding geeft om een order op de ICE Index te gaan plaatsen. Deze aankondiging wordt getoond op alle schermen van het Dispatching menu item. De volgende informatie wordt getoond:
GTS
WDM Order Forecast at: <xx:05>/<xx:10> LET -
GTS
<buys>/<sells>
Product: <single hour>/<remainder of day>
Amount per hour: <value> MW/h
Total amount: <value> MWh
SBS forecast value: <+/-value> MWh
Wanneer wordt mijn POS ge-reset?
Uw POS wordt in principe nooit ge-reset. Verrekeningen die effect hebben op de POS zijn WDBA’s. Alleen wanneer een WDBA wordt uitgevoerd, worden afgeroepen volumes pro rata verrekend met de posities (POS-en) van de veroorzakers. Shippers met een positie tegenovergesteld aan de SBS ten tijde van de balancing action worden niet geraakt.
Wanneer wordt het POS signaal van xx:15 gepubliceerd?
Door de verwerkingstijd wordt het POS signaal van xx:15 gepubliceerd om ca. xx:20. Dit geldt overigens voor alle 5-minutenwaarden. Er zijn ca. 5 minuten nodig om de waarden te berekenen, verwerken en publiceren.
Wat is het verschil tussen de near real time POS en de accountable POS (beide behorend bij xx:00)?
In het accountable POS signaal op het volle
uur
(xx:00) is rekening gehouden met allocaties op RNB punten. Deze allocaties komen pas later beschikbaar (ca. xx:13) voor het afgelopen
uur
. Wanneer een partij geen RNB punten in het
portfolio
heeft, is het accountable POS signaal (dat beschikbaar komt om ca. xx:20) gelijk aan het near real time POS signaal dat om ca. xx:05 beschikbaar komt. Let op: beide geven de POS waarde van xx:00.
Is het mogelijk om meerdere POS-en te hebben?
Ja dat kan, er wordt een POS signaal gecreëerd voor elk
portfolio
. Meerdere
portfolio
's voor een partij geven meerdere (onafhankelijke) POS'en.
Zal de WDBA aankondiging op Gasport  op alle schermen zichtbaar zijn? Het POS/SBS scherm staat bij ons altijd open. Welke informatie zal worden getoond?
De WDBA aankondiging in Gasport wordt onmiddellijk getoond als de SBS prognose aanleiding geeft om een order op de ICE Index te gaan plaatsen. Deze aankondiging wordt getoond op alle schermen van het Dispatching menu item. De volgende informatie wordt getoond:
GTS
WDM Order Forecast at: <xx:05>/<xx:10> LET -
GTS
<buys>/<sells>
Product: <single hour>/<remainder of day>
Amount per hour: <value> MW/h
Total amount: <value> MWh
SBS forecast value: <+/-value> MWh
Deze website vraagt je toestemming cookies te gebruiken voor
YouTube
. Lees het
cookiebeleid
voor meer informatie.
Ik ga akkoord
Ik ga niet akkoord