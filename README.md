# NBA Stats Capstone Project
**Capstone Project 1 for Springboard**

## Introduction
This project involves using the [ball don't lie API](https://ball-dont-lie.herokuapp.com/) to gather NBA stats and display then in different pages. Namely, this site includes:
- A homepage with recent NBA games
- Game pages with the box score
- Team pages with latest games
- Player pages with stats of latest games and season average

## Libraries & Installation
All Python libraries are located in the file `requirements.txt`. 
    pip install - requirements.txt
Note: The rendered webpages use JS libraries that reference Bootstrap, Font Awesome, jQuery, and Axios

## API
The balldontlie API can be used to query NBA stats and information, updated once every ~10 minutes. The API can be accessed via applications like [Insomnia](https://insomnia.rest/) or [Postman](https://www.postman.com/)
- Players - **GET** `https://www.balldontlie.io/api/v1/players`
- Teams - **GET** `https://www.balldontlie.io/api/v1/teams`
- Games - **GET** `https://www.balldontlie.io/api/v1/games`
- Game Stats - **GET** `https://www.balldontlie.io/api/v1/stats`
- Season Averages - **GET** `https://www.balldontlie.io/api/v1/stats`
For more information, go refer to [the website](https://www.balldontlie.io/#introduction)
