import requests
from cgi import test
import sys

url = "https://www.cheapshark.com/api/1.0/stores"
def test_name_of_stores():
    response = requests.get("https://www.cheapshark.com/api/1.0/stores").json()
    store_name = [n["storeName"] for n in requests.get("https://www.cheapshark.com/api/1.0/stores").json()]
    print(store_name)
    number_of_stores = len(store_name)
    expected = 33
    assert expected == number_of_stores

res = {'gameID': '146',
'steamAppID': '35140',
'cheapest': '3.99',
'cheapestDealID': 'cfP9tpZelJk3bRJA5FXHBrlRYxdgbDpylaXnTAj6VRg%3D',
'external': 'Batman: Arkham Asylum Game of the Year Edition',
'internalName': 'BATMANARKHAMASYLUMGAMEOFTHEYEAREDITION',
'thumb': 'https://cdn.cloudflare.steamstatic.com/steam/apps/35140/capsule_sm_120.jpg?t=1634156906'}

def validate_res(res):
    fields = ["gameID","steamAppID","cheapest","cheapestDealID","external","internalName","thumb"]
    for field in res:
        if field not in fields:
            return False
    return True

def validate_game_info(res):
    fields = ["info","cheapestPriceEver","deals"]
    for polje in res:
        if polje not in fields:
            return False 
    return True 

def test_game_by_steam_app_id():
    url = "https://www.cheapshark.com/api/1.0/games?title=a&limit=10&exact=0"  
    idovi = [g["steamAppID"] for g in requests.get(url).json()] 
    for gid in idovi:
        game = requests.get(f"https://www.cheapshark.com/api/1.0/games?steamAppID={gid}&limit=10&exact=0").json()
        assert validate_res(game[0])



def test_by_game_id():
    url = "https://www.cheapshark.com/api/1.0/games?title=a&limit=10&exact=0"
    game_id = [g["gameID"] for g in requests.get(url).json()]
    for gid in game_id:
        game = requests.get(f"https://www.cheapshark.com/api/1.0/games?id={gid}").json()
        assert validate_game_info(game)
        
test_by_game_id()
