# HeroCTF - Kernel module #3

Description of the challenge:

```
Hey honey !

I hid a last gift in the living room.
It's in another box.
The key's in the second safe, you know the wheel protected one.
Love you ! xoxo
```

Again, in this challenge there is a safe_mod.ko module. I downloaded it and analysed in ghidra.
In this case we don't have a device_file_write function in the module, so we don't have to write to the device.
Instead I found a device_file_ioctl function. I did some researches to understand what ioctl means, and I found that is an alternative way to send command and data to the driver.
Fortunately there is a C function ioctl() to communicate to the driver.

This function requires a file descriptor of /dev/safe and a request, supplied in the hint of the challenge.

Analysing more the function, we can understand how to unlock the safe:

![pa](https://user-images.githubusercontent.com/80392368/116065425-47c7bc00-a687-11eb-9f68-dca356d94fb0.PNG)

We need to do a ioctl() three times, and every time we need to change param 3 in order to unlock the right lock.

The tree numbers to send are: 69 47 20

After sending this 3 number to device driver, I tried to do 'cat flag.txt', but there was nothing :(

Then I realized that I need to use the same C program to do so, with root privileges. So after having unlocked all 3 locks, we need to spawn a root shell from our C program, then we can see the flag.
Here the source of the C program:
```

#include <stdio.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#define W_COMBINATION _IOW('x', 'w', int*)    //hint of the challenge --> equivalent to copy_from_user()

int main(int argc, char* argv[]){
    int number;
    char res[1000];
    int fd = open("/dev/safe", 2);
    write(fd, "Hello", 5);
    
    for(int i=0; i < 2; i++){
        printf("Number to send to the driver: ");
        scanf("%d", &number);
        ioctl(fd, W_COMBINATION, (signed int)number);
    }

    printf("Number to send to the driver: ");
    scanf("%d", &number);
    ioctl(fd, W_COMBINATION, (signed int)number);
    system("/bin/sh"); //Become root and now you can do 'cat flag.txt'
}

```
