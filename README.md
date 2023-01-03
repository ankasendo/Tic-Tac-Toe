# Portfolio project - 3 Python

# Tic Tac Toe

Tic Tac Toe is a python terminal game, which runs in the Code Institute mock terminal on Heroku

# Introduction

Tic Tac Toe is a game where two players each take turns in choosing either an 'X' or an 'O' in one square of a grid consisting of nine squares, in this case the game is against the computer. The first player who gets 3 of the same letters('X' or 'O') wins the game this is achieved by having the same letters in horizontally, vertically or diagonally.

[Click here for live version of my project](https://p3tic-tac-toe.herokuapp.com/)

[Click here to check my GitHub repository](https://github.com/ankasendo/Tic-Tac-Toe)

![AmIResponsive](/images/responsive.png)

# Table of contents
1. [UX](#ux "UX")
    * [User Stories](#userstories "User Stories")
2. [Features](#features)
    * [Run programme](#run-programme)
    * [Name input](#name-input)
    * [Start game](#start-game)
    * [Game over](#game-over)
3. [Technology used](#technology-used)
4. [Testing](#testing)
5. [Bugs](#bugs)
6. [Deployment](#deployemnt)
7. [Credits](#credits)
8. [Acknowledgement](#acknowledgement)

# UX:

## As a player

- I want to play a game with clear and easy instructions
- I want to be able to see my scores
- I want to be able to play the game again or quit easily 

## Aims 

- For visitors who visit the website to have a positive user experience, despite them not being greeted with much HTML and CSS styling.

- For the game to be enjoyable and allow the users to win.

## Flow Chart
To create the structure of the game, this diagram was created using [Lucid Charts](https://www.lucidchart.com/)
![Flow Chart](images/Flowchart.png)

# Features

## Run programme
Once the program runs, the user is welcomed to the game and they are asked them to insert their name. I used sleep method so the welcome message appears word by word. The game instructions appear so the user will know how to play the game and also a referecne board so the user will know how to input their chosen letter('X' or 'O').

![screenshot](images/first%20.png)

## Name input
The user will be asked what their name is.

![screenshot](images/first-page-full.png)


## Start game 
After the user has entered their name a welcome message will appear and it will ask the user to type 'p' to play the game, a loading message will then appear saying 'game starting', the game board will then appear and ready for the user to play. Reference board is kept throughout the game for the purposes of better understaniding of the same. 

![screenshot](images/3%20reference%20board.png)

## Game over
After the game is ended in a win, lose or a draw, a game over message will appear and it will ask the user if the want play again. 

![screenshot](images/final.png)

# Technology used 
- [Python](https://www.python.org/):
    - Python is the core programming language used to write all of the code in this application to make it fully functional.
- [GitHub](https://github.com/dashboard):
    - Used to store code for the project after being pushed.
- [Git](https://git-scm.com/):
    - Used for version control by utilizing the GitPod terminal to commit to Git and push to GitHub.
- [GitPod](https://gitpod.io/workspaces):
    - Used as the development environment.
- [Heroku](https://heroku.com/):
    -Used to deploy my application.
- [Lucid Chart](https://lucid.app/users/login#/login):
    - Used to create my flow chart of the story.
- [Pep8](https://pep8ci.herokuapp.com/#):
    - Used to check my code against Pep8 requirements.
- JavaScript provided in the Code Institute Template
- HTML provided in the Code Institute Template

# Testing
Testing was conducted through out my entire project, mostly manually. Pep8 validator initialy showed some errors, but after few fixes the resullt came back with no issues. Initially, I could not use terminal output, as error was showing up, however, after deployment, and line indentation fixing, it all worked as expected.

![screenshot](images/pep8-ci-liner.png)
![screenshot](images/pep8-ci-liner-no%20errors.png)

# Bugs 
I had a few bugs in my code when playing the game, first one occured right after deployement where error message would show up after clicking 'y' to start the game. The error message reffered to three lines on the code, however the problem was resolved by using PEP8 validator and analising code line by line. 


# Deployment
Steps for deployment:
* Create a new heroku app

## Heroku
To deploy this page to Heroku from its [GitHub repository](https://github.com/erykslezak/CIPP3) the following steps were taken:

- Log into or register new account at [Heroku](https://www.heroku.com/).
- Click the button **New** in top right corner of the dashboard.
- From the drop-down menu select **Create new app**.
- Enter your apps name in the first field and select your region.
- Click on **Create App** if you are happy with your choices.
- Once you the app is made you will see yourself within **Deploy** tab. Press on **Settings** tab.
- Once you are in the **Settings** tab scroll down till you find **Config Vars**.
- Press the button **Reveal Config Vars** and for 'KEY' field, type in PORT and for the value field type in '8000'.
Press the **Add** button.
- Scroll down to **Buildpacks**. Click the button **Add buildpack** and select 'python'. Do the same step and add 'node.js'.
**PYTHON MUST BE ON TOP OF THE BUILDPACKS. IF IN YOUR CASE NODE.JS IS FIRST, CLICK AND DRAG PYTHON TO TOP AND SAVE.**
- Return back to the **Deploy** tab. From the deployment method, select 'Github' as the deployment.
- You will be asked to connect your github account. Confirm and proceed.
- Search for your repository name and connect.
- Once that is done and successfully connected, select how you want to push updates from the following options.

  _Clicking **Enable Automatic Deploys**. This will update once you push updates to your Github._

  _Selecting the correct branch for deployment from drop-down menu and pressing **Deploy Branch** button. This will have to be done everytime manually._



# Credits 

* Stack Overflow
* [W3 School](https://www.w3schools.com/) helped me with my research and understanding.
* Youtube
* [Am I Responsive](https://ui.dev/amiresponsive) to create the main image for README file.
* [GeekFlare website](https://geekflare.com/tic-tac-toe-python-code/)
* [GeekforGeeks website](https://www.geeksforgeeks.org/python-implementation-automatic-tic-tac-toe-game-using-random-number/)

## Python Libraries Used

* [Random](https://docs.python.org/3/library/random.html)  for computer random moves 
* [Time and Sleep](https://realpython.com/python-sleep/) for text animation / disappearence
* [Sys](https://docs.python.org/3/library/sys.html)  for specific parameters and functions


 # Acknowledgement
 I would like to thank;
 
 * The slack community (https://slack.com/intl/en-ie/https://slack.com/intl/en-ie/) which i can always rely on.
 * I would like to thank the assessment team for taking their time to look over my project, Code institute Tutors and Love Sanwiches guided project.
 * Questions and answers by fellow students on Slack were heavily consulted.

