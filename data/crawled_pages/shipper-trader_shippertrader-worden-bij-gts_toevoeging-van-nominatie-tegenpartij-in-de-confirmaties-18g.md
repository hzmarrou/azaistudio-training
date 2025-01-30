# Toevoeging van nominatie tegenpartij in de confirmaties (18G) › Gasunie Transport Services

URL: https://www.gasunietransportservices.nl/shipper-trader/shippertrader-worden-bij-gts/toevoeging-van-nominatie-tegenpartij-in-de-confirmaties-18g#skip-to-content

Toevoeging van nominatie tegenpartij in de confirmaties (18G) › Gasunie Transport Services
Spring naar inhoud
Menu tonen
Menu sluiten
Op virtuele netwerkpunten is het sinds Edig@s versie 5.1, en ook in versie 6.1, verplicht om in de
confirmatie
(NOMRES) berichten naast de
confirmatie
ook de (oorspronkelijke)
nominatie
van de tegenpartij mee te sturen. De codering in het NOMRES bericht geeft de betekenis aan:
16G: geconfirmeerde waarden aan shipper
18G: genomineerde waarden door tegenpartij
Tijdens de eerste implementatie (destijds in versie 5.1) was de stroomrichting voor de 18G functionaliteit lange tijd onduidelijk. Uiteindelijk is in overleg met de Edig@s werkgroep het volgende besloten en ook dusdanig geïmplementeerd.
Let op:
Er zit verschil in de richting tussen Edig@s versie 5.1 en Edig@s versie 6.1 qua stroomrichting voor de 18G waarden.
Voor Edig@s versie 5.1 is voor 18G de stroomrichting van nominaties van de tegenpartij gelijk aan de stroomrichting van de
confirmatie
van de shipper voor zowel entry (Z02) als exit (Z03). In onderstaande figuur is een voorbeeld weergegeven van het versie 5.1 TTF Edig@s bericht met daarin opgenomen de 18G functionaliteit.
Voor Edig@s versie 6.1 is voor 18G de stroomrichting gewijzigd en gelijk gemaakt aan de stroomrichting van de ingezonden
nominatie
door de tegenpartij. Ofwel de stroomrichting van de genomineerde waarden voor de tegenpartij (18G) zijn nu tegengesteld aan de stroomrichting van de geconfirmeerde waarden van de shipper (16G). Dit zowel voor entry (Z02) als exit (Z03) waarden. In onderstaande figuur is een voorbeeld weergegeven van het versie 6.1 TTF Edig@s bericht met daarin opgenomen de 18G functionaliteit.
Deze website vraagt je toestemming cookies te gebruiken voor
YouTube
. Lees het
cookiebeleid
voor meer informatie.
Ik ga akkoord
Ik ga niet akkoord