

25-09-2024 13:29

Status:

Tags:



# Missing semester MIT- Lecture 1- Overview and the shell

CLI is better than GUIs because with GUIs we're limited to whatever buttons, sliders, fields we have. With CLIs we are able to do much more as well as combine multiple tools together to perform what is magic. 

The shell prompt is what you see at the start. 

command date just shows you the date.
	
command echo repeats back what is entered following a space. if you are displaying two words or smth then just put in double quotes or an escape character.

	echo "Hello world"
	echo Hello\ World

Environment variables are things that are set at the start of a shell. like home directory, user name, path and more. They're usually $ followed by variable name. So:
	echo $PATH 
returns a list of semicolon separated paths. 

command which tells us the actual program and its path. 

A path is usually directory names separated by / in linux and mac. In windows we have partitions like C: and D: and further separation is with a backslash

An absolute path fully determine the location of a file. A relative path is relative to where you currently are. 

command pwd to find where we currently are. means print work directory. 

command cd is for changing directories. so cd /home will move you to home directory. 

Two special directories are: 
. which is for the current directory
.. which is for the previous directory

So say I was in a directory called street and it had a child directory called home. then to cd into it we'd use cd ./home to indicate going to the current directories home directory, instead of absolute path's home directory. 

When we execute a file by typing ./file, here the . is probably the special directory. Woah.

command ls shows us the list of current files within the directory. A simple chaining that we can do is ls .. which will list the files within the parent directory instead of having to cd into parent then running ls. 

cd ~ always brings us to the home directory. Run relative paths through that if you want to.

cd - brings us back to the previous directory we were currently in. 

To find other options that are available with a command such as ls we can use --help. Remember most of these types of shell commands have both options and flags that you can set in the same line. 

In the help typically we have a line called:
	Usage: ls OPTIONS ... FILE ...
Here if the options or file is put in square brackets then that means it is optional. 

Usually single dash single letter as flag. It doesn't take values. An option takes values. 

ls -l shows all the files and detailed information such as if it's a file, directory, link etc, then the permissions, owners, groups and more. 

command mv allows you to rename a file. It is also used to move the file. Takes two paths as arguments for.

command cp allows you to copy files. You can use paths as the arguments here as well. 

command rm is to remove files. It is non-recursive. Put a -r flag at the end. rmdir is to remove empty directories. Made to make sure you don't delete a bunch of files on accident. 

command mkdir allows you to make a directory. If you type my photo it'll make two directories my and photos. So put within quotes or smth. 

command man summons the manual for whatever command is entered after man . Use q to quit.

BIG BRAIN: use ctrl L to clear the terminal. No need to type clear in the shell then press enter. 


Programs can be chained together using streams. Usually there's two streams input and output. By default input is the keyboard and output is the screen, but a terminal can allow you to rewire the streams. 

The simplest way is to use angle brackets. < allows you to rewire the input for the program, and vice versa. 

	echo hello > hello.txt
would now return hello by writing it in a directory called hello.txt. 

command cat allows you to print the contents of a file. 

	cat < hello.txt
would say cat to take its inputs from hello.txt. This displays on the terminal because we didn't change the output stream here.

	cat < hello.txt >hello2.txt
This now gives the hello.txt as input to cat and then it is output to hello2.txt

We can append by using double angle bracket like >>

We have the pipe command | which just takes the output of the left and use it as the input of the right. 

	ls -l / | tail -n1
Now ls returns a long list of entries. Tail on the otherhand is a program that just returns the end of a file. These two program were programmed independent of each other, they don't know the other exist, but here work together so easily. the | just makes it work. 

We're also able to use this with not just with text files but also images, and videos. Think mpv.

sudo means do as su (which is super) 

cd /sys opens a whole new world. This includes things in your kernel parameter. The core of your computer. Like class has bluetooth and backlight. 

Here the example was to change the brightness to 500.  The echo 500 > brightness returns permission denied. sudo will not work because the redirection of streams is not known, like how ls and tail didn't know about each other. (Ah, the beauty of the UNIX philosophy, everything does one thing, then extend). 

One way to handle is to change the user to root. This is signified in the shell by the $ having changed into #. All those stackoverflow questions now make sense. We can do sudo su to run as root to achieve the change to #.

