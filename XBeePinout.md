The Xbee modules don't match up correctly to the FPGA boards, so we've had to make a wiring harness to correct this problem.

| harness pin | xbee pin |
|:------------|:---------|
| 1 | 5v VDC |
| 2 | GND |
| 3 | dout (FROM XBEE TO MCU) |
| 4 | din  (FROM MCU TO XBEE) |

The XBEE modules are connected to the top row of JB, as shown below.

![http://plpbot.googlecode.com/hg/images/xbee.jpg](http://plpbot.googlecode.com/hg/images/xbee.jpg)