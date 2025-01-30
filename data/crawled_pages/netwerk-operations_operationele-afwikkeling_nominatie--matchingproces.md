# Nominatie- & Matchingproces › Gasunie Transport Services

URL: https://www.gasunietransportservices.nl/netwerk-operations/operationele-afwikkeling/nominatie--matchingproces#skip-to-content

Nominatie- & Matchingproces › Gasunie Transport Services
Spring naar inhoud
Menu tonen
Menu sluiten
Het gastransport binnen Nederland en naar onze partnerlanden vindt plaats op basis van nominaties die shippers naar het nominatiesysteem van
Gasunie Transport Services
(
GTS
) sturen. Als shipper dient u door middel van een
nominatie
bij ons aan te geven hoeveel
gas
(in kWh/h) u voor elk
uur
van de
gasdag
op een netwerkpunt getransporteerd wilt hebben.
Nominatieproces voor fysieke entry- en exitpunten
Er geldt een nominatieplicht voor ieder netwerkpunt waarvoor u
capaciteit
bij ons heeft gecontracteerd. Vrijstelling van de nominatieplicht is alleen mogelijk op basis van artikel 2.3 uit Appendix 5 van onze TSC.
Nominaties worden bij ontvangst gevalideerd tegen de door u
gecontracteerde capaciteit
voor het betreffende netwerkpunt. Indien de
nominatie
hoger is dan deze
capaciteit
, wordt u hierover geïnformeerd. In dat geval wordt de
nominatie
afgewezen en niet verder meegenomen in het proces. Wanneer u niet (tijdig) hernomineert binnen uw
gecontracteerde capaciteit
, ontvangt u een nul-
confirmatie
; er wordt dan een nul-
nominatie
verondersteld.
Initiële nominaties dienen om 14.00
uur
op de
gasdag
voorafgaand aan de
gasdag
waarop het transport dient plaats te vinden, door ons ontvangen te zijn. Indien gewenst en zolang de looptijd van het contract dit toelaat, kan tot 179 dagen vooruit worden genomineerd.
Vóór 16.00
uur
op de
gasdag
voorafgaand aan de
gasdag
waarop het transport dient plaats te vinden, ontvangt u van ons uw
confirmatie
. Indien uw
confirmatie
afwijkt van de
nominatie
bevat de
confirmatie
ook de reden van deze afwijking; dat kan bijvoorbeeld een mismatch of een interruptie zijn.
Nominaties die tussen 14.00 en 16.00
uur
door ons worden ontvangen, worden ook meteen op
capaciteit
getoetst. Over het resultaat van deze controle wordt u meteen geïnformeerd. Pas in het hernominatieproces (na 16.00
uur
) wordt uw
nominatie
in behandeling genomen voor verdere verwerking. Wijzigingen in nominaties kunnen aangegeven worden middels een
hernominatie
, waarbij rekening gehouden dient te worden met de lead time  op het betreffende netwerkpunt. Het eerstvolgende klokuur na ontvangst van een (her)
nominatie
nemen we deze in behandeling.
Op vrijwel alle grens- en aanlandingspunten van zeeleidingen vindt het matchingsproces tussen
GTS
en de neighbouring network operator (
NNO
) plaats. Dit houdt in dat er berichtenuitwisseling van
nominatie
-informatie plaatsvindt tussen
GTS
en de
NNO
waarbij de
nominatie
die
GTS
heeft ontvangen wordt vergeleken met de nominaties die de
NNO
heeft ontvangen. Bij een verschil wordt de standaard matchingsregel Lesser of Rule (LoR) toegepast. Concreet betekent dit dat de laagste waarde van de
nominatie
van onze shipper en zijn countershipper bij de
NNO
richting beide shippers wordt geconfirmeerd. Zowel
GTS
als de
NNO
sturen een confirmatiebericht met het matchingsresultaat naar hun eigen shippers.
Indien het nodig is om nominaties die op basis van interruptible
capaciteit
zijn ontvangen af te schakelen, gebeurt dit voorafgaand aan het matchingsproces. Afschakeling gebeurt op basis van prioritering; bij gelijke prioriteit van het contract (bij een gelijke timestamp) vindt verdere verdeling op pro rata-basis plaats. Het resultaat van afschakeling wordt meegenomen in het verdere proces en is via de
confirmatie
zichtbaar.
Nominaties voor TTF en TTFB
Op de virtuele netwerkpunten TTF en TTFB kan door middel van nominaties
gas
overgedragen worden. Indien geen
gas
wordt overgedragen hoeft u hier ook niet te nomineren, in tegenstelling tot fysieke netwerkpunten waar een nominatieverplichting geldt. Nominaties die worden ingestuurd dienen bij
GTS
erkende en geldige portfoliocodes te bevatten. Indien gewenst, kan op deze virtuele netwerkpunten tot 400 dagen vooruit worden genomineerd.
Het matchingsproces vindt plaats op basis van initiële nominaties van de aan elkaar
gas
overdragende shippers. Alle Future en Day Ahead nominaties die vóór 04.00
uur
zijn ontvangen, gaan het eerstvolgende hele klok
uur
mee in het matchingsproces. Vanaf 04.30
uur
vindt het Day Ahead matchingsproces iedere 30 minuten plaats, zodat alle (her)nominaties voor aanvang van de nieuwe en gedurende de huidige
gasdag
tijdig geconfirmeerd worden.
Op TTF en TTFB is een lead time van 30 minuten van toepassing.
Een
confirmatie
krijgt de status ‘No Counternomination’ (NC) indien van één van beide partijen nog geen
nominatie
is ontvangen. De confirmaties krijgen de status ‘Settled’ (S), indien beide genomineerde waarden overeenkomen. Is dit niet het geval, dan krijgt de
confirmatie
de status ‘MisMatch’ (MM) en wordt middels de Lesser of Rule (LoR) de laagste waarde aan beide partijen geconfirmeerd.
Confirmaties op TTF en TTFB krijgen de status ‘Unchanged Settled’ (US) als één van beide partijen een gewijzigde
hernominatie
instuurt, nadat eerder een ‘Settled’ deal is geconfirmeerd. Concreet betekent dit dat de eerder geconfirmeerde waarde intact blijft en dat partijen na een ‘Settled’ deal te hebben gesloten, niet eenzijdig hun deal kunnen wijzigen. Pas wanneer beide partijen hernomineren en de genomineerde waarden overeenkomen, zal er opnieuw een
confirmatie
worden uitgestuurd met een status ‘Settled’ (S) deal.
Hernominaties voor TTFB ten behoeve van de huidige
gasdag
zijn niet mogelijk; het bericht wordt dan ook afgewezen en niet meegenomen in het verdere matchingproces.
Matching regel Producer Prevail (PP)
De standaard matchingregel op netwerkpunten met een aangrenzende
NNO
(Neighboring Network Operator) is de Lesser of Rule (LoR) van toepassing. Dit betekent dat wanneer er sprake is van een verschil in ontvangen nominatiewaarden, de laagste waarde leidend is en aan beide partijen wordt geconfirmeerd.
Op sommige grens-netwerkpunten wordt echter van deze standaard matchingsregel afgeweken en is met de aangrenzende netwerk operator (
NNO
) een andere regel afgesproken: de Producer Prevail (PP)-regel. Deze regel is dan de default matchingsregel op het betreffende netwerkpunt en bestaat veelal tussen
GTS
en
NNO
’s met land- of zeeleidingen waarop meerdere producenten zijn aangesloten. De Producer Prevail-regel houdt in dat, in geval van een verschil in nominaties die door
GTS
zijn ontvangen en die door een producent zijn ontvangen, de
nominatie
van de
NNO
-shipper (upstream) leidend is. Dat wil zeggen dat deze wordt overgenomen door
GTS
en (zonder verlaging) aan haar de shippers van
GTS
(downstream) worden geconfirmeerd.
Het is raadzaam ten tijde van de contractuele afhandeling en vóór aanvang van de
levering
met zowel
GTS
als de
NNO
(producent) af te stemmen welke matchingregel van toepassing is. De
NNO
(producent) wordt verondersteld op aangeven van zijn shipper dezelfde matchingregel in haar nominatiesysteem te implementeren en in haar matchingproces toe te passen.
Deze website vraagt je toestemming cookies te gebruiken voor
YouTube
. Lees het
cookiebeleid
voor meer informatie.
Ik ga akkoord
Ik ga niet akkoord