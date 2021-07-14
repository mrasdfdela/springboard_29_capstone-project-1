from flask import Flask, jsonify
import requests
from datetime import datetime, timedelta

from models import User, FavTeam, FavPlayer

import pdb

# Query players, teams, and games
def get_player_by_id(id):
    try:
        resp = requests.get(f"https://www.balldontlie.io/api/v1/players/{id}")
        return resp.json()
    except:
        return None

def get_team_by_id(id):
    try:
        resp = requests.get(
          f"https://www.balldontlie.io/api/v1/teams/{id}",
        )
        return resp.json()
    except:
        return None

def get_game_by_id(id):
    try:
        resp = requests.get(
          f"https://www.balldontlie.io/api/v1/games/{id}")
        return resp.json()
    except:
        return None

# Get user favorites
def get_user_favteam_ids(user_id):
    teams = User.query.get(user_id).favteams
    team_ids = [ team.team_id for team in teams ]
    return team_ids

def get_user_favplayer_ids(user_id):
    players = User.query.get(user_id).favplayers
    player_ids = [ player.player_id for player in players ]
    return player_ids

# Get game and player stats
def get_recent_games_by_days(days, team_id=None):
    try:
        start_date = datetime.now() - timedelta(days=days)
        resp = requests.get(
            f"https://www.balldontlie.io/api/v1/games",
            params = {
                "start_date":start_date.strftime("%Y-%m-%d"),
                "team_ids[]":team_id
            })
        data = resp.json()['data']
        filtered_data = filter_recent_games(data)
        return sort_recent_games(filtered_data)
    except:
        return None

def sort_recent_games(data):
    sorted_data = sorted(data, key=lambda x: datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%fZ"), reverse=True)
    return sorted_data

def filter_recent_games(data):
    return filter(lambda d: d['home_team_score'] != 0, data)

def get_game_stats(id):
    try:
        resp = requests.get(
          f"https://www.balldontlie.io/api/v1/stats",
          params = {
              "game_ids[]": id
          })
        return resp.json()
    except:
        return None

def get_player_stats_seas(id):
    year = get_season_yr()
    records = 55
    player_stats = []

    current_page = -1
    total_pages = 1
    try:
        while current_page != total_pages:
          resp = get_player_stats(id,year,records)
          player_stats.extend(resp.json()['data'])
          current_page = resp.json()['meta']['current_page']
          total_pages = resp.json()['meta']['total_pages']
    except:
        return []
    return sort_player_stats(player_stats)

def get_player_stats(player_id, year, records):
    try:
        resp = requests.get(
            f"https://www.balldontlie.io/api/v1/stats",
            params = {
                "player_ids[]": player_id,
                "seasons[]": year,
                "per_page":records
            })
        return resp
    except:
        return None

def sort_player_stats(data):
    sorted_data = sorted(data, key=lambda x: datetime.strptime(x['game']['date'], "%Y-%m-%dT%H:%M:%S.%fZ"), reverse=True)
    return sorted_data

def get_seas_avgs(id):
    try:
        resp = requests.get(f"https://www.balldontlie.io/api/v1/season_averages",
        params = {
          "player_ids[]": [id]
        })
        return resp.json()['data']
    except:
        return None

# Date formatters
def str_to_date(str):
    for dt_format in ("%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%d %H:%M:%S UTC"):
        try:
            date = datetime.strptime(str, dt_format)
        except:
            pass
    return date.strftime("%A, %B %d")

def convert_games_date_format(games):
    for game in games:
        game['date'] = str_to_date(game['date'])
    return games

def convert_player_gm_dt_fmt(player_games):
    for p_gm in player_games:
        p_gm['game']['date'] = str_to_date(p_gm['game']['date'])
    return player_games

def get_season_yr():
    curr_yr = datetime.now().year
    seas_start = datetime(curr_yr, 10, 18)
    # pdb.set_trace()
    if datetime.now() > seas_start:
        return datetime.now().year
    else:
        return datetime.now().year - 1


# def get_recent_games(days):
#     year = get_season_yr()
#     records = 20
#     game_stats = []

#     current_page = 0
#     try:
#         while len(game_stats) < 10:
#             resp = get_game_stats(current_page,records,year)
#             if current_page == 0:
#                 current_page = resp['meta']['total_page']
#             else:
#                 game_stats.extend(resp)
#                 current_page = current_page - 1

#         return resp.json()
#     except:
#         return None

# def get_game_stats(page,records,year):
#     try:
#         resp = requests.get(
#             f"https://www.balldontlie.io/api/v1/games",
#             params = {
#                 "page":page,
#                 "per_page":records,
#                 "seasons[]": year
#             })
#         return resp
#     except:
#         return None