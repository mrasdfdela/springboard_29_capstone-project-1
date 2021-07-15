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
  <strong>GET </strong> https://www.balldontlie.io/api/v1/players</br>
  <img src="https://user-images.githubusercontent.com/33531005/125836556-ddcd47c6-d926-4773-b32c-9256f13e97d7.png">
</details>
<details>
  <summary>Teams</summary>
  <strong>GET </strong> https://www.balldontlie.io/api/v1/teams
  <img src="https://user-images.githubusercontent.com/33531005/125837381-da6f93ed-70c5-4926-96d1-85ec0995ff02.png">
</details>
<details>
  <summary>Games</summary>
  <strong>GET </strong> https://www.balldontlie.io/api/v1/games
  <img src="https://user-images.githubusercontent.com/33531005/125836877-3829e778-3fc9-4cd3-ba1c-e645d1e6942d.png">
</details>
<details>
  <summary>Stats</summary>
  <strong>GET </strong> https://www.balldontlie.io/api/v1/stats
  <img src="https://user-images.githubusercontent.com/33531005/125837145-f84ec997-1435-497f-b980-cf1ffcec1840.png">
</details>
<details>
  <summary>Season Averages</summary>
  <strong>GET </strong> https://www.balldontlie.io/api/v1/season_averages
  <img src="https://user-images.githubusercontent.com/33531005/125837229-1dae8691-75c8-4447-af0e-05280261ac8c.png">
</details>
For more information, go refer to [the website](https://www.balldontlie.io/#introduction)

## 
