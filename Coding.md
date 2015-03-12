Below are our different programs for the various subsections of the Sensor part of the PLPBot project.

Throughout the programs, you might see comments about how we are coding and why we are coding different aspect of each program.

The following lines of code are temporarily finalized. While we test, if we find any line of code is either incorrect or could be more efficient, we will update the necessary code immediately.

All of the following code uses the plp library for writing to the uart, timer, seven segment, and motor values.



<a href='Hidden comment: 
The above code is used for the Table of Contents
'></a>


# Line Following Program #
```
# main source file

.org 0x10000000

#This is some space for global variables

header:
	.word 0x00000000


initial:

	li $sp, 0x10fffffc
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
	
manual:	

	li $a0, 0x02020202
	jal libplp_sseg_write
	nop
	
	jal libplp_uart_readxb
	nop
	
	#Returns to main if the value is too small
	li $t0, 0xf7
	beq $v0, $t0, LineFollowing_Begin
	nop

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
	push $a0		# push the left motor value 


	#Right motor
	jal libplp_uart_readxb
	nop
	move $s1, $v0

	move $a0, $v0
	jal libplp_uart_write
	nop
	push $a0		# push the right motor value 

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

   dontsendthatrightmotorvalue:

	j initial
	nop

isr:
	move $a0, $zero
	jal libplp_uart_writebot
	nop		

	li $a0, 0x01010101
	jal libplp_sseg_write
	nop

	li $a0, 4292467296
	jal libplp_timer_write
	nop

isr_return:


	#reenable interrupts
	li $t0, 0xf0700000
	li $t1, 3
	sw $zero, 4($t0)
	
	j manual
	sw $t1, 0($t0)


```


# Speed Calculating Program #
```
# main source file
# Title: Speed Calculation
# Project Team: Sensor Team
# Developers: Richard Yang, Zamani Khumalo
# Date: November 2011
#
# Description:
# Calcutating the speed of a bot using the value of sensors on each wheel.
# 
# Assumptions:
# Processed after an interrupt occurs (specifed sampling time) 
# Scope is to store the number of ticks between each interrupt
# Initially the previous sample is zero
#
# Registers:
# $s0 : Current Sample 
# $s1 : Previous Sample 
# $s2 : Send Data
# $s3 : Time of sample
# $s4 : Increment
.org 0x10000000


loop:
li $t3, 0xf0100000 #load values for the switches
lw $s0, 0($t3)
li $t5, 0b10000000
slt $t5, $s0, $t5  #check if the value is less than specified value
beq $t5, $zero, moter_127 # if its not jump to set the speed
li $t5, 0b01000000
slt $t5, $s0, $t5
beq $t5, $zero, moter_119
li $t5, 0b00100000
slt $t5, $s0, $t5
beq $t5, $zero, moter_111
li $t5, 0b00010000
slt $t5, $s0, $t5
beq $t5, $zero, moter_103
li $t5, 0b00001000
slt $t5, $s0, $t5
beq $t5, $zero, moter_95
li $t5, 0b00000100
slt $t5, $s0, $t5
beq $t5, $zero, moter_87
li $t5, 0b00000010
slt $t5, $s0, $t5
beq $t5, $zero, moter_79
li $t5, 0b0000001
slt $t5, $s0, $t5
beq $t5, $zero, moter_71


moter_64:

li $a0, 64
jal libplp_uart_writebot
nop
j loop
nop

moter_71:
li $a0, 71
jal libplp_uart_writebot
nop
j count_time
nop

moter_79:
li $a0, 79
jal libplp_uart_writebot
nop
j count_time
nop

moter_87:
li $a0, 87
jal libplp_uart_writebot
nop
j count_time
nop

moter_95:
li $a0, 95
jal libplp_uart_writebot
nop
j count_time
nop

moter_103:
li $a0, 103
jal libplp_uart_writebot
nop
j count_time
nop

moter_111:
li $a0, 111
jal libplp_uart_writebot
nop
j count_time
nop

moter_119:
li $a0, 119
jal libplp_uart_writebot
nop
j count_time
nop

moter_127:
li $a0, 127
jal libplp_uart_writebot
nop
j count_time
nop

count_time:
li $a0, 0xffd9da60  # interrupt time 10ms
jal libplp_timer_write
nop
li $i0, wheel_sensor_loop
#enable interrupts
li $t0, 0xf0700000
li $t1, 15
sw $zero, 4($t0)
sw $t1, 0($t0)
# $i0 is where the code will go to when an interrupt occurs
# it holds a location in memory
waiting_for_interrupt:

	nop

	j waiting_for_interrupt
	nop
	


wheel_sensor_loop:


#check the time of time between 0~5
#check the lowest limit
initial_time_of_sample_1:
li $t2, 0
slt $t2, $s3, $t2
bne $t2, $zero, initial_time_of_sample #if t1<0, reset the value, if t1>=0, go to check the highest limit
nop
#check the highest limit
initial_time_of_sample_2:
li $t2, 5
slt $t2, $s3, $t2
bne $t2, $zero, add_one #if t1<5(also t1<=4), set the value
nop

#if value is abnormal,set the values
initial_time_of_sample:
li $s3, 0
li $s4, 0
li $s1, 0
li $s2, 0
j initial_time_of_sample_1
nop
# t1=t1+1,time of sample + 1
add_one:
addiu $s3, $s3, 0b01



#sample and store current sample
store_current_sample:
#li $a0, 100000
#jal libplp_timer_wait
#nop
li $s0, 0xf0300008  #0xf0100000
lw $t0, 0($s0)


#Branch to set_previous if the current sample is the same value as the previous sample
lw $t1, 0($s1)
beq $t0, $t1, set_previous
nop
# process the tick by incrementing by one 
addiu $s4,$s4, 1
set_previous:
# set previous sample = current sample
move $t1, $s0
sw $t1, 0($s1)


#check the time of sample
check_time_of_sample:
li $t0, 5
move $t1, $s3
bne $t1, $t0, loop
nop

#if 5 times, send data and refresh
send_data:
move $t1, $s4
sw $zero, 0($s3)
sw $zero, 0($s4)
li $t3, 0xf0200000
sw $t1, 0($t3)


j loop
nop

```

