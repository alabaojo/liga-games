
from games.constants import URL_UPDATE, URL_TEAM_ALL
from games.models import Team, Match, Result, Season
# /getmatchdata/Identifier/Season/GroupOrderId
import requests

def fetch_all_team_in():
    league = 'bl1/'
    season = '2016'
    url_endpoint= URL_TEAM_ALL
    url = url_endpoint+league+season 
    resp = requests.get(url)
    teams_json = resp.json()
    for team in teams_json:   
        Team(id = team['TeamId'], name = team['TeamName'],
        alias = team['ShortName']).save()
    return 
    
def team_all():
    pass



"""
def matches():
    league = 'bl1'
    season = 2016
    group = 8
    url_endpoint= URL_TEAM_ALL
    params = {'LeagueShortCut': league,'LeagueSeason': season, 'GroupOrderId': group}
    response = requests.get(url_endpoint, params=params)
    data = response.json()
    team_list = {'teams':data['results']}
    return team_list

"""

def get_it():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    geodata = response.json()
    match_list = {'books':geodata['id'], 
    'country': geodata['id']
    }
    return match_list
 
def season_matches(league,year):
    url_season = 'https://www.openligadb.de/api/getmatchdata/bl1/2016'
    params = {'year': year, 'league': league}
    #response = requests.get(url, params=params)
    data = requests.get(url_season).json()
    team_list = {'books':data['results']}
    return team_list


