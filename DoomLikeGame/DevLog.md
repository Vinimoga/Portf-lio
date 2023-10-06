2023:

0917 -

0919 - Today I've started venturing out about the 
raycast functions. They are a bit complicated but 
I'm trying to figure it out. I'have found another
but with me FAKEWIDTH and FAKEHEIGHT, becouse
they weren't in all the player assets, only on 
the map ones, it made the player be shown in 
another location but their coordinates be in 
another tile. After putting all the values on the 
player, it worked flawlessly, but I really had to 
figure It out. It has been an adventure until now,
I expect that this project takes some time before 
I really say it is 'finished'. I'm not thinking in
making a pretty big game, only something I cass 
take some time off college and into programming.

0927 - Started doing the engine of the game
(raycasting and stuff), it's been one week since I
did something in the game, better do more.

0929 - I've tried solving more about the raycasting 
function, but something is on my nerve. On the 
beggining i've tried doing it on a "changable" frame,
but this idea doesn't work if the entire game doesn't
work, so I am trashing it out to biuld again from a
squared resolution and a change it latter. A squared
map will be implemented too.

This is super hard

1003 - Finally the raycasting did work, what I did 
wrong was the raycasting function was searching for 
every occurrence of a ray passing through a wall, 
that cause a wall do be seen, but the wall behind 
also was passed through (because of the max depth),
that made two rays, one inside the other. Now i'll
try to make the rest of the game from the first 
tutorial, then i'll try to implement a different
type o raycasting, called a Digital Differential 
Analyzer (DDA). I'll see this again later. 

1004 - Today I braced miself to do the DDA part.
It is acctually not that hard. The way it works 
is tracing a ray to intercept the horizontal 
lines and the vertical lines, witch is the closest
one is where the ray 'hits' the wall. The problem 
arrives in exacly intercepting, becouse depending 
on the angle, the first part of the tile the ray 
is gonna hit is the top side, the botton side, so
you need to see with angle are you at to define 
where can it get, and then compare the results.

1005 - My error on the raycasting algoritmm was
literally a tiny number you should be subtracting
for it to work. I don't know why, this is what 
the internet told me. So now it is working huh...

the rest of the day I tried the pseudo 3D, so 
bear with me.
Apparently the pseudo 3D is very, basically 2 
lines of code.

1006 - Today I started experimenting with the 
expansion of the map and changes in the color
and lighting in the game. Also, I tried adding
object rendering, but it failed, I'll try it 
again later, for now I'll try to make the game
more absurd with the map creation.
I discovered that you can go out of bounds. 
This has been a good experience, because I'm 
feeling extra happy. Now that my college have
entered a strike i'll have more time to build 
my game from the ground Up.

