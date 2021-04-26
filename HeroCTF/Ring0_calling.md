# HeroCTF - Ring0 Calling

Description of the challenge:

```
I like to compile my kernels. And I like to do it the old way.
And I also like doing it 50x times because I forgot an option.

Can you get the flag ?
```

The name of the challenge itself was a huge hint. Ring0 refers to the kernel space of linux system, and we, as users, can communicate with ring0 throught system calls.
For example, a lot of C function that deals with files are wrappers of this system calls.
Back to the challenge, when I executed the run script on the host, I found the BACKUP folder, which contained a syscall_64.tbl file. This is a file where are listed all system calls of the system.

![unknown](https://user-images.githubusercontent.com/80392368/116061352-0a612f80-a683-11eb-9206-3e67c9e5539a.png)

Scrolling through this system calls, I found this one that was a little bit suspicious.
Then I thought of all possible methods to make a syscall to this sys_hero, and then I realized that I could create a C program that used the syscall() function to call sys_hero(the number of sys_hero syscall is 442)

Here the source of the program:

```
#include <sys/syscall.h>
#include <unistd.h>
#define SYS_hero 442

int main(){
 syscall(SYS_hero);
 return 0;
}
```

***WARNING: WHEN YOU COMPILE THE PROGRAM, REMEMBER TO COMPILE IT WITH THE FLAG -STATIC!!***

And then, using "scp" program, you can load the compiled program to the host.
After executing it, the flag will be in the kernel log, accesible with dmesg command.
