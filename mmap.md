# Memory Map Additions #

The memory map from the vanilla PLP tree has two additions.

  * 0xf0b00000 - XBee UART
  * 0xf0c00000 - Motor UART

Both are standard UART blocks, just like the vanilla UART mapped at 0xf0000000. The only difference is that both of the XBee and Motor UARTs are 9600 baud.