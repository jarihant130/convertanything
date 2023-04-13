import streamlit as st
import string

# Set page config for entire app
st.set_page_config(page_title="Linux Commands", page_icon=":penguin:", layout="wide")

# Define the commands for each alphabet page
commands = {
    "A": {
        "adduser/addgroup: The adduser and addgroup commands are used to add a user and group to the system respectively according to the default configuration specified in /etc/adduser.conf file." : "$ sudo adduser ConvertAnyThing",
        "agetty is a program which manages physical or virtual terminals and is invoked by init." : "$ agetty -L 9600 ttyS1 vt100",
        "alias is a useful shell built-in command for creating aliases (shortcut) to a Linux command on a system." : "$ alias home='cd /home/ConvertAnyThing/public_html'",
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
        "chgrp command is used to change the group ownership of a file. Provide the new group name as its first argument and the name of file as the second argument like this" : "$ chgrp ConvertAnyThing users.txt",
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
        "echo command prints a text of line provided to it.": "$ echo 'Hello, world!'",
        "eject command is used to eject removable media such as DVD/CD ROM or floppy disk from the system." : "$ eject /dev/cdrom \n$ eject /mnt/cdrom/ \n$ eject /dev/sda",
        "env command lists all the current environment variables and used to set them as well.": "$ env",
        "exit command is used to exit a shell": "$ exit",
        "expr command is used to calculate an expression" : "$ expr 30 - 20"
    },
    "F": {
        "factor command is used to show the prime factors of a number." : "$ factor 10",
        "find command lets you search for files in a directory as well as its sub-directories. It searches for files by attributes such as permissions, users, groups, file type, date, size and other possible criteria": "$ find /home/user1 -name '*.txt'",
        "free command shows the system memory usage (free, used, swapped, cached, etc.) in the system including swap space. Use the -h option to display output in human friendly format." : "$ free -h",
    },
    "G": {
        "grep command searches for a specified pattern in a file (or files) and displays in output lines containing that pattern ": "$ grep 'error' log.txt",
        "groups command displays all the names of groups a user is a part of" : "$ groups \n $ groups convert_anything",
        "gzip helps to compress a file, replaces it with one having a .gz extension": "$ gzip passwds.txt \n$ cat file1 file2 | gzip > foo.gz",
        "gunzip expands or restores files compressed with gzip command" : "$ gunzip foo.gz",
    },
    "H": {
        "head command is used to show first lines (10 lines by default) of the specified file or stdin to the screen" : "ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head",
        "history command is used to show previously used commands or to get info about command executed by a user": "$ history",
        "hostname command is used to print or set system hostname in Linux." : "$ hostname \n$ hostname NEW_HOSTNAME",
        "hostnamectl command controls the system hostname under systemd. It is used to print or modify the system hostname and any related settings" : "$ hostnamectl \n$ sudo hostnamectl set-hostname NEW_HOSTNAME",
        "hwclock is a tool for managing the system hardware clock; read or set the hardware clock (RTC)" : "$ sudo hwclock \n$ sudo hwclock --set --date 8/06/2017",
        "hwinfo is used to probe for the hardware present in a Linux system" : "$ hwinfo",
    },
    "I": {
        "id command shows user and group information for the current user or specified username" : "$ id ConvertAnyThing",
        "ifconfig command is used to configure a Linux systems network interfaces. It is used to configure, view and control network interfaces": "$ ifconfig \n$ sudo ifconfig eth0 up \n$ sudo ifconfig eth0 down \n$ sudo ifconfig eth0 172.16.25.125 ",
        "ionice command is used to set or view process I/O scheduling class and priority of the specified process. If invoked without any options, it will query the current I/O scheduling class and priority for that process": "$ ionice -c 3 rm /var/logs/syslog",
        "iostat is used to show CPU and input/output statistics for devices and partitions. It produces useful reports for updating system configurations to help balance the input/output load between physical disks." : "$ iostat",
        "ip command is used to display or manage routing, devices, policy routing and tunnels. It also works as a replacement for well known ifconfig command." : "$ sudo ip addr add 192.168.56.10 dev eth1",
        "iptables is a terminal based firewall for managing incoming and outgoing traffic via a set of configurable table rules." : "$ sudo iptables -L -n -v",
        "iw command is used to manage wireless devices and their configuration." : "$ iw list ",
        "iwlist command displays detailed wireless information from a wireless interface. The command below enables you to get detailed information about the wlp1s0 interface." : "$ iwlist wlp1s0 scanning",
    },
    "J": {
        "jobs": "$ jobs"
    },
    "K": {
        "kill command is used to kill a process using its PID by sending a signal to it (default signal for kill is TERM)": "$ kill <pid> \n$ kill -p 2300 \n$ kill -SIGTERM -p 2300",
        "killall command is used to kill a process by its name.": "$ killall firefox",
        "kmod command is used to manage Linux kernel modules. To list all currently loaded modules, type." : "$ kmod list",
    },
    "L": {
        "last command display a listing of last logged in users." : "$ last ",
        "ln command is used to create a soft link between files using the -s flag" : "$ ln -s /usr/bin/lscpu cpuinfo",
        "locate command is used to find a file by name. The locate utility works better and faster than it’s find counterpart. The command below will search for a file by its exact name (not *name*):" : "$ locate -b '\domain-list.txt'",
        "login command is used to create a new session with the system. You’ll be asked to provide a username and a password to login" : "$ sudo login",
        "ls command is used to list contents of a directory. It works more or less like dir command.": "$ ls -l \n$ ls -l file1",
        "lshw command is a minimal tool to get detailed information on the hardware configuration of the machine, invoke it with superuser privileges to get a comprehensive information." : "$ sudo lshw ",
        "lscpu command displays system’s CPU architecture information (such as number of CPUs, threads, cores, sockets, and more)" : "$ lscpu",
        "lsof command displays information related to files opened by processes. Files can be of any type, including regular files, directories, block special files, character special files, executing text reference, libraries, and stream/network files." : "$ lsof -u ConvertAnyThing",
        "lsusb command shows information about USB buses in the system and the devices connected to them" : "$ lsusb ",
    },
    "M": {
        "man command is used to view the on-line reference manual pages for commands/programs" : "$ man du \n$ man df",
        "md5sum command is used to compute and print the MD5 message digest of a file. If run without arguments, debsums checks every file on your system against the stock md5sum files" : "$ sudo debsums",
        "mkdir command is used to create single or more directories, if they do not already exist (this can be overridden with the -p option)": "$ mkdir convertAnyThing-files \n$ mkdir -p convertAnyThing-files",
        "more command enables you to view through relatively lengthy text files one screenful at a time." : "$ more file.txt",
        "mv command is used to rename files or directories. It also moves a file or directory to another location in the directory structure.": "$ mv file1.txt file2.txt"
    },
    "N": {
        "nano is a popular small, free and friendly text editor for Linux; a clone of Pico, the default editor included in the non-free Pine package." : "$ nano file.txt",
        "nc (or netcat) is used for performing any operation relating to TCP, UDP, or UNIX-domain sockets. It can handle both IPv4 and IPv6 for opening TCP connections, sending UDP packets, listening on arbitrary TCP and UDP ports, performing port scanning." : "$ nc -zv 192.168.1.5 22",
        "netstat command displays useful information concerning the Linux networking subsystem (network connections, routing tables, interface statistics, masquerade connections, and multicast memberships)": "$ netstat -an \n$ netstat -a | more",
        "nice command is used to show or change the nice value of a running program. It runs specified command with an adjusted niceness. When run without any command specified, it prints the current niceness. The following command starts the process “tar command” setting the “nice” value to 12." : "$ nice -12 tar -czf backup.tar.bz2 /home/*",
        "nmap is a popular and powerful open source tool for network scanning and security auditing. It was intended to quickly scan large networks, but it also works fine against single hosts." : "$ nmap -sV 192.168.56.0/24",
        "nproc command shows the number of processing units present to the current process. It’s output may be less than the number of online processors on a system." : "$ nproc",
    },
    "O": {
        "The openssl is a command line tool for using the different cryptography operations of OpenSSL’s crypto library from the shell. The command below will create an archive of all files in the current directory and encrypt the contents of the archive file": "$ tar -czf - * | openssl enc -e -aes256 -out backup.tar.gz \n$ openssl enc -aes-256-cbc -salt -in file.txt -out file.enc"
    },
    "P": {
        "passwd command is used to create/update passwords for user accounts, it can also change the account or associated password validity period. Note that normal system users may only change the password of their own account, while root may modify the password for any account." : "$ passwd convertAnyThing",
        "pidof displays the process ID of a running program/command." : "$ pidof init \n$ pidof cinnamon",
        "ping command is used to determine connectivity between hosts on a network (or the Internet)": "$ ping google.com",
        "ps shows useful information about active processes running on a system. The example below shows the top running processes by highest memory and CPU usage.": "ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head \n$ ps -ef | grep <process>",
        "pstree displays running processes as a tree which is rooted at either PID or init if PID is omitted." : "$ pstree",
        "pwd command displays the name of current/working directory" : "$ pwd",
    },
    "Q": {
        "quota": "$ quota -u user1"
    },
    "R": {
        "rdiff-backup is a powerful local/remote incremental backup script written in Python. It works on any POSIX operating system such as Linux, Mac OS X. Note that for remote backups, you must install the same version of rdiff-backup on both the local and remote machines." : "$ sudo rdiff-backup /etc /media/ConvertAnyThing/Backup/server_etc.backup",
        "reboot command may be used to halt, power-off or reboot a system" : "$ reboot",
        "rename command is used to rename many files at once. If you’ve a collection of files with “.html” extension and you want to rename all of them with “.php” extension" : "$ rename 's/\.html$/\.php/' *.html",
        "rm command is used to remove files or directories": "$ rm file.txt \n$ rm file1 \n$ rm -rf my-files",
        "rmdir command helps to delete/remove empty directories": "$ rmdir mydir",
    },
    "S": {
        "scp command enables you to securely copy files between hosts on a network": "$ scp file.txt user@remote:/path/to/dir",
        "sed": "$ sed 's/error/warning/g' log.txt",
        "shutdown command schedules a time for the system to be powered down. It may be used to halt, power-off or reboot the machine" : "$ shutdown --poweroff",
        "sleep command is used to delay or pause (specifically execution of a command) for a specified amount of time" : "$ check.sh; sleep 5; sudo apt update",
        "sort command is used to sort lines of text in the specified file(s) or from stdin" : "$ sort filename.txt",
        "split as the name suggests, is used to split a large file into small parts." : "$ tar -cvjf backup.tar.bz2 /home/ConvertAnyThing/Documents/* ",
        "ssh (SSH client) is an application for remotely accessing and running commands on a remote machine. It is designed to offer a secure encrypted communications between two untrusted hosts over an insecure network such as the Internet.": "$ ssh user@remote",
        "stat is used to show a file or file system status like this (-f is used to specify a filesystem)." : "$ stat file1",
        "su command is used to switch to another user ID or become root during a login session. Note that when su is invoked without a username, it defaults to becoming root." : "$ su \n$ su ConvertAnyThing",
        "sudo command allows a permitted system user to run a command as root or another user, as defined by the security policy such as sudoers. In this case, the real (not effective) user ID of the user running sudo is used to determine the user name with which to query the security policy." : "$ sudo apt update \n$ sudo useradd ConvertAnyThing \n$ sudo passwd ConvertAnyThing",
        "sum command is used to show the checksum and block counts for each each specified file on the command line." : "$ sum output file.txt ", 
    },
    "T": {
        "tac command concatenates and displays files in reverse. It simply prints each file to standard output, showing last line first." : "$tac file.txt",
        "tail command is used to display the last lines (10 lines by default) of each file to standard output. If there more than one file, precede each with a header giving the file name. Use it as follow (specify more lines to display using -n option)." : "$ tail long-file \n$ tail -n 15 long-file",
        "talk command is used to talk to another system/network user. To talk to a user on the same machine, use their login name, however, to talk to a user on another machine use ‘user@host’." : "$ talk person [ttyname] \n$ talk ‘user@host’ [ttyname]",
        "tar command is a most powerful utility for archiving files in Linux.": "$ tar -czvf archive.tar.gz /path/to/dir",
        "tee command is used to read from standard input and prints to standard output and files " : '$ echo "Testing how tee command works" | tee file1 ',
        "time command runs programs and summarizes system resource usage." : "$ time wc /etc/hosts",
        "top program displays all processes on a Linux system in regards to memory and CPU usage and provides a dynamic real-time view of a running system." : "$ top",
        "touch command changes file timestamps, it can also be used to create a file" : "$ touch file.txt",
        "tr command is a useful utility used to translate (change) or delete characters from stdin, and write the result to stdout or send to a file" : "$ cat domain-list.txt | tr [:lower:] [:upper:]",
        "The tree command is a tiny, cross-platform command-line program used to recursively list or display the content of a directory in a tree-like format." : "$ tree",
    },
    "U": {
        "The umask command in Linux is used to set default permissions for files or directories the user creates.": "$ umask 022",
        "uname command displays system information such as operating system, network node hostname kernel name, version and release etc. Use the -a option to show all the system information" : "$ uname \n $ uname -a",
        "uniq command displays or omits repeated lines from input (or standard input). To indicate the number of occurrences of a line, use the -c option.": "$ uniq file.txt",
        "uptime command shows how long the system has been running, number of logged on users and the system load averages" : "$ uptime",
        "users command shows the user names of users currently logged in to the current host" : "$ users",
    },
    "V": {
        "vim (Vi Improved) popular text editor on Unix-like operating systems. It can be used to edit all kinds of plain text and program files.": "$ vim file"
    },
    "W": {
        "w command displays system uptime, load averages and information about the users currently on the machine, and what they are doing (their processes)" : "$ w",
        "wall command is used to send/display a message to all users on the system" : "$ wall “This is ConvertAnyThing – Linux How Tos”",
        "watch command runs a program repeatedly while displaying its output on fullscreen. It can also be used to watch changes to a file/directory." : "$ watch -d ls -l",
        "wc command is used to display newline, word, and byte counts for each file specified, and a total for many files." : "$ wc filename",
        "wget command is a simple utility used to download files from the Web in a non-interactive (can work in the background) way": "$ wget http://example.com/file.txt",
        "whatis command searches and shows a short or one-line manual page descriptions of the provided command name(s)" : "$ whatis wget",
        "which command displays the absolute path (pathnames) of the files (or possibly links) which would be executed in the current environment." : "$ which who",
        "who command shows information about users who are currently logged in" : "$ who",
        "whereis command helps us locate the binary, source and manual files for commands." : "$ whereis cat",
    },
    "X": {
        "xargs command is a useful utility for reading items from the standard input, delimited by blanks (protected with double or single quotes or a backslash) or newlines, and executes the entered command.": "$ find /path/to/dir -name '*.txt' | xargs grep 'error'"
    },
    "Y": {
        "yes command is used to display a string repeatedly until when terminated or killed using [Ctrl + C]": "$ yes 'y'",
        "youtube-dl is a lightweight command-line program to download videos and also extract MP3 tracks from YouTube.com and a few more sites." : "$ youtube-dl --list-formats https://www.youtube.com/watch?v=iR",
    },
    "Z": {
        "zcmp and zdiff minimal utilities used to compare compressed files" : "$ zcmp domain-list.txt.zip basic_passwords.txt.zip \n$ zdiff domain-list.txt.zip basic_passwords.txt.zip ",
        "zip is a simple and easy-to-use utility used to package and compress (archive) files.": "$ zip -r archive.zip /path/to/dir \n$ tar cf - . | zip | dd of=/dev/nrst0 obs=16k \n$ zip inarchive.zip foo.c bar.c --out outarchive.zip \n$ tar cf - .| zip backup -",
        "zz command is an alias of the fasd commandline tool that offers quick access to files and directories in Linux. It is used to quickly and interactively cd into a previously accessed directory by selecting the directory number from the first field" : "$ zz",
    }
}


# Define a function to display the commands for a given alphabet page
def display(page):
    with st.expander(f"Linux Commands - {page}"):
#         st.write("### Commands:")
        if page in commands:
            for command, example in commands[page].items():
                st.write(f"#### `{command}`")
                st.code(example)
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
            # if st.button(letter, key=letter):
            display(letter)
            st.write(f'<style>.stButton#{letter} {{{button_style}}}</style>', unsafe_allow_html=True)
        else:
            st.write(letter)


alphabet_selector()







