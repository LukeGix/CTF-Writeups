# VolgaCTF 2021 - Streams

**Warning:** I'm new to the world of CTF, this is my first writeup. So sorry in advance if this writeup is messy, I'm still learning how to do it properly :)

**Challenge description:** 

``` 
We really really need one of the files that were captured in these two .pcapng. 
It contains a string that starts with "VolgaCTF". 
Is there any chance you could find it? 
```


This challenge provides us two pcap files: stream.pcap and stream2.pcap...but what exactly are pcap files? --> [FileCTF.zip](https://github.com/LukeGix/CTF-Writeups/files/6226861/FileCTF.zip) (A zip file containing the two files provided by the challenge)



PCAP files are Packet CAPtured files from Wireshark (a tool for network traffic analysis and more, link to the official website --> https://www.wireshark.org/)

Looking to the first file, stream.pcap, we can see that there are a lot of packets. In particular we can see that there are some types of packets called "FTP-DATA".
The first thing I thought is that some sort of files were loaded/downloaded from a server via FTP (stands for File Transfer Protocol).

![Stream1](https://user-images.githubusercontent.com/80392368/112874625-6efc8f00-90c3-11eb-9e3f-718463d0bc69.PNG)

By clicking on one of those packets, we can see in the info column that there is this request to store a file called "root.rar", so my intuition was correct. At first, I didn't know what to do, so I started researching on the Internet, when I stumbled across this site --> https://shankaraman.wordpress.com/2013/06/06/reconstructing-files-from-wireshark-packets/ that gave me some inputs.

## Step 1: Extract RAR file from stream.pcapng

In this article is explained very well how to extract the actual rar from this pcapng file; I will summerize it here, but I suggest you reading it:

1. In order to see the start of the rar file, we need to know that every rar archive have an **_header_** which, in this case, is only a sequence hex values: `52 61 72 21 1A 07 00`
2. Unfortunately, with CTRL + F I wasn't able to search for that sequence of hex values in the packets, but I saw the first packet of FTP-DATA type and in the detailed info window at the bottom of the screen, the hex values of the header, which can be transformed in the ascii string: Rar!....


![Capture2](https://user-images.githubusercontent.com/80392368/112874850-b8e57500-90c3-11eb-9daf-c73d17ebc105.PNG)



3. Once you have found this header, you have to right-click the packet in the main window and select the "Follow...TCP Stream" option.
4. This will open a new window where you can see more clearly the ascii representation of the RAR file.
5. You have to configure the "show and save data as" option to "raw" and you'll have to wait a little bit, in order to give wireshark the time to load all packets in "raw mode".
6. After 3/4 seconds, you can click the "save as..." button and save the file as a RAR file.

![Capture3](https://user-images.githubusercontent.com/80392368/112874965-dfa3ab80-90c3-11eb-984f-09d793ee7d73.PNG)


## Step 2: Repair RAR file

After Step 1, I tried to open the archive in Windows with WinRar, but I figure out that the RAR file was corrupted.
Fortunately, WinRar is able to repair corrupted RAR files, so I clicked on "Utilites --> Repair a corrupted archive"(this will create a new archive called rebuilt.*name_archive*.rar).


![Capture4](https://user-images.githubusercontent.com/80392368/112875179-242f4700-90c4-11eb-808d-a184e1776fe3.PNG)


After that, I tried to extract the archive, but I was asked to insert a password to unlock the archive, and this lead us to the third step.

![Capture5](https://user-images.githubusercontent.com/80392368/112875192-285b6480-90c4-11eb-9070-a25abdcc5559.PNG)


## Step 3: Recover password from stream2.pcapng

It's time to analyse stream2.pcapng.
The first time I opened it I was confused: can I sniff USB packets with wireshark?(In the protocol column, we can see that is specified USB) The answer is _yes_. Among all the wonderful things wireshark allow us to do, there is also USB packet sniffing and analysis.

![Capture6](https://user-images.githubusercontent.com/80392368/112875395-68bae280-90c4-11eb-83c2-461ca7890b52.PNG)


For me, this part was the hardest of this challenge, but also the most interesting.
The first thing I thought was that a keyboard communicates with the CPU thru _interrupts_. 
The keyboard literally interrupts the CPU saying that the user has typed some characters, so the CPU can read this characters and print them to the screen.

So I started searching for possible interrupts in the packets but I wasn't able to find anything. After some researches, I found this article --> https://abawazeeer.medium.com/kaizen-ctf-2018-reverse-engineer-usb-keystrok-from-pcap-file-2412351679f4 that actually was a writeup of another CTF.

In this article the author talks about four ways the keyboard can interact with CPU: isochronus mode, interrupt mode, bulk mode and control mode.
Each of these mode has an hex value that identifies the mode(0 for isochronus, 1 for interrupt, 2 for control and 3 for bulk).
So I thought that I had to find what mode this keyboard had used, but it turned out that in this pcap file there are multiple modes!

![Capture7](https://user-images.githubusercontent.com/80392368/112876218-863c7c00-90c5-11eb-9e2f-6e35da4dfa30.PNG)

I started looking for interrupt mode packets and I tried to see if from the Lefover Captured Data (Data that can contain the number of the key pressed) I could have been able to extract the key pressed from the user, but nothing. 

The legth of this data was too big to be a keystroke.

Reading the article mentioned before, I tried to put the same display filter shown in the article: `((usb.transfer_type == 0x01) && (frame.len == 72)) && !(usb.capdata == 00:00:00:00:00:00:00:00)` but this filter didn't worked for me.
So I tried to remove the "frame.len" part, applying the following filter: `((usb.transfer_type == 0x01) && !(usb.capdata == 00:00:00:00:00:00:00:00)`.
This is the output I received.

![Capture8](https://user-images.githubusercontent.com/80392368/112878161-e46a5e80-90c7-11eb-9541-6a0e44b24806.PNG)

The packet with length 35 caught my attention: the Leftover Capture Data wad very small and of the format `0000xx0000000000` (8 hex values), and this was also the format of the keystrokes that the guy of the writeup had found! 


| Leftover Capture Data |
| -------------------- |
| 0000**28**0000000000 |  
| 0000**1a**0000000000 |
| 0000**13**0000000000 |
| 0000**1a**0000000000 |
| 0000**0b**0000000000 |
| 0000**14**0000000000 |
| 0000**16**0000000000 |
| 0000**07**0000000000 |
| 0000**0b**0000000000 |
| 0000**0f**0000000000 |
| 0000**13**0000000000 |
| 0000**24**0000000000 |
| 0000**0b**0000000000 |
| 0000**1b**0000000000 |
| 0000**23**0000000000 |
| 0000**26**0000000000 |

These are the hex values that I found.


I tried to use his python script to map the `xx` values of the packets with the keys, but it didn't worked for me.
Eventually I figured out that these values are not the hex values of the key pressed, but they are the hex values of the **Usage IDs** of the keys. 
Fortunately I found a PDF from usb.org that explain the translation between Usage ID and key value. Link to the pdf --> https://usb.org/sites/default/files/documents/hut1_12v2.pdf (page 53)

So the hex values can be translated into:
28 --> Enter
1A --> w
13 --> p
1A --> w
0B --> h
14 --> q
16 --> s
07 --> d
0B --> h
0F --> l
13 --> p
24 --> 7
0B --> h
1B --> x
23 --> 6
26 --> 9

This is the password for the **RAR file**

## Step 4: The intricated RAR

After the extraction of the archive, we can see the beautiful mess of the root directory. Inside this directory there are **15** directories, and each of these directories have other sub-directories. 
Here there is the `tree` command on the root directory:


![Capture9](https://user-images.githubusercontent.com/80392368/112881322-cef73380-90cb-11eb-9863-4782c867d177.PNG)


Inside each folder there is a file called `FLAG IS HERE.txt`...obviously most of them are baits, but I knew that the flag must be inside this mess.
I exported the rar file in windows and I used the search function of WinRar to find the flag(I knew that the format of the flag was VolgaCTF{... so I searched for that) and boom! The flag magically appeared.

![FLAG](https://user-images.githubusercontent.com/80392368/112882086-cb17e100-90cc-11eb-9a61-95b1bf292203.PNG)

