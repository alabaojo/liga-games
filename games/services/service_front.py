
from games.constants import URL_UPDATE, URL_TEAM_ALL
from games.models import Team, Match, Result, Season
# /getmatchdata/Identifier/Season/GroupOrderId
import requests


def teams_info():
    teams = [t for t in Team.objects.all()]
    return teams
