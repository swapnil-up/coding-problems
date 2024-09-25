

25-09-2024 13:30

Status:

Tags:



# Missing semester MIT- Lecture 02- Shell Tools and Scripting

```
foo=bar
echo $foo
	returns bar
foo = bar
	returns command not found foo
```
As we see above, we can assign a value to another variable and call it via $name.

We are space sensitive in bash, the cli just understands it as a program called foo with parameters = and bar. 

You can pass string values in single or double quotes. If we pass a $variable too, then " will return the assigned value, while ' will return $ variable just like that. 
```
echo "value is $foo"
	returns value is bar
echo 'value is $foo'
	returns value is $foo
```

If we say source script.sh then it just loads it into the console, so that it can be run with a simple source parameter. 

$0 name of the script
$1 first argument of the script 
$2-$9 second to ninth argument in the script. 
$? Return code of the previous command
$_ Last argument from the last command.
Entire last command, including arguments. A common pattern is to execute a command only for it to fail due to missing permissions; you can quickly re-execute the command with sudo by doing `sudo !!` 
$@ - All the arguments
$# - Number of arguments
`$$` - Process identification number (PID) for the current script

By return code we mean if there was an error (1) or if it was a success (0). This means that running true in the shell, then echo $? returns 0, while false would echo out a 1. 

We have two operators || and && for OR and AND. 
```
false || echo "Oops, fail"
# Oops, fail

true || echo "Will not be printed"
#

true && echo "Things went well"
# Things went well

false && echo "Will not be printed"
#

true ; echo "This will always run"
# This will always run

false ; echo "This will always run"
# This will always run
```

We can also concatenate commands onto the same line using ;

We can do 
```
foo=$(pwd)
```
This would save the actual path into foo. This allows you to substitute in the output of the command. 

We also have process substitution, <( CMD ) which will execute CMD, then put the output in a temporary file and substitue the <( ) with just the file name. A simple example is `diff <(ls foo) <(ls bar)` which shows differences between files in dirs `foo` and `bar`.

```
#!/bin/bash

echo "Starting program at $(date)" # Date will be substituted

echo "Running program $0 with $# arguments with pid $$"

for file in "$@"; do
    grep foobar "$file" > /dev/null 2> /dev/null
    # When pattern is not found, grep has exit status 1
    # We redirect STDOUT and STDERR to a null register since we do not care about them
    if [[ $? -ne 0 ]]; then
        echo "File $file does not have any foobar, adding one"
        echo "# foobar" >> "$file"
    fi
done
```

Above we have a script that does some of what we've written earlier. 
Here we're moving all the output and errors into /dev/null. for error we prefixed with 2>

if `$? -ne 0` ; then refers to a conditional which checks if the command of the previous code is not equal to zero. Here zero of course refers to true condition, so if this conditional triggers then a foobar gets appended to the code blocks. 

We use double square brackets because that makes it less prone to errors. 

Arguments can be given more succinctly and the terminal will then expand them as needed. This is called globbing. This can be wildcards like * and ? or curly braces. 

```
ls *.sh 
	returns all .sh files.

convert image.{png,jpg}
# Will expand to
convert image.png image.jpg

cp /path/to/project/{foo,bar,baz}.sh /newpath
# Will expand to
cp /path/to/project/foo.sh /path/to/project/bar.sh /path/to/project/baz.sh /newpath

# Globbing techniques can also be combined
mv *{.py,.sh} folder
# Will move all *.py and *.sh files


mkdir foo bar
# This creates files foo/a, foo/b, ... foo/h, bar/a, bar/b, ... bar/h
touch 


{foo,bar}/{a..h}
touch foo/x bar/y
# Show differences between files in foo and bar
diff <(ls foo) <(ls bar)
# Outputs
# < x
# ---
# > y

```

We have scripts which get called via terminal, but the working mechanics is understood by the terminal based on the first shebang line. 

```
#!/usr/local/bin/python

while the above is correct, to make it portable it is best to use the path variable instead

#!/usr/bin/env python 
```


We can find errors in shell scripts using commands such as shellcheck.

tldr is a simpler man page version

command find allows you to find very easily

```
find . -name src -type d
```
Allows you to find within the current directory all directories with name src.

```
find . -path '**/test/*.py' -type f
```
This'd allow you to find all python files within a test folder

We can combine that with other commands as so, 
```
find . -name "*.tmp" -exec rm {} \;
```
Heh after running the above command to check if it worked, we could also use echo $? instead of running the whole file again. 

command locate would allow you to quickly locate all instances of a file, more rapidly than find which creates a structure. 

command grep allows us to find a keyword within a file quickly. We can also use it recursively:
```
grep foobar mcd.sh

grep -R foobar .
```

We also have rg, which is ripgrep which has some extra features like coloring, context lines

To look through history of commands instead of simply pressing up arrow, we can use command `history` 
To get it since the beginning of time we can do a history 1.

For some reason history 1 only returns the last entry on my terminal. 

Now we can pipe this to  grep to find only a specific type of command such as:

```
history | grep yt-dlp
```

fzf allows us to make a grep interactive. As such 
```
cat example.sh | fzf
```
Then write to have it enter stuff. 

To enable autocomplete suggestions based on past history in bash gotta get the ble.sh github repo. There's also hstr to look at in the future. 

We can look through directories with tools such as ls -R to list recursively, as well as tree command. 

Tools such as broot are even better though if you traverse directories often. 
Others such as fasd and autojump allow you to rank files by frecency (frequency and recency)


#### Exercises

1. Read [`man ls`](https://www.man7.org/linux/man-pages/man1/ls.1.html) and write an `ls` command that lists files in the following manner

- Includes all files, including hidden files
- Sizes are listed in human readable format (e.g. 454M instead of 454279954)
- Files are ordered by recency
- Output is colorized

ls -lhat --color=always

2. Write bash functions `marco` and `polo` that do the following. Whenever you execute `marco` the current working directory should be saved in some manner, then when you execute `polo`, no matter what directory you are in, `polo` should `cd` you back to the directory where you executed `marco`. For ease of debugging you can write the code in a file `marco.sh` and (re)load the definitions to your shell by executing `source marco.sh`.
It seems the shorthand for source is .
```
source myScript.sh
is the same as
. myScript.sh
```

Took me a second, but while referencing the basics of how shell functions are written it wasn't that tough. 

```
#!/bin/bash

dir="/"

marco() {
	dir=$(pwd)
	echo "$dir"
}

polo() {
	cd $dir
	echo $(pwd)
}
```


3. Say you have a command that fails rarely. In order to debug it you need to capture its output but it can be time consuming to get a failure run. Write a bash script that runs the following script until it fails and captures its standard output and error streams to files and prints everything at the end. Bonus points if you can also report how many runs it took for the script to fail.

    ```
     #!/usr/bin/env bash
    
     n=$(( RANDOM % 100 ))
    
     if [[ n -eq 42 ]]; then
        echo "Something went wrong"
        >&2 echo "The error was using magic numbers"
        exit 1
     fi
    
     echo "Everything went according to plan"
    ```


# References

