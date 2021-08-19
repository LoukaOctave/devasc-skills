# NETACAD-DEVASC SKILLS-BASED EXAM SEP 2021

## Task 1 -- GitHub Skills Test
### Task preparation
GitHub account and working virtual machine needed.
### Task implementation
1. I created a directory using ```mkdir Devasc_Skills``` and then initialised a local git repository with ```git init``` inside that newly created directory.
2. Each time a task was completed I added the relevant files into the folder.
3. I created a remote GitHub repository in my web browser and then connected my local repository to it using ```git remote add origin https://github.com/LoukaOctave/devasc-skills.git```, ```git fetch origin```, and ```git checkout main```. In this step I needed to authenticate myself using my credentials.
4. In order to upload files to the repository I needed to stage them using ```git add [file]```, commit them using ```git commit``` and then push those commits to the remote with ```git push```. After commiting but before pushing, I would tag them. For this I would create a tag using ```git tag [task-#]```, and share that tag using ```git push origin [tag]```.
5. After every step I took screenshots of my work/results.
6. The README.md file was automatically created when I made the repository. I kept it up-to-date by editing it in the default text editor.
### Task troubleshooting
In step 3 I encountered a warning which said that support for password authentication was removed on August 13, 2021. I followed the instructions listed right after and created a personal access token in my GitHub developer settings, which I used to complete the task.
### Task verification
After fetching the origin for the first time, the README.md file - that only existed on the remote - appeared in my local repository. After completing more tasks and uploading them, the pushed commits could be seen on the remote repository (see screenshots).

## Task 2 -- Ansible Skills Test
### Task preparation
A working virtual machine is needed with Ansible installed on it.
### Task implementation
1. I connected to my DEVASC VM.
2. I created an Ansible playbook in VS code and wrote the script. The script contains 3 tasks and 2 handlers:
    * INSTALL NTP: Will use ```apt-get install``` to install the latest version of ```ntp```. This command will be preceded by ```apt-get update```.
    * VERIFY INSTALLATION: Will output the version of ntp, which tells us that ntp has been installed.
    * SET NTP SERVER POOLS: Will overwrite ```/etc/ntp.conf``` and modify its list of pools with ones I picked online. This task will trigger ```RESTART NTP SERVER```.
    * RESTART NTP SERVER: Will restart the ntp server. This handler will trigger ```CHECK NTP SERVER STATUS```.
    * CHECK NTP SERVER STATUS: Will output the status of the ntp server using ```service ntp status```.
3. I named the playbook "ntp_install".
4. I ran the playbook in my VM using ```ansible-playbook -v ntp_install.yaml```.
5. After running the playbook, I verify that it was successful by looking at the output in my terminal. As can be seen in the screenshots: the ntp server has been installed, configured and (re)started.
### Task troubleshooting
In the playbook, I couldn't use the ```service``` module to output the ntp status, so I used ```command``` instead and added ```warn=false``` as an argument to hide warnings.
### Task verification
After running the playbook with verbose, I get several indicators that the tasks were successfully completed (see screenshots).
* ```VERIFY INSTALLATION``` does indeed display the version number for ntp on our machine, which means it is now present on it.
* ```CHECK NTP SERVER STATUS``` shows ntp as active and running, which means it is as intended.
* ```PLAY RECAP``` shows no failed tasks, which means that none of the things we tried to do were unsuccessful.

## Task 3 -- Docker
### Task preparation
A working virtual machine is needed with Docker installed on it, along with a Docker ID.
### Task implementation
1. I wrote a Dockerfile that performs a configuration identical to the one in the Ansible playbook from an Ubuntu image that has the latest version of Apache2 installed onto it. In that Dockerfile I also ```EXPOSE``` the port number Apache is running on so that it can be accessed in our localhost.
I then wrote a bash script that will create this Dockerfile, build an image of it, and run a container of that image; on any machine.
2. The port that Apache will run on and that will be exposed from the container can be passed as an argument using ```--build-arg PORT=[number]```, because it is defined inside the Dockerfile with ```ARG```. Of course this is optional, as a default value of ```8081``` is already assigned to ```PORT``` in the Dockerfile.
I made it so that our bash script can take an optional argument when executed from the command line, and that it feeds its value - if any exists - into our Dockerfile.
3. I took a screenshot where you can see the code for my bash script along with a terminal window running the script, and a browser window showing the result of my work.
### Task troubleshooting
I've had some issues while trying to use ```CMD``` in my Dockerfile. I wanted to use it in order to (re)start Apache whenever I run a container of my image. Sadly, it only kept giving me errors so I ditched it. At that moment, I did discover that i did not really need it, because Apache starts up by itself when a container is created.
### Task verification
Verifying that everything worked as intended was pretty straightforward.
* When running the bash script in the terminal, I can tell from the output that my Dockerfile is building an image and that a container is run as soon as that's done. The steps from the Dockerfile are displayed one by one, and then the container ID is shown.
* To make sure my container didn't just crash right away, I can run ```docker ps``` and see that it is still up and running. It also displays the exposed ports, and the ports they have been forwarded to.
* Now comes the last step: I can either ```curl``` or browse to ```http://localhost:[forwarded_port]``` to see the Apache2 default page in HTML format.
* Additionally, if I enter my container's shell, I can ```cat /etc/apache2/ports.conf``` and ```cat /etc/apache2/sites-available/000-default.conf``` to check that the correct port number has been set in both of these files.