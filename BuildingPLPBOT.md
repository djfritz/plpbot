# Introduction #

PLPBot is a mix of off the shelf, manufactured, and soft (verilog) components. The robot platform itself is the Machine Labs MMP-5, which comes with a simple serial motor control interface. The control circuitry is based on the Progressive Learning Platform (PLP), with some modifications such as additional UARTs. Wireless communication is accomplished via Xbee modules to a base station, where a Java control interface picks up the rest. An Axis wireless camera provides the video stream, which is embedded in the control software.

The robot platform provides a 12Vdc power system, which is stepped down to 5Vdc via a buck boost regulator. The power regulator circuit was manufactured in house.

The Xbee modules have platform boards they are mounted to, which were also manufactured in house.

## Building the PLP hardware ##

See the [PLP](http://plp.okstate.edu) website for information on building the PLP system.

PLPBot is a patch to the PLP system. You can clone the PLP repository and apply the PLPBot patch, and build from there. A simple script is provided in the `hw` directory to automate this process. To build PLPBot, you'll need mercurial, python, and the Xilinx Webpack.

## Manufactured Components ##