# WhatCanWePlayTogether

This tool helps you with the problem of finding games which you can play together with your friends.

## Set-Up

### Requirements
* [steamapi python library](https://github.com/smiley/steamapi)
* Flask: `pip install flask`

### Run the application
Start the flask app: `python main.py`

Go to "localhost:5000/user/$yoursteamnickname" and select all of you friends which are part of the group.
On submit the tool will find all games which are present in all of your Steam librarys

## ToDo
- Code cleanup :D
- Some nicer HTML/CSS
- try/except to catch private Steam profiles
- Only consider games with multiplayer? 