command tee allows things to be written into the file but also stdout, so you can see it in the terminal too.  

so if we did 
	echo 1050 | sudo tee brightness 
we're able to make it work without going into a root terminal. tee was given sudo permission which was enough. 

One potential goldmine idea is the scroll lock LED. It has no functional purpose atm, but by having access here, we can change it so that it turns on when email is received. 

command xdg-open then a file will open it in the apt application. This'd mean that you'd never have to open a file explorer again. Heh. 


Extra things noted when reading through the class lectures. 

bash's full form is Bourne Again SHell. 


#### Exercises

1. To make sure you’re running an appropriate shell, you can try the command `echo $SHELL`. If it says something like `/bin/bash` or `/usr/bin/zsh`, that means you’re running the right program. 
Says /bin /bash

2. Create a new directory called `missing` under `/tmp`.
cd /tmp
mkdir missing

piping the two together didn't work. That is used for stream. Seems the answer is semicolon ;

cd /tmp; mkdir missing
This works. 

3. Look up the `touch` program. The `man` program is your friend.
man touch 
Seems that the option is optional but a file must be given. It allows for access and modification times to be changed, as well create a new empty file if it doesn't exist. 

4. Use `touch` to create a new file called `semester` in `missing`.
touch semester

5. Write the following into that file, one line at a time:

```
#!/bin/sh
curl --head --silent https://missing.csail.mit.edu
```

The first line might be tricky to get working. It’s helpful to know that `#` starts a comment in Bash, and `!` has a special meaning even within double-quoted (`"`) strings. Bash treats single-quoted strings (`'`) differently: they will do the trick in this case. See the Bash [quoting](https://www.gnu.org/software/bash/manual/html_node/Quoting.html) manual page for more information.

```
echo '#!/bin/sh' > semester
curl --head --silent https://missing.csail.mit.edu
```
Here I got confused and wrote cat echo first. Nope as we enter one program at a time. Also double quotes didn't work here surprisingly. To append the second line we used >>. 

6. Try to execute the file, i.e. type the path to the script (`./semester`) into your shell and press enter. Understand why it doesn’t work by consulting the output of `ls` (hint: look at the permission bits of the file).

/tmp/missing/semester
returns bash: /tmp/missing/semester: Permission denied
Didn't work because the file hasn't been made executable. 

7. Run the command by explicitly starting the `sh` interpreter, and giving it the file `semester` as the first argument, i.e. `sh semester`. Why does this work, while `./semester` didn’t?

`man sh` was very helpful
sh /tmp/missing/semester
ran very easily. 

The difference lies in how shell interpreters handle script execution vs how the OS handles an executable file. In a simpler way, the sh is simply reading and executing line by line like a simple text file. 

8. Look up the `chmod` program (e.g. use `man chmod`).
man chmod
The usage says that atleast one mode must be specified, with more being optional. 

9. Use `chmod` to make it possible to run the command `./semester` rather than having to type `sh semester`. How does your shell know that the file is supposed to be interpreted using `sh`? See this page on the [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) line for more information.
chmod +x semester

10. Use `|` and `>` to write the “last modified” date output by `semester` into a file called `last-modified.txt` in your home directory.

Was trying to use sed, but that works with the actual script, not contents. 

Got stuck trying to make it all in one line, maybe I didn't have to? Did get in multiple lines, but had to get chatGPT to help with single line which needed && operator. 

./semester > hello3.txt && (head -n 4 hello3.txt | tail -n 1 > ~/hi.txt)

Here we put the data from the script into hello3.txt and then we cut to the fourth line which holds the date modified, then cut just that line out of all those above it with tail and then redirected to hi in my home. 

GPT used grep when I gave it the question. As such:

./semester | grep -i 'last-modified' > ~/last-modified.txt


11. 1. Write a command that reads out your laptop battery’s power level or your desktop machine’s CPU temperature from `/sys`. Note: if you’re a macOS user, your OS doesn’t have sysfs, so you can skip this exercise.

cd /sys/class/power_supply
then,
cat BAT0/capacity


# References

https://www.baeldung.com/linux/read-specific-line-from-file