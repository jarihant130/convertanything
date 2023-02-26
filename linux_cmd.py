import streamlit as st
import string

# Set page config for entire app
st.set_page_config(page_title="Linux Commands", page_icon=":penguin:", layout="wide")

# Define the commands for each alphabet page
commands = {
    "A": {
        "adduser/addgroup: The adduser and addgroup commands are used to add a user and group to the system respectively according to the default configuration specified in /etc/adduser.conf file." : "$ sudo adduser tecmint",
        "agetty is a program which manages physical or virtual terminals and is invoked by init." : "$ agetty -L 9600 ttyS1 vt100",
        "alias is a useful shell built-in command for creating aliases (shortcut) to a Linux command on a system." : "$ alias home='cd /home/tecmint/public_html'",
        "anacron is a Linux facility used to run commands periodically with a frequency defined in days, weeks and months. anacron jobs are listed in /etc/anacrontab and jobs can be scheduled using the format below " : "period   delay   job-identifier   command",
        "apropos command is used to search and display a short man page description of a command/program " : "$ apropos adduser",
        "apt tool is a relatively new higher-level package manager for Debian/Ubuntu systems" : "$ sudo apt update",
        "apt-get is used to install new software packages, remove available software packages, upgrade existing software packages as well as upgrade entire operating system." : "$ sudo apt-get update",
        "arch is a simple command for displaying machine architecture or hardware name (similar to uname -m)" : "$ arch",
        "arp (Address Resolution Protocol) is a protocol that maps IP network addresses of a network neighbor with the hardware (MAC) addresses in an IPv4 network." : "$ sudo arp-scan --interface=enp2s0 --localnet",
        "at command is used to schedule tasks to run in a future time. It’s an alternative to cron and anacron, however, it runs a task once at a given future time without editing any config files" : '$ sudo echo "shutdown -h now" | at -m 23:55',
        "atq command is used to view jobs in at command queue" : "$ atq",
        "atrm command is used to remove/deletes jobs (identified by their job number) from at command queue" : "$ atrm 2",
        "awk is a powerful programming language created for text processing and generally used as a data extraction and reporting tool.": "$ awk '/error/ { print }' log.txt",
    },
    "B": {
        "batch is also used to schedule tasks to run a future time, similar to the at command" : "",
        "basename command helps to print the name of a file stripping of directories in the absolute path" : "$ basename bin/findhosts.sh",
        "bc is a simple yet powerful and arbitrary precision CLI calculator language which can be used like this:": "$ echo '4.5 + 3.2' | bc",
        "bg is a command used to send a process to the background." : """
        $ tar -czf home.tar.gz .
$ bg 
$ jobs
        """,
        "bzip2 command is used to compress or decompress file(s)." : "$ bzip2 -z filename      #Compress \n$ bzip2 -d filename.bz2  #Decompress",
    },
    "C": {
        " cal command print a calendar on the standard output" : "$ cal",
        "cat is used to view contents of a file or concatenate files, or data provided on standard input, and display it on the standard output" : "$ cat file.txt",
        "cd is used to change from one directory to another": "$ cd /usr/local/bin",
        "chgrp command is used to change the group ownership of a file. Provide the new group name as its first argument and the name of file as the second argument like this" : "$ chgrp tecmint users.txt",
        "chmod command is used to change/update file access permissions": "$ chmod 755 myscript.sh \n         or \n$ chmod +x sysinfo.sh",
        "chown command changes/updates the user and group ownership of a file/directory": "$ chown user1 myfile.txt \n        or\n$ chmod -R www-data:www-data /var/www/html",
        "cksum command is used to display the CRC checksum and byte count of an input file" : "$ cksum README.txt",
        "clear command lets you clear the terminal screen" : "$ clear",
        "cmp performs a byte-by-byte comparison of two files" : "$ cmp file1 file2",
        "comm command is used to compare two sorted files line-by-line " : "$ comm file1 file2",
        "cp command is used for copying files and directories from one location to another": "$ cp /home/file1.txt /home/Personal/"
    },
    "D": {
        "date command displays/sets the system date and time" : '$ date \n$ date --set="8 JUN 2017 13:00:00"',
        "dd command is used for copying files, converting and formatting according to flags provided on the command line. It can strip headers, extracting parts of binary files and so on": "$ dd if=/dev/zero of=myfile.bin bs=1M count=10",
        "df is used to show file system disk space usage": "$ df -h",
        "diff is used to compare two files line by line. It can also be used to find the difference between two directories in Linux" : "$ diff file1 file2",
        "dir works like Linux ls command, it lists the contents of a directory" : "$ dir",
        "is a tool for retrieving hardware information of any Linux system. It dumps a computer’s DMI (a.k.a SMBIOS) table contents in a human-readable format for easy retrieval" : "$ sudo dmidecode --type system",
        "du is used to show disk space usage of files present in a directory as well as its sub-directories": "$ du /home/mydir \n    or\n$ du -h mydir"
    },
    "E": {
        "echo prints a text of line provided to it.": "$ echo 'Hello, world!'",
        "" : ""
    },
    "F": {
        "find": "$ find /home/user1 -name '*.txt'"
    },
    "G": {
        "grep": "$ grep 'error' log.txt"
    },
    "H": {
        "history": "$ history"
    },
    "I": {
        "ifconfig": "$ ifconfig eth0"
    },
    "J": {
        "jobs": "$ jobs"
    },
    "K": {
        "kill": "$ kill <pid>",
        "killall": "$ killall firefox"
    },
    "L": {
        "ls": "$ ls -l"
    },
    "M": {
        "mkdir": "$ mkdir mydir",
        "mv": "$ mv file1.txt file2.txt"
    },
    "N": {
        "netstat": "$ netstat -an"
    },
    "O": {
        "openssl": "$ openssl enc -aes-256-cbc -salt -in file.txt -out file.enc"
    },
    "P": {
        "ping": "$ ping google.com",
        "ps": "$ ps -ef | grep <process>"
    },
    "Q": {
        "quota": "$ quota -u user1"
    },
    "R": {
        "rm": "$ rm file.txt",
        "rmdir": "$ rmdir mydir"
    },
    "S": {
        "scp": "$ scp file.txt user@remote:/path/to/dir",
        "sed": "$ sed 's/error/warning/g' log.txt",
        "ssh": "$ ssh user@remote"
    },
    "T": {
        "tar": "$ tar -czvf archive.tar.gz /path/to/dir",
        "top": "$ top"
    },
    "U": {
        "umask": "$ umask 022",
        "uniq": "$ uniq file.txt"
    },
    "V": {
        "vi": "Open the vi editor"
    },
    "W": {
        "wget": "$ wget http://example.com/file.txt"
    },
    "X": {
        "xargs": "$ find /path/to/dir -name '*.txt' | xargs grep 'error'"
    },
    "Y": {
        "yes": "$ yes 'y'"
    },
    "Z": {
        "zip": "$ zip -r archive.zip /path/to/dir"
    }
}


# Define a function to display the commands for a given alphabet page
def display(page):
    st.write(f"## Linux Commands - {page}")
    st.write("---")
    st.write("### Commands:")
    if page in commands:
        for command, example in commands[page].items():
            st.write(f"#### `{command}`")
            st.code(example)
            st.write("---")
    else:
        st.write("No commands found for this letter.")
    
# Define a function to display buttons for selecting an alphabet page
def alphabet_selector():
    st.write("## Select an alphabet:")
    button_style = """
        display: inline-block;
        margin-right: 5px;
        margin-bottom: 5px;
        padding: 5px;
        border-radius: 5px;
        background-color: #f0f0f0;
    """
    for letter in string.ascii_uppercase:
        if letter in commands:
            if st.button(letter, key=letter):
                display(letter)
            st.write(f'<style>.stButton#{letter} {{{button_style}}}</style>', unsafe_allow_html=True)
        else:
            st.write(letter)










