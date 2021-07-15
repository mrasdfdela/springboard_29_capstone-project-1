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
  {
  "data":[
    {
      "id":237,
      "first_name":"LeBron",
      "last_name":"James",
      "position":"F",
      "height_feet": 6,
      "height_inches": 8,
      "weight_pounds": 250,
      "team":{
        "id":14,
        "abbreviation":"LAL",
        "city":"Los Angeles",
        "conference":"West",
        "division":"Pacific",
        "full_name":"Los Angeles Lakers",
        "name":"Lakers"
      }
    }
    ...
 ],
 "meta": {
    "total_pages": 50,
    "current_page": 1,
    "next_page": 2,
    "per_page": 25,
    "total_count": 9999
  }
}
</details>
<details>
  <summary>Teams</summary>
  <strong>GET </strong> https://www.balldontlie.io/api/v1/teams
  {
  "data": [
    {
      "id":14,
      "abbreviation":"LAL",
      "city":"Los Angeles",
      "conference":"West",
      "division":"Pacific",
      "full_name":"Los Angeles Lakers",
      "name":"Lakers"
    },
    ...
  ],
  "meta": {
    "total_pages": 1,
    "current_page": 1,
    "next_page": null,
    "per_page": 30,
    "total_count": 30
  }
}
</details>
<details>
  <summary>Games</summary>
  <strong>GET </strong> https://www.balldontlie.io/api/v1/games
  {
  "data": [
    {
      "id":1,
      "date":"2018-10-16T00:00:00.000Z",
      "home_team_score":105,
      "visitor_team_score":87,
      "season":2018,
      "period": 4,
      "status": "Final",
      "time": " ",
      "postseason": false,
      "home_team":{
        "id":2,
        "abbreviation":"BOS",
        "city":"Boston",
        "conference":"East",
        "division":"Atlantic",
        "full_name":"Boston Celtics",
        "name":"Celtics"
      },
      "visitor_team":{
        "id":23,
        "abbreviation":"PHI",
        "city":"Philadelphia",
        "conference":"East",
        "division":"Atlantic",
        "full_name":"Philadelphia 76ers",
        "name":"76ers"
      },
    },
    ...
  ],
  "meta": {
    "total_pages": 1877,
    "current_page": 1,
    "next_page": 2,
    "per_page": 25,
    "total_count": 46911
  }
}
</details>
<details>
  <summary>Stats</summary>
  <strong>GET </strong> https://www.balldontlie.io/api/v1/stats
  {
  "data": [
    {
      "id":29,
      "ast":2,
      "blk":2,
      "dreb":8,
      "fg3_pct":0.25,
      "fg3a":4,
      "fg3m":1,
      "fg_pct":0.429,
      "fga":21,
      "fgm":9,
      "ft_pct":0.8,
      "fta":5,
      "ftm":4,
      "game":{
        "id":1,
        "date":"2018-10-16T00:00:00.000Z",
        "home_team_id":2,
        "home_team_score":105,
        "season":2018,
        "visitor_team_id":23,
        "visitor_team_score":87
      },
      "min":"36:49",
      "oreb":2,
      "pf":3,
      "player":{
        "id":145,
        "first_name":"Joel",
        "last_name":"Embiid",
        "position":"F-C",
        "team_id":23
      },
      "pts":23,
      "reb":10,
      "stl":1,
      "team":{
        "id":23,
        "abbreviation":"PHI",
        "city":"Philadelphia",
        "conference":"East",
        "division":"Atlantic",
        "full_name":"Philadelphia 76ers",
        "name":"76ers"
      },
      "turnover":5
    },
    ...
  ],
  "meta": {
    "total_pages": 2042,
    "current_page": 1,
    "next_page": 2,
    "per_page": 25,
    "total_count": 51045
  }
}
</details>
<details>
  <summary>Season Averages</summary>
  <strong>GET </strong> https://www.balldontlie.io/api/v1/season_averages
  {
  "data": [
    {
      "games_played":37,
      "player_id":237,
      "season":2018,
      "min":"34:46",
      "fgm":9.92,
      "fga":19.22,
      "fg3m":2.05,
      "fg3a":5.73,
      "ftm":5.08,
      "fta":7.54,
      "oreb":0.95,
      "dreb":7.59,
      "reb":8.54,
      "ast":7.38,
      "stl":1.32,
      "blk":0.65,
      "turnover":3.49,
      "pf":1.59,
      "pts":26.97,
      "fg_pct":0.516,
      "fg3_pct":0.358,
      "ft_pct":0.674
    }
  ]
}
</details>
For more information, go refer to [the website](https://www.balldontlie.io/#introduction)

## 
