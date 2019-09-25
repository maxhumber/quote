import json
from quote import search

def test_search():
    query = 'blake crouch'
    result = search(query, limit=5)
    one = json.loads(result)[0]
    assert one['author'] == 'Blake Crouch'
    assert one['book']
    assert isinstance(one['quote'], str)