# Tick Counter #

```

# test tick sensor

.org 0x10000000
initialize:
	li $sp, 0xf000000

loop:

li $t3, 0xf0100000 #load values for the switches
lw $s0, 0($t3)
li $t5, 0b10000000
slt $t5, $s0, $t5  #check if the value is less than specified value
beq $t5, $zero, moter_127 # if its not jump to set the speed
li $t5, 0b01000000
slt $t5, $s0, $t5
beq $t5, $zero, moter_119
li $t5, 0b00100000
slt $t5, $s0, $t5
beq $t5, $zero, moter_111
li $t5, 0b00010000
slt $t5, $s0, $t5
beq $t5, $zero, moter_103
li $t5, 0b00001000
slt $t5, $s0, $t5
beq $t5, $zero, moter_95
li $t5, 0b00000100
slt $t5, $s0, $t5
beq $t5, $zero, moter_87
li $t5, 0b00000010
slt $t5, $s0, $t5
beq $t5, $zero, moter_79
li $t5, 0b0000001
slt $t5, $s0, $t5
beq $t5, $zero, moter_71


moter_64:

li $a0, 64
jal libplp_uart_writebot
nop
j loop
nop

moter_71:
li $a0, 71
jal libplp_uart_writebot
nop
j store_current_sample
nop

moter_79:
li $a0, 79
jal libplp_uart_writebot
nop
j store_current_sample
nop

moter_87:
li $a0, 87
jal libplp_uart_writebot
nop
j store_current_sample
nop

moter_95:
li $a0, 95
jal libplp_uart_writebot
nop
j store_current_sample
nop

moter_103:
li $a0, 103
jal libplp_uart_writebot
nop
j store_current_sample
nop

moter_111:
li $a0, 111
jal libplp_uart_writebot
nop
j store_current_sample
nop

moter_119:
li $a0, 119
jal libplp_uart_writebot
nop
j store_current_sample
nop

moter_127:
li $a0, 127
jal libplp_uart_writebot
nop
j store_current_sample
nop



#sample and store current sample
store_current_sample:
li $a0, 100000
jal libplp_timer_wait
nop
li $t6, 0xf0300008
lw $s0, 0($t6)

#Branch to set_previous if the current sample is the same value as the previous sample
beq $s0, $s1, set_previous
 nop
# process the tick by incrementing by one 
addiu $t8,$t8, 1


set_previous:
# set previous sample = current sample
lw $s1, 0($t6)
li $t3, 0xf0200000
sw $t8, 0($t3)
nop
j loop

```