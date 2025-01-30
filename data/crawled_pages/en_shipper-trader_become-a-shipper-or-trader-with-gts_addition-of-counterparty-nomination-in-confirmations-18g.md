# Addition of counterparty nomination in confirmations (18G) › Gasunie Transport Services

URL: https://www.gasunietransportservices.nl/en/shipper-trader/become-a-shipper-or-trader-with-gts/addition-of-counterparty-nomination-in-confirmations-18g#skip-to-content

Addition of counterparty nomination in confirmations (18G) › Gasunie Transport Services
Jump to content
Show menu
Close menu
At virtual network points, it is compulsory in Edig@s version 5.1 and also in Edig@s version 6.1 to include the (original)
nomination
of the counterparty in the
confirmation
(NOMRES) messages, alongside the actual
confirmation
. The codes used in the NOMRES message indicate the meaning:
16G: confirmed values to
shipper
18G: nominated values by counterparty
During the first implementation (back then in version 5.1) the flow direction for the 18G functionality was unclear for a long time. Eventually, in consultation with the Edig@s working group, the following was decided and implemented as such.
Please note that there is a difference in the direction between Edig@s version 5.1 and Edig@s version 6.1 in terms of flow direction for the 18G values.
For Edig@s version 5.1, for 18G the flow direction of counterparty nominations is equal to the flow direction of the
shipper
confirmation
for both entry (Z02) and exit (Z03). The figure below shows an example of the version 5.1 TTF Edig@s message with the 18G functionality included.
For Edig@s version 6.1, the flow direction for 18G has been changed and made equal to the flow direction of the submitted
nomination
by the counterparty. In other words, the flow direction of the nominated values for the counterparty (18G) are now opposite to the flow direction of the confirmed values of the
shipper
(16G). This applies to both entry (Z02) and exit (Z03) values. The figure below shows an example of the version 6.1 TTF Edig@s message with the 18G functionality included.
This website requests your permission to use cookies for
YouTube
. Read our
cookie policy
for more information.
I agree
I don't agree