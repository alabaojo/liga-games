
from games.constants import URL_UPDATE, URL_TEAM_ALL
from games.models import Team, Match, Result, Season
# /getmatchdata/Identifier/Season/GroupOrderId
import requests


def teams_info():
    teams = [t['name'] for t in Team.objects.values('name')]
    return teams

def fetch_api_team():
    league = 'bl1/'
    season = '2016'
    url_endpoint = URL_TEAM_ALL
    url = url_endpoint + league + season
    resp = requests.get(url)
    teams_json = resp.json()
    for team in teams_json:
        Team(order=team['TeamId'], name=team['TeamName'],
             alias=team['ShortName']).save()
    return

