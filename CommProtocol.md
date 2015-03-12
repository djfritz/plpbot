# Motor Control - PLP Board #

PLPBot uses the Simple Serial control to drive the 4 motors on the MMP-5 with 9600 baud rate. The format for this interface is as follows (per [MMP-5 manual](http://www.themachinelab.com/mmp5/PDFs/MMP58User%20Guide%20NiCad.pdf)):

  * One byte packets.
  * Sending a number from 1 to 127 controls left motors, with 64 being stop, 1 full reverse, and 127 full forward.
  * Sending a number from 128 to 255 controls right motors, with 192 being stop, 128 full reverse, and 255 full forward.
  * Sending 0 is an exception that will stop both motors.
  * The controller latches the values for each set of motors.

This scheme carries over all the way to the Input Station (driver's console).

# PLP Board - Base station #

The packet structure for the base station and on-board PLP system communication use the scheme from Motor Control section with the addition of a start byte, with 9600 baud rate over XBee link. The Base station is a dumb repeater, it checks the start byte of the incoming packet (0x7F), and then it forwards the start byte and the values for the two sets of motors to PLP Board via XBee if the start byte was valid.

# Base station - Driver's Console #

The Driver's Console sends a 3-byte packet every 10ms over an internet connection (Socket interface port 1337). The packet structure is as follows:

  * Start byte 0x7F
  * Value for motor set left (1-127), or 0 if the driver hit the panic button
  * Value for motor set right (128-255), or 0, as above

  * The robot returns the character 'f' (0x66) on every properly received packet. The basestation forwards this to the client driver. In this manner, the client driver can receive feedback on the packet latency and overall communication health of the robot.

The Base station acts as the server in this simple client/server setup.