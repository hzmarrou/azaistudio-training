# Balancering regime › Gasunie Transport Services

URL: https://www.gasunietransportservices.nl/en/faq/balancering-regime#skip-to-content

Balancering regime › Gasunie Transport Services
Jump to content
Show menu
Close menu
I will only trade on the TTF and so I assume that I will always be in balance. Is the balancing regime applicable to me in this case?
Yes, traders also need to be informed about the balancing regime and needs to be able to receive and send all the related messages.
Although, fundamentally, a trader will not experience imbalances quickly, it may be the case that an imbalance occurs between entry and exit in the
portfolio
, e.g. due to incorrect
portfolio
management or an error in the nominations/confirmations with counterparties.
How can I become an offeror on the gas exchange of ICE Endex?
If you want to become an offeror on the
gas
exchange you must satisfy a number of requirements. Click
here
for the website of ICE Endex. If you can trade on the exchange of ICE Endex that is sufficient to offer flexibility to the
gas
exchange in the run-up to a balancing action.
GTS
does not propose any additional requirements.
When is my POS reset?
In principle, your POS is never reset. Settlements having an effect on the POS are WDBA’s. It is only when a WDBA is performed that volumes are set off pro rata against the positions (POSs) of the causers. Shippers with a position opposite to the SBS at the time of the balancing action are not affected.
How often is a "Within-Day-Balancing Action '(WDBA) performed?
It is impossible to estimate in advance. We look 10 minutes and 15 minutes past the
hour
to the end of
hour
prediction of the SBS. If the prediction of the SBS at 10 minutes past the
hour
gives a reason to a WDBA, then an announcement is made in Gasport and a Request For Quote (RFQ) is placed on the trading screen of the ICE Endex. The announcement and the RFQ is an estimate of the volume and product placed on the within-day market of ICE Endex and is based on the latest information.
If the prediction of the SBS at 15 minutes past the
hour
still gives a reason to a WDBA, then an update of the announcement is made and again a Request For Quote (RFQ) is placed on the trading screen of ICE Endex.
If the prediction of the SBS for the next
hour
at 20 minutes past the
hour
gives a reason for a WBDA than an order is placed on the within-day market of ICE Endex.
The type of product for which the order is placed, is dependent on the color of the zone wherein the SBS is predicted. In the
light green zone
GTS
send an order for a WD product to the exchange with a lead time of 3 hours and 40 minutes with supplies for the remaining hours of the
gas day
. As an indication, an order that leads to a transaction at 12:20 will be delivered from 16:00 to 06:00. In the orange and
red zone
GTS
send an order for a Next-
Hour
product with a lead time of 40 minutes. The whole delivery takes place in one clock
hour
. An order for a Next
Hour
product that leads to a transaction at 12:20 has a delivery from 13:00 to 14:00.
How often are the zones adjusted?
We disclose the size of the zones per
hour
, based on the estimated transport load (with regard to the programmes delivered by the Shippers), at least two hours before the beginning of the
gas day
. These hourly values will not be changed after they have been published.
Am I obliged to apply damping?
No, you are only obliged to apply damping if you transport
gas
to exit points that deliver to domestic consumers.
How much gas does GTS call up when placing a WDBA?
The volume that must be called will be calculated as follows:
Difference between the anticipated final value of the SBS and the boundary value of the
dark green zone
.
The part that possibly is not yet delivered of a realized WDBA transaction is included in the determination of the volume of any new WDBA. This only applies for WDBA with the SBS in the light green area.
If the SBS is in the light-green zone, and the imbalance is less than the unbalance of the previous
hour
, no WDBA will take place.
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
Do you have a forecast for the SBS over a longer period of time?
No,
GTS
has only a prognosis value for the coming
hour
.
Is wheeling subject to the same balancing rules as regular bookings?
Yes, the POS is also determined for a
wheeling
portfolio
and a WDBA may also apply.
Can the zones be profiled within the gas day (i.e. not a constant value)?
Yes this is possible.
Are the zones (by definition) symmetric?
Yes
If the zones are profiled within the gas day answer, can we then also retrieve the profile by means of a report? The SBS report only gives the zones for 1 hour, and the DPM Information exchange does not give any further report of the publication of the zo
Yes, a separate download has been provided for the zones (which indicates zones for one or more
gas
days). It is correct that in the SBS download, this zone info only shows the applicable zone. The specs for the separate zone message are given under the message specifications on the website (GTS_InformationServices_R1).
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
What are the changes on the invoice due to the new balancing rules?
The invoice is kept the same as the BidPriceLadder invoice as much as possible. The two changes are:
The Line Pack Flexibility Service is added
On the front page (PDF) the total of balancing actions (supplied en received) is mentioned in “Exchange”. In the attachment you can find per balancingaction if it concerns supplied or received.
This website requests your permission to use cookies for
YouTube
. Read our
cookie policy
for more information.
I agree
I don't agree