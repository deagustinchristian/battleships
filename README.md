# Battleships

Battleships is a Python terminal game, which runs via Code Institutes mock terminal on Heroku.

Players can try to beat the computer by destroying the computer's battleships before running out of missiles. Players start with 15 missiles and the computer has randomly placed 6 battleships. Each battleship occupies one square on the board.

[Here is the live version of my game](https://cda-battleships.herokuapp.com/)

![Looking good on different devices](https://raw.githubusercontent.com/deagustinchristian/battleships/main/assets/images/terminal.png)

## How to Play

My version of Battleships is a bit different from the original pen-and-paper game. In this version, the players objective is to destroy the computers randomly placed battleships.

A hit is marked with an X and a miss is marked with an -. The player starts with 15 missiles and the computer has 6 battleships placed randomly on the board.

The player wins the game if all ships are destroyed before running out of missiles.

## Features 

### Existing Features

- Randomly placed battleships

    - The computer battleships are randomly placed on the board
    - The player cannot see the computer's ships
    - Play against the computer
    - Accepts user input
    - Missiles amount decrease after each try

![A hit and a miss](https://raw.githubusercontent.com/deagustinchristian/battleships/main/assets/images/hitmiss.jpeg)

- Input validation and error checking
    - Player cannot enter coordinates outside of the grid
    - For the rows player has to enter numbers
    - For the columns player has to enter letters
    - Player cannot enter same guess twice

![Same try twice](https://raw.githubusercontent.com/deagustinchristian/battleships/main/assets/images/sametrytwice.jpeg)

- Game asks player if they wish to try again

![Wanna try again](https://raw.githubusercontent.com/deagustinchristian/battleships/main/assets/images/Endgame.jpeg)

### Features Left to Implement

- A future idea to implement would be to add functions so that ships of different sizes could be added to the board.

- Make the board larger

- Decrease the number of missiles to make the game even harder

- Add a player board so that the computer can hunt the player's battleships

## Data Model

I used a class as my model because that's what I first saw in the Code Institute video


## Testing 

I have manually tested this game by doing the following:

- Passed the code through PEP8 and confirmed there are no problems with the code

- Given invalid inputs, numbers where it asked for letters and letters when the game asks for numbers, same input twice

- Tested the game both in my local terminal and the Code Institute Heroku terminal


### Validator Testing 

- PEP8

![PEP8](https://raw.githubusercontent.com/deagustinchristian/battleships/main/assets/images/PEP8.jpeg)

###  Bugs
- When I first ran my code through PEP8 I almost fainted, a lot of indentation mistakes and too long code I eventually had to rename player_guess_board to just player_board for PEP8 to accept it

- I had issues with how to shorten the code but learned that () can help shorten the code without affecting it

As far as I know, there are no unfixed bugs. 

## Deployment
 
This project was deployed using Code Institute´s mock terminal for Heroku.

- Steps for deployment: 
  - Fork or clone this repository
  - Create a new Heroku app
  - Set the buildbacks to Python and NodeJS, in that order
  - Link the Heroku app to the repository
  - Click deploy

[Here is the live version of my game](https://cda-battleships.herokuapp.com/) 


## Credits 


### Content 

- All text on the website was made up by me. I used Grammarly on this ReadMe file just so the grammar and spelling were as correct as possible.

- I have used different sources to learn and understand the coding and the concepts of Python, to better understand the concepts of the game and how to make it I studied the following websites and how they did it.

    - Code Institute - Battleship game video.
        - (https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/)


    - I got the idea of using letters instead of numbers for the columns from this persons Github and used part of his code for it.
        - (https://github.com/dmoisset/battleship-dojo/blob/master/battleship.py)


    - This Youtube channel was really good to get a sense of how the game can be built and very good explanations on how everything works, I built the game after following his steps.
        - (https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=0s)


    - I learned more about Python Classes via W3Scools.
        - (https://www.w3schools.com/python/python_classes.asp)


    - My mentor showed me how to shorten code without breaking it.
