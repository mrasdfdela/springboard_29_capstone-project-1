# NBA Stats Capstone Project
**Capstone Project 1 for Springboard**

## Introduction
This project uses the [ball don't lie API](https://ball-dont-lie.herokuapp.com/) to gather NBA stats and display them in different pages. Namely, this site includes:
- A homepage with recent NBA games
- Game pages with the box score
- Team pages with their latest games
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
  <strong>GET </strong> https://www.balldontlie.io/api/v1/teams</br>
  <img src="https://user-images.githubusercontent.com/33531005/125837381-da6f93ed-70c5-4926-96d1-85ec0995ff02.png">
</details>
<details>
  <summary>Games</summary>
  <strong>GET </strong> https://www.balldontlie.io/api/v1/games</br>
  <img src="https://user-images.githubusercontent.com/33531005/125836877-3829e778-3fc9-4cd3-ba1c-e645d1e6942d.png">
</details>
<details>
  <summary>Stats</summary>
  <strong>GET </strong> https://www.balldontlie.io/api/v1/stats</br>
  <img src="https://user-images.githubusercontent.com/33531005/125837145-f84ec997-1435-497f-b980-cf1ffcec1840.png">
</details>
<details>
  <summary>Season Averages</summary>
  <strong>GET </strong> https://www.balldontlie.io/api/v1/season_averages</br>
  <img src="https://user-images.githubusercontent.com/33531005/125837229-1dae8691-75c8-4447-af0e-05280261ac8c.png">
</details>
For more information, go refer to [the website](https://www.balldontlie.io/#introduction)

## Pages
- Pages for signing up, logging in, and editing the user
    - Signup requires a username, email, and password
    - Signing in allows users to "like" and add record notes about their favorite teams.
    - Users can update their username and email in the *Edit User* page
- A homepage with recent NBA games
    - Includes links to the respective team pages and game details
- Game pages with the box score
    - Includes links to the respective team pages and player pages
- Team pages with their latest games
    - Includes links to game pages
    - Also includes a section for (signed in users) to add notes about the team
- Player pages with stats of latest games and season average
    - Includes links to team page
    - Also includes a section for (signed in users) to add notes about the player

## Endpoints
Endpoints can be roughly categorized by 1) User 2) Show 3) Like/Unlike
- User
    -  `/login`
    -  `/logout`
    -  `/user/edit` - displays a form for editing a User's username or email
- Show
    -  `/` - returns the homepage
    -  `/user/{user_id}` - returns lists of user's favorite teams and players
    -  `/player/{player_id}` - returns the player page or posts a user note about the player
    -  `/team/{team_id}` - returns the team page or posts a user note about the team
    -  `/game/{game_id}` - returns the game page
- Like / Unlike
    -  `/user/{user_id}/fav_player` - post/delete routes adding/removing a favorite player
    -  `/user/{user_id}/fav_team` - post/delete routes adding/removing a favorite team

## Technologies
This site uses a Flask stack and includes these libraries:
- PostgreSQL/Flask-SQLAlchemy
- bcrypt/Flask-Bcrypt
- WTForms/Flask-WTF
- Requests
- Bootstrap
- Font Awesome
- jQuery
- Axios
