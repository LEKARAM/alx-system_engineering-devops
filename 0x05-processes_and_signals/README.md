0-what-is-my-pid 1-list_your_processes 2-show_your_bash_pid 3-show_your_bash_pid_made_easy 4-to_infinity_and_beyond 5-kill_me_now 6-kill_me_now_made_easy 7-highlander 8-beheaded_process 9-process_and_pid_file 10-manage_my_process 11-zombie.c 12-screencast_unix_signal

Linux PID
Linux process
Linux signal

man: ps, pgrep, pkill, kill, exit

help: trap

For those who want to know more and learn about all signals, check out this article.

At the end of this project you are expected to be able to explain, without the help of Google:

What is a PID
What is a process
How to find a process PID
How to kill a process
What is a signal
What are the 2 signals that cannot be ignored
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 14.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing
Write a Bash script that displays its PID.

GitHub repository: holberton-system_engineering-devops
Directory: 0x05-processes_and_signals
File: 0-what-is-my-pid
Write a Bash script that displays a list of currently running processes.

Requirements:

Must show all processes, for all users, including those which might not have a TTY
Display a user-oriented format
Show process hierarchy
GitHub repository: holberton-system_engineering-devops
Directory: 0x05-processes_and_signals
File: 1-list_your_processes
Using your previous exercise command, write a Bash script that displays line containing the bash word, this allowing you to easily get the PID of your Bash process

Requirements:

You cannot use pgrep
The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error here)
Here we can see that my Bash PID is 4404.

GitHub repository: holberton-system_engineering-devops
Directory: 0x05-processes_and_signals
File: 2-show_your_bash_pid
Write a Bash script that displays the PID, along with the process name, of processes which name contains the word bash.

Requirements:

You cannot use ps
Here we can see that:

For the first iteration: bash PID is 4404 and that the 3-show_your_bash_pid_made_easy script PID is 4555
For the second iteration: bash PID is 4404 and that the 3-show_your_bash_pid_made_easy script PID is 4557
GitHub repository: holberton-system_engineering-devops
Directory: 0x05-processes_and_signals
File: 3-show_your_bash_pid_made_easy
Write a Bash script that displays To infinity and beyond indefinitely.

Requirements:

In between each iteration of the loop, add a sleep 2
Note that I ctrl+c (killed) the Bash script in the example.

GitHub repository: holberton-system_engineering-devops
Directory: 0x05-processes_and_signals
File: 4-to_infinity_and_beyond
We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

Write a Bash script that kills 4-to_infinity_and_beyond process.

Requirements:

You must use kill
Terminal #0

Terminal #1

I opened 2 terminals in this example, started by running my 4-to_infinity_and_beyond Bash script in terminal #0 and then moved on terminal #1 to run 5-kill_me_now. We can then see in terminal #0 that my process has been terminated.

GitHub repository: holberton-system_engineering-devops
Directory: 0x05-processes_and_signals
File: 5-kill_me_now
Write a Bash script that kills 4-to_infinity_and_beyond process.

Requirements:

You cannot use kill or killall
Terminal #0

Terminal #1
