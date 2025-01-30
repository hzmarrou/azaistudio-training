# Balancing Actions (WDBA) › Gasunie Transport Services

URL: https://www.gasunietransportservices.nl/en/shipper-trader/balancing-regime/balancing-actions-wdba

Balancing Actions (WDBA) › Gasunie Transport Services
Jump to content
Show menu
Close menu
At this page you can read more with regards to balancing actions in the TTF market area. A balancing action is performed on the ICE Endex Within-Day Market, known as the Within Day Balancing Action (WDBA).
This means that
GTS
will buy/sell
gas
for balancing actions on the ICE Endex
gas
exchange.
Gas
is delivered from the TTF to
GTS
, who then reallocates it to the causers.
If the end of the hourly prediction of the SBS exceeds the permissible limits, we will perform a balancing action. The purpose of a balancing action is to bring the SBS back to the
dark green zone
boundary.
The costs of the balancing action will be charged to the causers of the imbalance.
There are two types of products
GTS
can buy or sell. The product
GTS
buys or sells, depends on the value of the SBS forecast:
If a balancing action is performed in the
light green zone
GTS
will buy or sell end-of-day product. This means that
gas
is taken in/delivered in equal shares until the end of the with effect from 4 hours after the
hour
of the instruction. For example: a balancing action at 13:20 hours will result in
gas
being delivered from 17:00 hours to 06:00 hours.
If a balancing action is performed in the orange or red zones,
GTS
will buy the Next
Hour
product.
Gas
is then taken in/delivered in 1
hour
from the next
hour
following the instruction. For example: a balancing action at 13:20 hours will result in
gas
being delivered from 14:00 hours to 15:00 hours.
When is a balancing action performed?
If the SBS forecast is outside the
dark green zone
at 10 minutes past the
hour
, we send a first notification to the shippers (Gasport) and ICE Endex (request for quote).
If the SBS forecast is still outside the
dark green zone
at 15 minutes past the
hour
, we send a second notification to the shippers (Gasport) and ICE Endex (request for quote).
If the SBS forecast is still outside the
dark green zone
at 20 minutes past the
hour
,
GTS
will place a Market Order resulting in the buying or selling of
gas
on the ICE Endex within-day market.
Balancing actions take place at a randomly chosen time between 21 and 22 minutes after the top of the
hour
. The reason we changed this process can be found in the newsletter you can find below.
NB: We will not perform a balancing action in the
light green zone
if the (absolute numerical value of the) SBS forecast is equal to or less than the (absolute numerical value of the) SBS forecast of the past
hour
.
How will the buying or selling volume be determined?
The buying or selling volume is calculated based the difference between the SBS forecast at H:20 and the boundary value of the
dark green zone
.
Volumes are bought or sold in quantities of 1 MWh.
Balancing Actions
How is the balancing volume allocated to the causers?
If a balancing action is performed in the
light green zone
,
GTS
will buy or sell end-of-day product. This means that
gas
is taken in/delivered in equal shares until the end of the
gas day
with effect from 4 hours after the
hour
of the instruction. For example: a balancing action at 13:20 hours will result in
gas
being delivered from 17:00 hours to 06:00 hours.
If a balancing action is performed in the orange or red zones,
GTS
will buy the 1-
hour
product.
Gas
is then taken in/delivered in 1
hour
from the next
hour
following the instruction. For example: a balancing action at 13:20 hours will result in
gas
being delivered from 14:00 hours to 15:00 hours.
The
gas
that is delivered/received as a result of the balancing action described above is assigned pro rata to the causers, on the basis of the accountable POS of the
hour
of the instruction.
The price charged to the causers is the volume-weighted average price of the
gas
bought/sold.
Information exchange
The balancing action and the
distribution
of the
gas
bought/sold is an automated process. Parties who have a POS in the same direction as the SBS in the
hour
of the balancing action are considered to be causers. The causers will receive information about which part of the balancing action will be assigned to their POS and for which
hour
or hours. For example, a balancing action at 06:20 hours in the
light green zone
will result in a pro rata assignment to the causers of the volume bought/sold from 10:00 to 06:00 hours. The
causer
will be notified, the
Causer
Clearing
Confirmation
and the transactions will take place at the Bidladder Virtual Point. Invoicing will take place after the end of each month.
Below table shows an overview of all exchange actions and emergency calls over the past 31 days or the chosen month. You can view the time of the action,
hour
(s) of delivery, type of action, total volume transferred and price:
file-chart-line
Balancing actions
Use "Meer opties" to download
FAQ
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
How much gas does GTS call up when placing a WDBA?
The volume that must be called will be calculated as follows:
Difference between the anticipated final value of the SBS and the boundary value of the
dark green zone
.
The part that possibly is not yet delivered of a realized WDBA transaction is included in the determination of the volume of any new WDBA. This only applies for WDBA with the SBS in the light green area.
If the SBS is in the light-green zone, and the imbalance is less than the unbalance of the previous
hour
, no WDBA will take place.
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
This website requests your permission to use cookies for
YouTube
. Read our
cookie policy
for more information.
I agree
I don't agree