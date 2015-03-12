# Robot Control Interface #

PLPBOT has a very simple serial control interface that is connected to the S0 port on the robot and the JA1 port on the PLP board. It consists of a simple 9600, 8N1 serial interface, with no feedback.

There are four motors on PLPBOT, but only two motor control signals. This is because both left motors are synchronous, as are both right motors. Motor control is via a single byte sent to the robot. The byte is split into two ranges, as shown in the table below.

| Data | Action |
|:-----|:-------|
| 1-63 | Left motors reverse (1 is fastest) |
| 64 | Left motors stop |
| 65-127 | Left motors forward (127 is fastest) |
| 128-191 | Right motors reverse (128 is fastest) |
| 192 | Right motors stop |
| 193-255 | Right motors forward (255 is fastest) |
| 0 | All stop |

Values are latched until another command is received.