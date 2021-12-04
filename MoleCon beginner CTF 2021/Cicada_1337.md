# Cicada 1337 - Misc




Description of the challenge:
```
Don't worry, you won't have to scan QRs across the globe
```
This is the image we got from the challenge

![level1](https://user-images.githubusercontent.com/80392368/144709045-50bc5937-3ff0-461b-b7b6-eed8c6c355b1.png)

The first thing I thought was to search strings inside the image, and I found a postimg link:
```
luke@luke:/$ strings level1.png | grep https
https://postimg.cc/3kM6gYzr
```

And another image:

![pidgey](https://user-images.githubusercontent.com/80392368/144709122-e5e5c38a-75c0-4282-92b9-df8eeee80f9c.jpg)

Another "strings" in this image led us to another postimg link

```
luke@luke:/$ strings pidgey.jpg | grep postimg
postimg.cc/K1HDbzfm
```

And this final image:


![congratulations](https://user-images.githubusercontent.com/80392368/144709206-3c7b39d2-8dd0-4cd5-bf6a-55fa6d694e2b.png)

I tried with a "strings" on this image but no prime numbers.

Then I realized that maybe the width and height could be 2/3 numbers we needed. The third number was the dimension of the comment in the image (found with exiftool)
The three numbers are: 643,587,1033. the product is 389896553, and so the subreddit is r/389896553.

In this subreddit there is a list of numbers and a story:

```
{A KOAN}

A MAN DECIDED TO GO AND STUDY WITH A MASTER

HE WENT TO THE DOOR OF THE MASTER

"WHO ARE YOU WHO WISHES TO STUDY HERE" ASKED THE MASTER

THE STUDENT TOLD THE MASTER HIS NAME

"THAT IS NOT WHO YOU ARE, THAT IS ONLY WHAT YOU ARE CALLED

WHO ARE YOU WHO WISHES TO STUDY HERE" HE ASKED AGAIN

THE MAN THOUGHT FOR A MOMENT, AND REPLIED "I AM A PROFESSOR"

"THAT IS WHAT YOU DO, NOT WHO YOU ARE," REPLIED THE MASTER

"WHO ARE YOU WHO WISHES TO STUDY HERE"

CONFUSED, THE MAN THOUGHT SOME MORE

FINALLY, HE ANSWERED, "I AM A HUMAN BEING"

"THAT IS ONLY YOUR SPECIES, NOT WHO YOU ARE

WHO ARE YOU WHO WISHES TO STUDY HERE", ASKED THE MASTER AGAIN

AFTER A MOMENT OF THOUGHT, THE PROFESSOR REPLIED "I AM A CONSCIOUSNESS INHABITING AN ARBITRARY BODY"

"THAT IS MERELY WHAT YOU ARE, NOT WHO YOU ARE

WHO ARE YOU WHO WISHES TO STUDY HERE"

THE MAN WAS GETTING IRRITATED

"I AM," HE STARTED, BUT HE COULD NOT THINK OF ANYTHING ELSE TO SAY, SO HE TRAILED OFF

AFTER A LONG PAUSE THE MASTER REPLIED, "THEN YOU ARE WELCOME TO COME STUDY"

```


```
9:43

19:50

5:35

1:1

14:41

19:10

12:11

7:44

5:23

20:11

6:58

16:22

20:63

8:12

17:27

2:34

9:4

20:34

19:57

15:35

8:44

15:80

18:29

1:8
```


We figure out that the numbers are in the format line:nth character, combining all the letters we had the flag!
9:43 -> p
19:50 -> t
5:35 -> m
1:1 -> {
14:41 -> S
19:10 -> E
12:11 -> E
7:44 -> K
5:23 -> A
20:11 -> N
6:58 -> D
16:22 -> Y
20:63 -> O
8:12 -> U
17:27 -> S
2:34 -> H
9:4 -> A
20:34 -> L
19:57 -> L
15:35 -> F
8:44 -> I
15:80 -> N
18:29 -> D
1:8 -> }
ptm{SEEKANDYOUSHALLFIND}
