# NBA Stats Capstone Project
**Capstone Project 1 for Springboard**

## Introduction
This project involves using the [ball don't lie API](https://ball-dont-lie.herokuapp.com/) to gather NBA stats and display then in different pages. Namely, this site includes:
-A homepage with recent NBA games
- Game pages with the box score
- Team pages with latest games
- Player pages with stats of latest games and season average
- Pages for signing up, logging in, and editing the user

## Libraries & Installation
All Python libraries are located in the file `requirements.txt`. 
> pip install - requirements.txt

Note: The rendered webpages use JS libraries that reference Bootstrap, Font Awesome, jQuery, and Axios

## API
The balldontlie API can be used to query NBA stats and information, updated once every ~10 minutes. The API can be accessed via applications like [Insomnia](https://insomnia.rest/) or [Postman](https://www.postman.com/)
<details>
  <summary>Players</summary>
  ## Heading
  **GET** `https://www.balldontlie.io/api/v1/players`
</details>
<details>
  <summary>Teams</summary>
  **GET** `https://www.balldontlie.io/api/v1/teams`
</details>
<details>
  <summary>Games</summary>
  **GET** `https://www.balldontlie.io/api/v1/games`
</details>
<details>
  <summary>Stats</summary>
  **GET** `https://www.balldontlie.io/api/v1/stats`
</details>
<details>
  <summary>Season Averages</summary>
  **GET** `https://www.balldontlie.io/api/v1/season_averages`
</details>
For more information, go refer to [the website](https://www.balldontlie.io/#introduction)

## 
