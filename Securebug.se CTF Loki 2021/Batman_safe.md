## Securebug.se CTF Loki 2021 - Batman Safe

Description of the challenge:

```
Find the correct combination for Batman’s Safe and submit the generated flag!
```

So, for this challenge we have an ELF executable named 'Safe.Run'

![image](https://user-images.githubusercontent.com/80392368/126750167-04feaa4b-f2ff-400e-8c2f-a10d04b01b77.png)

Once we execute it, it will ask a name and a combination to unlock the safe.
The first thing I thought was to analyse it with ghidra.

![image](https://user-images.githubusercontent.com/80392368/126750757-34598e0c-bcad-4fdc-a1d0-bba3c059b051.png)


These are the most important part of the main function. The first thing I noticed were the declaration of the variables(first image). We have the control over the first two array and I thought that maybe we could do a buffer overflow.

![image](https://user-images.githubusercontent.com/80392368/126750816-a23997cd-0e46-491e-93af-3e1cba5865be.png)

Going down in the main function, we can see that there are a bunch of "if" statement: they check if the variables declared above have a particular value. The problem is that those variables were initialized! How we can assing them some values?
And so I had the confirmation that we need a buffer overflow: we set the first two arrays and the overflow to assign values to other variables.

In the first while loop, we can see that it checks only the first character of the name, to see if it starts with **B**.

Then, checking all the if cases, we can retrieve the combination: **sb7hs-dhza4-r2d3z-tra25**.

![image](https://user-images.githubusercontent.com/80392368/126751718-da023420-1352-4433-b9b1-203762924d7a.png)

If we insert this information in the program, we get the flag!
