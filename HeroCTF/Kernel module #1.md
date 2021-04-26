# HeroCTF - Kernel Module #1

Description of the challenge: 
```
Hey sweetheart !
I left a little something for you in the safe.
It's unlocked, so you just have to retrieve it.
Love you ! xoxo
PS : Happax, the cat, has been behaving oddly lately.. 
```

In order to start the challenge, we had to connect via ssh to an host.
Once connected, we had to execute the run script and the real challenge started.

The challenge said that we should read the /dev/safe device for the flag, but cat didn't work --> ```PS : Happax, the cat, has been behaving oddly lately.. ```

So I used the less command to read the device, and so I was able to get the flag.
