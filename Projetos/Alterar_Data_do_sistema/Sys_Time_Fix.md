# System time Fix

### Sumary
Simple Fix using the Windows Terminal and TimeAPI for fast time adjusting using internet.

### Motivation

For some time my PC stoped syncronizing and had problems mantaining it's internal time ok, 
the cause of the problem is problably a internal hardware error, but I didn't had time to 
fix it or to be without my PC, so I simply changed it every time I had to turn on the PC.

Some day I skipped class because I thought the time was right, then I resolved to fix this
problem. I found an API for time in the internet, it is simply a site that the only string 
it has is the current date/time.

I did the formatting of the string into dictionary's and made a simple os message to the 
windows CMD for it to change the clock time instantaneously.

### How it works

- Search for the timeAPI
- Gets the HTML code
- formate it to a dictionary
- get the time and data key
- get it into format to send it to the CMD
- do a CMD command for it to change the time

### Precautions

If you cannot the program cannot change your time, you have to give the .exe file administrator 
permission for it to change your time. 

You have to be at least on the same year for it to properly work, or else the time API doens't
get it.

You have to be connected to the internet.
