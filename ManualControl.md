# Manual Control Team #

http://dl.dropbox.com/u/47218867/Stuff%20added%20to%20Wiki/PLPBot.JPG

## Members ##

|Team Member| Role|
|:----------|:----|
| Bo Bittle | Project Manager|
| Zach Smith | Lead Engineer|
| Lucas Kinion | Documentation Expert|
| Nolan Replogle | Team Mascot |

## Project Summary ##
Our project, as a whole class, is to program a robot using PLP so that it can complete an obstacle course. The course contains a manual control portion, a portion where the robot uses sensors to follow a line along the track with no user input, and then a portion where it plays back all the movements of the previous two sections to get back to the beginning on its own.

The class is split up into four teams: Base Station, Manual Control, Sensors, and Autonomous. Our group is the Manual Control team.

## What we do ##

Our team is in charge of the manual control portion of the PLP Bot obstacle course. Our responsibilities include:

  * Receiving data from the controller through the XBee
  * Checking the data to make sure it hasn't been corrupted
  * Manipulating the data we receive and using it to control the motors
  * Reading the bot's current speed
  * Sending back the current speed to the controller to be displayed

## Additional Hardware Info ##

The robot uses a Nexys 2 FPGA board to process the information it needs to drive. It has some additional hardware, though, including motors, XBee, reflective sensors, and a rotary encoder.

| Component | Memory Location |
|:----------|:----------------|
| XBee | 0xf0b00000 |
| Motors | 0xf0c00000 |
| Sensors | 0xf0300000 |

The XBee is a component that sends 1 byte at a time over radio waves to communicate with the other XBee on the base station. It has a range of around 100 feet before the reception starts dropping off. It is used in the exact same way as UART, but with a different memory address.

The motors are also addressed in the same way as UART. The speed values as readable by the motors are as follows:
| **Direction** | **Left Motor** | **Right Motor** |
|:--------------|:---------------|:----------------|
| Reverse | 1 - 63 | 129 - 191`*` |
| Stop | 64 | 92 |
| Forward | 65 - 127 | 193 - 255 |

`*` 128 is technically full reverse on the right motor, but for symmetry's sake, we ignore that value.

## Flowchart ##

