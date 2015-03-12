# Zamani Khumalo #

### Information ###

![http://blog.earnmydegree.com/wp-content/uploads/2009/01/michael_scott2.jpg](http://blog.earnmydegree.com/wp-content/uploads/2009/01/michael_scott2.jpg)

Year: Junior

Statement: I am an Industrial Engineering major and am the Project Manager of the Sensor Team.


### Ways to Contact Me ###

  * Email: zamani@okstate.edu
  * Phone: Ask and I can give it to you
  * In Person: Feel free to stop me in class or on campus if you need to talk

<a href='Hidden comment: 
* Text in *bold* or _italic_
* Headings, paragraphs, and lists
* Automatic links to other wiki pages
'></a>

### Reflections ###

**_Reflection on PLP_**

PLP is the first tool that I have used to simulate interactions with
hardware. It was very difficult to understand at the beginning because
it was so foreign and barebones compared to other programming
languages. The first few labs did set the tone for the course but I
feel we could have had more emphasis on being taught the functions in
class and in lab. Very detailed notes with posted step by step examples
to solve a number of problems should be posted. Understanding the
fundamental of each operation was no emphasized and I feel that needs
to change in the future. Setting online quizzes on different operations
and what they mean can provide real time information on who in the
class actually understands what is being done.

I believe PLP is a great tool with a bright promise; the one thing that
needs to be established is small pieces of useful code. I only really
stared to grasp the full understanding and powerful capabilities in the
last two weeks of the project. I was able to look at code and
understand exactly what was happening and what needed to be done. I
feel very comfortable in PLP and I will probably use it in the future.
I was really happy to see my code communicate the way I had planned
with the hardware components. The PLP tool has provided the connection
between software and hardware; previously I only knew the theory now I
understand exactly how it works. It has given me more confidence in
selecting the right equipment needed to complete a specific operation.

**_Reflection on Assembly Language Programming_**

Learning how to program in assembly language has provided me with
fundamental knowledge on how information is processed. I have found
that my ability to program in higher level languages has improved
greatly because of the amount of detail I go through before deciding
which function to use or create. I analyze the process from start to
finish and ask critical questions like, “What will the processor be
doing here?” “Can I use my memory more effectively?” “Can I reduce the
number of variables?” “Can I be more efficient and use less power?” I
spend a great amount of time comparing my code to what the physical
hardware operations will be. Using a coding style that simulates jumps,
interrupts and loops more effectively because I know how that
information will be processed from a fundamental level. It’s a great
way to understand the world and information in general; it’s just 1’s
and 0’s at the end of the day. The developer’s interpretation of those
variables constitutes information; a data set of 1’s and 0’s can
represent multiple sets of information. This has radically changed my
strategies on producing informative systems in an enterprise
environment.

**_Reflection on Collaborative Teamwork_**

The collaborative aspect of this course was beneficial in providing a
simulated engineering design environment. I was able to apply some of
the skills and techniques learned from previous industrial engineering
classes to this class. It also provided extra insight into group
behavior and the engineering development cycle. At the start of the
project it was not difficult to establish a plan of action as we have
all experienced working in groups in previous engineering classes. One
of the critical points we emphasized was having effective meetings and
planning sessions. Great emphasis was placed on planning and producing
a reliable schedule and plan of action assigning people to various
activities and roles. Once roles were assigned the group was able to
start planning and testing their ideas using the PLP Tool.

A majority of the discussions and assumptions where made based on the
intensive research done on the PLP Bot and sensors. Research was
conducted by all the member of the team and we used a variety of
websites and took a hard look at the capabilities of all the hardware
components. When the team developed a working model based on the
initial assumptions and attempted to implement them on the PLP Bot we
found a number of problems.


The first problem was identifying what went wrong and if the problems
were due to programming syntax errors or logical errors. Once we
established that the majority of the problems were logic errors we
attempt to find the source of the errors. The initial errors that we
found with the distance sensor were the following:

  * The initial assumption that a perfect square wave would be produced
by the sensor was not true. This was the foundation of the speed
calculation and was the most important assumption.
  * The sensor actually has some amount of noise when no object was
detected, the exact amount is unknown and as a result the speed
calculations needed to change.


We attempted to tackle the problem from multiple directions, the first
direction was to create a more controllable sampling routine using an
interrupt as opposed to waiting. This enabled the team to sample at a
very specific point in time. The problem that came up was that even
with the modification of the sample rate we were not able to skip or
identify the noise areas.

The next we attempted to tackle the problem by looking at the frequency
responses from the noise itself such that we can see it on the LED’s
and verify if it changes. The team spent hours trying to analyze the
responses and the best model we made was able to obtain a pulse that
matched the speed of the bot, that pulse would repeat faster and faster
as the bot increased in speed. The team ran out of time before we were
able to capture that information in a useable manner and integrate it
into the systems itself. The problem solving process and working with
other team members was a great learning experience.

I have personally leaned the benefit to working in a collaborative
environment with individuals with the same mind set and set of
objectives. We were able to learn from each other and even when things
went wrong we would come together and help each other. It was
enormously frustrating when the logic works on the simulator but not on
the hardware. Sharing one robot amongst a number of teams each with
different sets of objectives to test was difficult. The team managed to
share the BOT in an effective manner ad would work with each other on
other sections. I found myself troubleshooting various processes and
loops in other sections and also having them come assist me with my own
work. There was a very effective supportive team where we always asked
questions and helped each other.

> - Zamani Khumalo, Project Manager