import requests
from flask import Flask, jsonify

def get_player_by_id(id):
    try:
      resp = requests.get(f"https://www.balldontlie.io/api/v1/players/{id}")
      return serialize_player(resp.json())
    except:
      return None

def serialize_player(player_json):
    return {
      "id": player_json['id'],
      "first_name": player_json['first_name'],
      "last_name": player_json['last_name']
    }