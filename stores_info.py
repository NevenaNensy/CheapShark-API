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