![http://i.imgur.com/HEebg.png](http://i.imgur.com/HEebg.png)

## Data Protocol ##

The robot is going to receive 4-byte packets from the controller, formatted as follows: **0xMO\_LM\_RM\_CS**

  * **MO** = Mode
    * FF for Manual Control
    * F7 for Sensor Control
    * F2 for Autonomous
  * **LM** = Left Motor
    * Value between 0 and 127
    * This value is already formatted to be sent to the motor
  * **RM** = Right Motor
    * The value we receive is between 0 and 127
    * We add 128 to that value so that it can be sent to the motor also
    * The reason we have the base station send us the actual value minus 128 is to differentiate between a mode byte and a motor byte. This way, the mode byte is the only one that's over 128, so we can easily check and see how big our first byte is to see if it's actually the beginning of a packet.
  * **CS** = Checksum
    * Checksum contains the total number of 1's in the previous 3 bytes, as sent
    * We will sum up the 1's and compare that summation to the checksum
    * If the checksum is incorrect, our data is corrupted and we go into Loss of Signal mode


## Algorithm ##

The first thing we do is receive a byte of data from home base. The first bit should be the mode, so we check to see what that byte is. If it's FF, we continue on to check the second bit. If it's F2 or F7, we jump off to the section of code for that given mode. If it's anything else, we assume it's bad data and indicate loss of signal, shut off the motors, and wait for new data.

After receiving and confirming the first byte, we take in the second, third, and fourth bytes in order. We store all 4 bytes in different registers to use later.

After we have all 4 bytes saved, we check the checksum. The checksum is generated on the home base's end by counting up the number of 1's in the first 3 bytes of their packet and adding that number up to make up the fourth byte. We do the same thing with the first 3 bytes we receive, and compare it to their checksum to make sure we're getting the data properly. If not, we indicate loss of signal, turn off the motors, and wait for new data. If so, we go ahead and send our motor data to the motors.

When it comes to writing the motor data, we send the left motor directly as we received it. We then add 128 to the right motor value and send it as well.

So for example, the person at the controls wants us to spin in a circle to the left. That means we want the left motor to go full forward and the right motor to go full reverse, which means sending a 127 and a 129 (0x7F and 0x81) to the motors. The packet the controller team sends us would be **0xFF\_7F\_01\_10**.  The 0x10 (or decimal 16) is the checksum, which is the summation of the number of 1's in the first 3 bytes. We would sum that up in the first 3 bytes and compare it to that 0x10 and confirm that the packet was correct before doing anything else. We would then send the 0x7F for the left motor to the motor address without manipulating it, then add 128 (or 0x80) to the right motor value before sending it.

## Code ##
Under construction

```
# main source file

.org 0x10000000

#This is some space for global variables

li $sp, 0x10fffffc
header:
	.word 0x00000000

# initial sets up interrupts for the timer, and initializes the timer 50ms from overflow for LOS purposes
initial:

	#set up the interrupts
	li $i0, isr

	#enable interrupts
	li $t0, 0xf0700000
	li $t1, 3
	sw $zero, 4($t0)
	sw $t1, 0($t0)

	li $a0, 4292467296
	jal libplp_timer_write
	nop
	
# manual is our main loop. it reads data from the xbee then checks the mode and either leaves if it's in another mode or continues
# to read in and send motor values along with various checks and things
manual:	


	jal libplp_uart_readxb
	nop
	
	li $a0, 0x01010101
	jal libplp_sseg_write
	nop


	li $t0, 0xf7
	beq $v0, $t0, LineFollowing_Begin	# if mode is f7, jump off to source file with sensor team's code
	nop
	li $t0, 0xf2	
	beq $v0, $t0, Autonomous_wait_start	# if mode is f2, jump off to source file with autonomous team's code
	nop

	#Returns to main if the value is too small
	li $t0, 0x80
	slt $t1, $t0, $v0
	beq $zero, $t1, manual
	nop
	
	#storing the value of the header
	li $t0, header
	sw $v0, 0($t0)


	move $a0, $v0
	jal libplp_uart_write
	nop

	#Left motor
	jal libplp_uart_readxb
	nop
	move $s0, $v0

	move $a0, $v0
	jal libplp_uart_write
	nop
	push $a0			# push the left motor value for aaron


	#Right motor
	jal libplp_uart_readxb
	nop
	move $s1, $v0

	move $a0, $v0
	jal libplp_uart_write
	nop
	push $a0			# push the right motor value for aaron


	#Check sum
	jal libplp_uart_readxb
	nop
	move $s2, $v0

	move $a0, $v0
	jal libplp_uart_write
	nop

	# Writing the left
	move $a0, $s0
	jal libplp_uart_writebot
	nop
	li $t0, 0xf0200000



	sw $a0, 0($t0)
	
	# Writing the right motor
	li $t0, 128
	beq $s1, $zero, dontsendthatrightmotorvalue
	nop
	addu $a0, $s1, $t0
	jal libplp_uart_writebot
	nop

   # it goes here if the e-brake is on, which makes the right motor value 0, so we don't want to add 128 and send it
   dontsendthatrightmotorvalue:



	j initial
	nop

# if the timer overflows, it goes here where we stop the motors, display loss of signal, reset the timer, and wait for more data
isr:
	move $a0, $zero
	jal libplp_uart_writebot
	nop		

	move $a0, $zero
	jal libplp_sseg_write
	nop

	li $a0, 4292467296
	jal libplp_timer_write
	nop

# this just reenables interrupts before jumping back to the main loop
isr_return:


	#reenable interrupts
	li $t0, 0xf0700000
	li $t1, 3
	sw $zero, 4($t0)
	
	j manual
	sw $t1, 0($t0)
```