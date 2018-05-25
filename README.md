# PASSWORD LOCKER
### By Murungi Kirima
This project was generated with Python3.6

## Prerequisites
* You will need to have python3 or python3.6 installed on your machine.
* On the terminal copy the following individual commands on your console.
```
$ sudo add-apt-repository ppa:jonathonf/python-3.6
$ sudo apt-get update
$ sudo apt-get install python3.6
```
* Confirm installation:
```
$ python3.6

Python 3.6.0 (default, Nov 17 2016, 17:05:23)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>

>>>exit()
```

## Usage
* On the terminal copy the following individual commands on your console:
```
$ git clone https://github.com/murungiKirima/password_locker.git
$ cd <cloned_folder>
$ python3.6 run.py
```
* Follow the short codes to use the app.

### Running unit tests
For running tests, use the following codes in your terminal:
```
$ python3.6 credentials_test.py
$ python3.6 user_test.py
```

## Bugs.
There is no database to support the app since it is a terminal app. Once you exit or log out of a session you loose all the credentials and the created user account so you will have to create a new user for every session.

## Further help
For additions, submit a pull request and once approved you can make contributions at will. Alternatively contact me at: murungikirima@gmail.com

## License
MIT License.
