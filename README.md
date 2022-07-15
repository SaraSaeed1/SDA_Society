# How to Opent the project

You must have Python and Django virtual environment If you don't have
### Install Python 3 on your computer for Mac users:


To install Python, we will use homebrew, which is a package manager that helps us install software on our operating system. You may have installed homebrew already. To check, run this command in your terminal:

```
~$ brew -vcopy
```
If you get an error, go to [brew.sh](https://brew.sh/) and follow the instructions for installing homebrew.

Now that we have homebrew working, we can install Python:

```
~$ brew update		    # update homebrew
~$ brew install python3	    # install Python 3
```

Updating and installation might take a few minutes. If there are any other problems, homebrew helps us out by telling us certain commands we might need to run to properly install things. Read through the outputs and run the recommended commands. Otherwise, we can check the version to see if it installed:

```
~$ python3 -V         # type this commandcopy
```

You should see a version number like ```Python 3.6.5``` (version numbers may be slightly different). If you get an error, consult with your instructor.


### Run the virtual environment

inide the volder of the project, run this command in your terminal:


```
python manage.py migrate
```

```
python manage.py runserver
```

