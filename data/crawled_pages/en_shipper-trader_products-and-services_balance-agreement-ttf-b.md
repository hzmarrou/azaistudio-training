# Balance Agreement (TTF-B) › Gasunie Transport Services

URL: https://www.gasunietransportservices.nl/en/shipper-trader/products-and-services/balance-agreement-ttf-b#skip-to-content

Balance Agreement (TTF-B) › Gasunie Transport Services
Jump to content
Show menu
Close menu
In case a
shipper
transports
gas
to domestic physical network points, he has the possibility to transfer (a part of) his imbalance risk to another
shipper
. To realize this he must enter in a Balance Agreement with another
shipper
.
In a balance agreement the balance-receiving
shipper
and balance-supplying
shipper
agree that a certain amount of
gas
is transferred at the virtual trading point TTF-B (301411), a network point created for this purpose. The exact amount is calculated afterwards on the basis of allocations of the balance-receiving
shipper
.
Shippers can enter into a balance agreement for one or more specified
user
categories (G1A, G2A, G2C, GXX, GVV and starting 1-1-2018 also GIN and GIS) of the balance-receiving
shipper
. The balance-receiving
shipper
will stay unchanged mentioned as PV is the
connection
registers of the
transmission
operators. For different categories different agreements can be made. It is also possible to have just a selection of
user
categories in the balance agreement. However it is not possible to include individual customers into the balance agreement.
Different types of balance agreements
Percentage-balance: the balance-supplying
shipper
supplies
gas
up to a agreed percentage of the physical offtake of the balance-receiving
shipper
per
user category
.
Max-balance: the allocated amount of
gas
on the TTF-B network point between the balance-supplying
shipper
and the balance-receiving
shipper
has an on beforehand specified upper limit.
Min-balance: the allocated amount of
gas
on the TTF-B network point between the balance-supplying
shipper
and the balance-receiving
shipper
has an on beforehand specified lower limit.
It is possible to combine different types, however the combination of a percentage and a fixed lower limit is not possible.
Programs, Nominations, Confirmations en Allocations
The balance agreement between shippers must be effectuated by means of sending a specific
nomination
message BALDOC to
GTS
in which both parties scope the balance agreement.
Nomination
:
Nomination
message BALDOC can be send up to 400 days in advance, although shippers can choose to nominate on a monthly or daily basis. It is allowed to include several consecutive days or months in one message. The first day in the message has to be in the future since within day nominations are not allowed for balance agreements. It is not an obligation that both shippers in the agreement have the same
nomination
pattern, because matching will be performed on a daily basis applying the Zero-Rule, notwithstanding the Lesser-Rule that applies on the TTF. The
confirmation
will get the status “settled” when both nominations contain the same information.
NRT-process:
The balance-supplying
shipper
receives near real-time information about the aggregated exit
portfolio
insofar as the scope of the balance agreement goes. This information is shared, amongst others, in Gasport (or via B2B) per
user category
. The realized amounts of the balance-supplying
shipper
will be treated as exit allocations. For the balance-receiving
shipper
these realizations will be treated as entry allocations, all data will be presented in GasPort (or B2B).
Offline allocation process:
The offline allocations for the TTF balance agreements are calculated at the moment that a complete set of offline allocations for the balance-receiving
shipper
is available. If a difference occurs between the NRT and offline date the settlement invoice will be used to settle the differences.
Program:
The balance-supplying
shipper
specifies the total of his balance agreements in his
exit programme
PRODOC. There must be a split between protected users and others  in accordance with his own physical exit (GSTPPUB for protected users and GSTPOTHERB for other
user
categories).
This website requests your permission to use cookies for
YouTube
. Read our
cookie policy
for more information.
I agree
I don't agree