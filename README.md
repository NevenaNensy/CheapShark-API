# CheapShark-API

CheapShark is a price comparison website for digital PC Games

Here is three API:
1. Returns a full list of store IDs, names, and a flag specifying if store is active.
  
   url = "https://www.cheapshark.com/api/1.0/stores"

2. Get a list of games that contain a given title or match a steamAppID
  
   url = "https://www.cheapshark.com/api/1.0/games?title=a&limit=10&exact=0" 

3. Gets info for a specific game. Response includes a list of all deals associated with the game.
  
   url = "https://www.cheapshark.com/api/1.0/games?title=a&limit=10&exact=0"

In every API I used assert statement and finished with Pytest.

