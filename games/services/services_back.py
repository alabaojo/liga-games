
from games.constants import URL_UPDATE, URL_TEAM_ALL
from games.models import Team, Match, Result, Season
# /getmatchdata/Identifier/Season/GroupOrderId

import requests

def fetch_all_team():
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


def fetch_all_results():
    urlTEMP ='https://www.openligadb.de/api/getmatchdata/bl1/2016'
    league = 'bl1/'
    season = '2016'
    url_endpoint= URL_TEAM_ALL
    url = url_endpoint+league+season
    r = requests.get(urlTEMP)
    resp = r.json()
    match_id =  [res ['MatchId'] for res in resp]
    team1 = [res['Team1'] for res in resp]
    team2 = [res['Team2'] for res in resp]
    match_result = [res['MatchResult'] for res in resp]
    result_id= [lambda x : x['ResultId'] for x in match_result]

    matches = Match()
    match_list= {
        'id' : match_id,
        'team1' : [res['Team1'] for res in resp],
        'team2' : [res['Team2'] for res in resp],
        'result_id' : result_id
    }

    match = Match(match_list).save()

    result_list = {
        'point_team1' : [res['PointsTeam1'] for res in match_result],
        'point_team2' : [res['PointTeam2'] for res in resp],
        'result_id' : result_id
    }
    result = Result(result_list).save()

    return

def fetch_team():
    league = 'bl1/'
    season = '2016'
    url_endpoint= URL_TEAM_ALL
    url = url_endpoint+league+season
    resp = requests.get(url)
    teams_json = resp.json()
    for team in teams_json:
        Team(team_order = team['TeamId'], name = team['TeamName'],
        alias = team['ShortName']).save()
    return