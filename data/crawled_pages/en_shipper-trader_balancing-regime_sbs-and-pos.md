# SBS and POS › Gasunie Transport Services

URL: https://www.gasunietransportservices.nl/en/shipper-trader/balancing-regime/sbs-and-pos

SBS and POS › Gasunie Transport Services
Jump to content
Show menu
Close menu
On this web page we publish the
System Balance Signal
(SBS). The
System Balance Signal
is the aggregation of the
Portfolio
Imbalance Signals (POSs) of all shippers active in our network.
What are the POS and the SBS?
The balancing regime is based on near-real time information about the cumulative balancing position of every
shipper
(
portfolio imbalance signal
or POS) and of the
system
(
system balance signal
or SBS) as a whole. The SBS is equivalent to the sum total of all POSs and reflects the balancing position of the network
system
.
If we define “damping” as the difference between planned exit and entry submitted by a
shipper
in a programme, we derive a definition for imbalance: imbalance is the difference – on an hourly basis – between the damping in the programme and the difference between the entry and exit actually realised. For programmes without damping, planned entry and exit are equal, also on an hourly basis. In that case, the imbalance is the difference between the near-real time entry allocations and exit allocations.
The programmes (and consequently, the damping) are fixed the day before the actual day of transportation.
Depending on the type of entry and exit points in a
portfolio
, in practice “near-real time” means “with a delay of approximately 5 minutes”. Using the near-real time allocations, we calculate the final near-real time imbalance for each
portfolio
every
hour
(if a
portfolio
consists of an entry and an
exit programme
, the net imbalance is calculated). The hourly imbalance is added to the POS of the previous
hour
to calculate the POS for this
hour
. When all the POSs have been calculated, the SBS is calculated as the sum of all POSs.
The POS will become final approximately 20 minutes after the
hour
. During the
hour
, we calculate the expected SBS every 5 minutes on the basis of the expected POSs for the end of that
hour
. The expected SBS is used to determine if a balancing action should be started on the ICE Endex
Gas
Exchange.
If we define “damping” as the difference between planned exit and entry submitted by a
shipper
in a programme, we derive a definition for imbalance: imbalance is the difference – on an hourly basis – between the damping in the programme and the difference between the entry and exit actually realised. For programmes without damping, planned entry and exit are equal, also on an hourly basis. In that case, the imbalance is the difference between the near-real time entry and exit allocations.
The programmes (and consequently, the damping) are fixed the day before the actual day of transportation.
Depending on the type of entry and exit points in a
portfolio
, in practice “near-real time” means “with a delay of approximately 5 minutes”. Using the near-real time allocations, we calculate the final near-real time imbalance for each
portfolio
every
hour
(if a
portfolio
consists of an entry and an
exit programme
, the net imbalance is calculated). The hourly imbalance is added to the POS of the previous
hour
to calculate the POS for this
hour
. When all the POSs have been calculated, the SBS is calculated as the sum of all POSs.
The POS will become final approximately 20 minutes after the
hour
. During the
hour
, we calculate the expected SBS every 5 minutes on the basis of the expected POSs for the end of that
hour
. The expected SBS is used to determine if a balancing action should be started on the ICE Endex
Gas
Exchange.
Whenever the
system
is “long”, “long” portfolios are defined as “causers” en “short” portfolios are defined as “helpers”. On the other hand when the
system
is “short”, “short” portfolios are defined as “causers” and “long” portfolios are defined as “helpers”. We publish the combined postions of all “helpers” and “causers”. By doing this we enable the “causers” to calculate the part of the volume bought or sold through a balancing action on the exchange of ICE ENDEX that will be assigned to their
portfolio
.
The
System Balance Signal
is an aggregation of all the
Portfolio
Imbalance Signals (POSs) of all portfolios of the active shippers in our network.
Because the POS is commercial sensitive information only the
shipper
can view the individual POS of his
portfolio
. This is made available through our online platform Gasport.
Buffer zones
The flexibility of the national
gas
transport network varies depending on the transport load and is divided into four zones. Based on the anticipated transport load (depending on the programmes delivered by the shippers), we publish the sizes of the zones per
hour
at least two hours before the start of the
gas day
. These hourly values do not change once they have been published.
The four zones are:
Dark green zone
: As long      as the
System
Balance      Signal (SBS) remains within the
dark green zone
, we will not      perform a balancing action.
Light green zone
: If the      predicted
System Balance Signal
(SBS) enters or remains in the light green      zone, we will, under certain circumstances, perform a end of day balancing      action.
Orange zone
: If the      predicted
System Balance Signal
(SBS) enters or remains in the orange      zone, we will perform a next
hour
balancing action.
Red zone
: If the predicted
System Balance Signal
(SBS) enters or remains in the
red zone
, we will      perform a next
hour
balancing action. If we do not expect this to be      sufficient to maintain
system integrity
, we will declare an emergency      situation.
GTS
retains the right to instruct shippers to change      the amount injected at entry points (including entry points with      connected
gas
storage facilitates) and – as a last resort – the      withdrawal at exit points.
Here we publish the buffer zones for the coming
gas day
. The boundary values of the dark green, light green and orange zones can be seen by clicking on the link ‘Actual buffer zones’.
file-chart-line
Buffer zones
Graphic SBS
By clicking on the link ‘Actual graph’, you can view the latest SBS status. The graph shows a short history of the SBS and the prediction for the coming
hour
(the prognosis value). In addition to the SBS, the graph also shows the sum total of the helpers, the sum total of the causers and the buffer zones. By clicking on the second link ‘Download most recent data’, you can download the most recent data as an XML file. The time format is displayed in CET!
file-chart-line
Actual SBS
A 31-day history of the SBS can be obtained by clicking on the link ‘Historical graph’. You can zoom in by selecting a part of the graph.
By clicking "Meer opties" the data can be saved as a XML-file.
Opties
Historical SBS
file-chart-line
Historic SBS (Full screen)
FAQ
Do you have a forecast for the SBS over a longer period of time?
No,
GTS
has only a prognosis value for the coming
hour
.
If the zones are profiled within the gas day answer, can we then also retrieve the profile by means of a report? The SBS report only gives the zones for 1 hour, and the DPM Information exchange does not give any further report of the publication of the zo
Yes, a separate download has been provided for the zones (which indicates zones for one or more
gas
days). It is correct that in the SBS download, this zone info only shows the applicable zone. The specs for the separate zone message are given under the message specifications on the website (GTS_InformationServices_R1).
Will the WDBA notification be visible on Gasport screen? We keep the Gasport POS/SBS page open at all times. What is the content of the notification?
The message that will be constructed has the following format:
GTS
WDM Order Forecast at: <xx:05>/<xx:10> LET -
GTS
<buys>/<sells>
Product: <single
hour
>/<remainder of day>
Amount per
hour
: <value> MW/h
Total amount: <value> MWh
SBS forecast value: <+/-value> MWh
When is my POS reset?
In principle, your POS is never reset. Settlements having an effect on the POS are WDBA’s. It is only when a WDBA is performed that volumes are set off pro rata against the positions (POSs) of the causers. Shippers with a position opposite to the SBS at the time of the balancing action are not affected.
Is the POS available at hh:15 (DPM M&A, chapter 2) really going to be published later at hh:20 (DPM M&A, paragraph 3.12)?
The accountable POS will, apart from in exceptional situations, indeed be published between xx:15 and xx:20. The reason for this is that the near real-time allocations of the CSS are only available at xx:13. This is because actual near real-time allocations are used for determining the accountable POS and not the allocation from a previous
hour
as was the case for the determining the forecast POS.
Is the accountable POS only available at hh:15 for portfolios based on near real-time allocations which are only available after 5 minutes past the hour (such as RNB/PNB,TTF-B, etc.)?
The accountable POS is indeed only available between xx:15 and xx:20.
For a POS where no near real-time allocations are needed that are only available after 5 minutes past the
hour
(such as RNB/PNB,TTF-B, etc.), the prognosticated POS for xx:00 (which is available before xx:05) is equal to the accountable POS at xx:15 – xx:20.
Is it possible to create multiple POSs?
Yes, multiple portfolios with multiple POSses. A POS is per
portfolio
.
Will the WDBA notification be visible on Gasport screen? We keep the Gasport POS/SBS page open at all times. What is the content of the notification?
For the Within Day Balancing Actions a message is displayed immediately when the prognosis is that an order on the exchange platform is required. This message will be displayed on all screens under the Dispatching menu item.
The message that will be constructed has the following format:
GTS
WDM Order Forecast at: <xx:05>/<xx:10> LET -
GTS
<buys>/<sells>
Product: <single
hour
>/<remainder of day>
Amount per
hour
: <value> MW/h
Total amount: <value> MWh
SBS forecast value: <+/-value> MWh
This website requests your permission to use cookies for
YouTube
. Read our
cookie policy
for more information.
I agree
I don't agree