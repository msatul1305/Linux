FIX - Financial Information Exchange protocol
It is a vendor neutral electronic communications protocol for international real time exchange of securities transaction information.
Used for pre trade, post trade and trade communication.

Fix architecture

2 layers:
1. Session layer: Initialization(Handshaking), maintenance and termination of connection => For high performance
2. Application layer: Order creation, cancellation, replacement and so on. => Business specific functions

Message Structure

-> Text only

Field definition contains->
1. Name
2. Number
3. Data type
4. Value

Message structure
eg. 

8=FIX.4.4 | 9=176 | 35=8 | 49=PHLX| 56=PERS | 52=20071123-05:30:00.000 | 11=ATOMNOCCC9990900 | 20=3 | 150=E | 39=E| 55=MSFT | 167=CS | 54=1 | 38=15| 40=2 | 44=15 | 58=PHLX EQUITY TESTING | 59=0 | 47=C | 32=0 | 31=0 | 151=15 | 14=0 | 6=0 | 10=128 |


8=FIX.4.4|9=110|35=D|34=3|49=CLIENT|52=20190424-11:19:16.885|56=SERVER|11=ID|21=3|40=1|54=1|55=EUR/USD|60=20190424-11:19:16.885|10=54|


FIX Message components: 
1. Standard header
2. Message body
3. Standard trailer

1. **Standard header**
  8 - BeginString
  9 - BodyLength
  35 - MsgType => eg. Cancelling Order, Placing order etc.
  49 - SenderCompID
  56 - TargetCompID
  34 - MsgSeqNum
  52 - SendingTime
  
  
2. Message body
  message sent by application
  
3. Trailer
  **key = 10**, value = checksum
  checksum = sum of message upto but not including (from 8 = FIX to 6 = 0 |)%128
  
8=FIX.4.4|9=110|35=D|34=3|49=CLIENT|52=20190424-11:19:16.885|56=SERVER|11=ID|21=3|40=1|54=1|55=EUR/USD|60=20190424-11:19:16.885|10=54|

D => Order Single 
34 - MsgSeqNum = 3
11 - ClOrdID
21 - Handllnst = 3 => Manual Order
40 - OrdType - 1 => Market
54 - side - 1 => BUY
55 - Symbol
60 - TransactTime




