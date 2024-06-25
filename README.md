# sina-email-migrator

## What is this?
A selenium python script that helps you automatically download all your Sina emails as EML files.

## In what case do you want to use this?
* You have login credentials to your Sina email 
* And for any reason, you are unable to turn on smtp/imap/pop3 for your email. 
   * An example is you don't have an active China mainland phone number

## How to use this?
* Have python3, firefox and geckodriver installed on your computer
* `git clone https://github.com/robosharkler/sina-email-migrator.git`
* `cd sina-email-migrator`
* `python -m venv`
* `pip install -r requirements.txt`
* `python app.py >> log.txt`
* A firefox window should pop up. Sign in in to your sina email account. Go back to the terminal where you run the `app.py`, press enter

## Why I write this
For the education and experiment purposes only