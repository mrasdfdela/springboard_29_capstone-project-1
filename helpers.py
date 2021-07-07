from flask import Flask, jsonify
import requests
from datetime import datetime, timedelta

from models import User, FavTeam, FavPlayer

import pdb

def get_player_by_id(id):
    try:
        resp = requests.get(f"https://www.balldontlie.io/api/v1/players/{id}")
        return resp.json()
    except:
        return None

def get_user_favteam_ids(user_id):
    teams = User.query.get(user_id).favteams
    team_ids = [ team.team_id for team in teams ]
    return team_ids

def get_user_favplayer_ids(user_id):
    players = User.query.get(user_id).favplayers
    player_ids = [ player.player_id for player in players ]
    return player_ids

def get_team_by_id(id):
    try:
        resp = requests.get(
          f"https://www.balldontlie.io/api/v1/teams/{id}",
        )
        return resp.json()
    except:
        return None

def get_recent_games(days):
    try:
        start_date = datetime.now() - timedelta(days=days)
        resp = requests.get(f"https://www.balldontlie.io/api/v1/games",
            params = {
                "start_date":start_date.strftime("%Y-%m-%d")
            })
        return resp.json()
    except:
        return None

def str_to_date(str):
    date = datetime.strptime(str, "%Y-%m-%dT%H:%M:%S.%fZ")
    return date.strftime("%A, %B %d")

def convert_gameday_format(games):
    new_games = games
    for game in new_games:
        game['date'] = str_to_date(game['date'])
    return new_games


def serialize_player(player_json):
    return {
      "id": player_json['id'],
      "first_name": player_json['first_name'],
      "last_name": player_json['last_name']
    }