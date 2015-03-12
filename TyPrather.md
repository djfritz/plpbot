# Ty Prather #

http://timetunedin.files.wordpress.com/2008/11/office_stanley_0501.JPG?w=360&h=240

### Information ###

  * Year: Sophomore
  * Major: Electrical and Computer Engineering
  * Statement: Statement: My name is Ty and I am the Lead Code Designer of the Sensor Team.


### Ways to Contact Me ###

  * Email: Ty.Prather@okstate.edu
  * Phone: Ask and I can give it to you
  * In Person: Feel free to stop me in class or on campus if you need to talk

<a href='Hidden comment: 
* Text in *bold* or _italic_
* Headings, paragraphs, and lists
* Automatic links to other wiki pages
'></a>

### Reflections ###

Research:
-	Line sensor is composed of capacitors that are discharged based on the reflectance of the material under the sensor
  * By reading the sensor at a specific moment in time, we will be able to differentiate the reflectance of the white floor from the reflectance of the black tape.
-	Reflectance sensor will be connected via the GPIO
  * GPIO is interfaced by the tri-state register, and another register for interfacing with the GPIO blocks
  * Tri-state register sets whether each GPIO connection is an input or an output

Process:
-	Based on research, this is the proposed process for detecting and following a line
  * Set the tri-state register to set the GPIO to an output
  * Charge the capacitors through the GPIO
  * Set the tri-state register to set the GPIO to an input
  * Wait for the capacitors to discharge
  * Read value from capacitors
  * Process data

How to process data:
-	There are eight individual sensors providing eight data points
-	If the middle two sensors read 1s, then the line is in the middle
-	If the left side of the sensors read 1s, then the bot needs to make a left turn
-	If the right side of the sensors read 1s, then the bot needs to make a right turn
-	Should also have an “autocorrect” function so that if the bot gets slightly off the line, it is corrected back to center
  * If center lights and one to either side is lit, then the opposite side motor speed will be increased to push the robot back to center

Using process data: (Turning motors)
-	Motors are interfaced using the communication protocol found on the PLP Bot Wiki
-	Code will communicate to motors using UART code provided my the manual control team
-	Speed:
  * Will want robot to go reasonably fast, but not slow enough that imperfections in turning and fading by motors will not cause significant error.
  * Will want to stop robot before turn and turn slow enough that the robot does not overshoot the line
Initial Programming:
-	During writing the initial program, the code is not that complex. Basically just one big loop
  * $aX registers are used for memory locations
  * $sX registers are used for saved values
  * $tX registers are used for temporary values and are initialized right before they are used so if they are overwritten, they are re-initialized before they are used again
-	Program uses no timer, and no interrupts, but does use several waiting loops
-	Registers $t3 and $t4 are used with Branch-On-Equal and Add-Immediate statements to create an “improvised for-loop”
  * Used for charging, discharging, and reading capacitors
-	Because of troubleshooting problems and for ease of use, a debug function was also written so that the LEDs were lit according to the values from the sensor.

Problems Encountered:

Problem 1: Since we were using the GPIO, there was no way to simulate the program in PLP. We were unable to see the line sensor data in a resource like the CPU watcher so we had to come up with a way to view our data
-	Solution: The code was written so that the LEDs mirrored the values of the reflectance sensor so we could see what values were being given by the sensor

Problem 2: Upon seeing the data from the reflectance sensor, it was discovered that the sensor did not range from bits 0-7 in order, but instead the capacitors were scrambled, making data interpretation very difficult
-	Solution: Code was written by Wira and Fritz that unscrambled this data and placed the bits in order from left to right, mirroring the sensor

Problem 3: The sensor location on the bot
-	a) Because the sensor was not at the front of the bot. This caused the bot to not read a left turn until the center of the bot was at the turn instead of reading the turn as the front of the bot reached the turn.
  * Solution: To solve this problem, the code was written so that the bot reversed after a turn was sensed, then completed the turn.
-	b) Because the sensor was not centered left-to-right underneath the bot, the values of the motors for a left turn and for a right turn were slightly different
  * Solution: Through testing, we were able to determine how much of a difference was caused by this misalignment and adjust for it in programming




Problem 4: In the original thought process, the bot would quit turning after the line was sensed to be in the middle of the sensor again. This did not always work though because there is also a spot in the middle of the turn where the sensor could read as only the two center capacitors being charged, even though the turn was not completed.
-	Solution: Instead of completing a turn based on line location, the turns were programmed to be completed by a timer, then the autocorrect functionality would finish the turns

Problem 5: Because a timer was used to complete the turn, the time had to be very precise, even a few clock cycles could dramatically effect the position of the robot; but the more significant problem was the drain on the battery. As the battery drained, the motors were able to provide less power and weren’t able to complete the turn in the same amount of time as the motors on a full battery.
-	Solution: Unfortunately, we were unable to come up with a solution to this problem in time to integrate it into our final project.
-	Proposed Solution: In order to fix this issue, the best way that we came up with would be to combine the processes of turning by a timer, and turning by sensing the line and create a method that was able to turn the robot a significant amount to get past the first point that reads a line in the center, then use the autocorrect to finish the turn.

Changes in hindsight:
-	Would have rather used an optical sensor instead of a reflectance sensor to get more accurate data
-	Would have moved the sensor location on the robot to save time in coding and made the coding easier
-	Would have done more testing to see which kinds of turns were the best (i.e. 90-degree turns, or banking turns)

Final Discussion:
> In conclusion, the final result of the line sensor programming was a product that the sensor team was extremely satisfied with. It was intuitive by using the LEDs as a display for the data, it was simple and had no complex settings, and overall, it was effective. The robot was able to follow a straight line and make corrections as it drifted off the line, but in general it was unable to complete several turns in a row. One of the highlights of the project was downloading the code onto the robot for the first time, and after finding just one error in the code, the sensor was working on the first test in less than five minutes. The sensor team was proud to have a code that was robust and very quick to cycle. In the video provided on the sensor team wiki, one can see that there is no delay between the time that the sensor detects a change, and the time that it is updated on the LEDs. Even though there was a large amount of troubleshooting on the turning method it was very encouraging to have a base code that worked the first time, and worked well. If we were to redo this project and use the changes previously listed, there is no doubt that this robot would have had a line sensor that was able to accurately and effectively lead the bot through any course.


> - Ty Prather, Lead Code Designer