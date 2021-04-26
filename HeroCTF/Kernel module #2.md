# HeroCTF - Kernel module #2.md

Description of the challenge:

```
Hey sweetie !

I placed a little gift for you in the living room.
It's in a box that's locked though.
The key's in the safe, and this time I locked it with a password.
Love you ! xoxo

PS : Happax seems to be back to normal.
```

The method to access to this challenge is the same as the previous one.

Once in the challenge, I noticed a safe_mod.ko. I downloaded it to my machine and I statically analized it with ghidra, and I found some interesting functions:

![aaaaaaaaa](https://user-images.githubusercontent.com/80392368/116063350-2b2a8480-a685-11eb-8298-ff75b53cd800.PNG)

After some researches, I found out that the device_file_write is called when we try to write something to /dev/safe and device_file_read is called when we try to read from /dev/safe

![dd](https://user-images.githubusercontent.com/80392368/116063679-8a889480-a685-11eb-8427-a57f0ecd212b.PNG)

In the decompiled version of device_file_write, at one point there is a strstr call to see if in the string we write to /dev/safe there is OpenSesame.

So OpenSesame is the password to unlock the safe.
However, I've tried to do 'echo "OpenSesame" > /dev/safe' but no flag in dmesg.

So, after some time, I found in the init module function of the device a variable called rot13_ops, so I thought that maybe I had to encrypt it in ROT13.

I used cyberchef --> https://gchq.github.io/CyberChef/ to encrypt "OpenSesame" and echoed it in /dev/safe. Then you can do 'cat flag.txt' and see the flag!
