# SpotifyTeamProject

<h2>Project Description</h2>

<p>The Android Things Spotify Listener demonstrates how the mechanism of listening to music from raspberry works. Music comes from Spotify, both on laptop and telephone. The user should use either headphones or speakers. By means of a traffic light , we should see the intensity of the song volume. If the loudness is not disturbing for the user , the green led will flash, unless if it is in the disturbed listening mode the yellow led will flash otherwise it means that the volume is in a way hurting the ears of the listeners , the red led will flash.The led that flash changes depending on the volume</p>

<h2>Screenshots</h2>
<br><br>

<img src="media/Prezentare-Spotify.gif">

<h2>Schematics</h2>
<br><br>


<img src="media/rp2_pinout.png">
<p>I used pins number 7,8,25. 7 is for the green light, 8 for the yellow light and 25 for red light.</p>



<h2>R-requisites</h2>
<br>

<ul>
<li>
Android Things compatible board – Raspberry Pi model 3 B
</li>
<li>
The following individual components:

 - 2 coolers
 - 1 semaphore led
 - 1 breadboard
 - jumper wires
</li>
<li>PyCharm</li>
</ul>


<h2>Setup and Build</h2>

<p>To setup, follow these steps below.</p>

<ol>
<li>Ensure that the raspberry is plugged in</li>
<li>Connect the computer to the same network as the raspberry</li>
<li>Establish a connection between computer and Raspberry OS through putty</li>
<li>Transfer your files from your OS to raspberry(if you are using Windows you can use WinSCP)teams</li>
</ol>



<br>
<h2>Running</h2>

<p>In order to run the app you have to follow these steps:</p>

<ol>
<li>Connect the breadboard to the raspberry through jump wires which have to be on the same road as the jump wires from semaphore led</li>

<li>Run the application with the following command sudo python “VolumeProjectSemaphore.py”</li>
<li>Press the button to see the result</li>
<li>
Enjoy :smirk:
</li>
</ol>
