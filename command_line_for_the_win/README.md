this project is called "Command line for the win", we suppose to play a game challenging about Bash skills, as each task is completed, the name of that task will turn green.
Next, we should create a screenshot, showing that we've completed the required levels, and then we will push this screenshot
with the right name to GitHub, in either the PNG or JPEG format.

those are the steps i followed to Transfer Files from my local machine to the remote server:
1/ i took the screenshots of the challenging game and then save them into seperate sub-directories in my local machine, from 1 to 9, 10 to 18, and finally 19 to 27.
2/ i opened a prompet, (i usually use MobaXterm), i copied the SFTP host and username from the sandbox environment.
(to locate local files we use lls, and to change directory in the local machine, we use lcd)

3/ i change the current directory in the remote server to (alx-system_engineering-devops/command_line_for_the_win), and then change the local directory to the one where i have put the files i want to transfer

4/ i run the command put -R sub_directory_name

4/ Once the screenshots are transferred, i pushed the files to Github
