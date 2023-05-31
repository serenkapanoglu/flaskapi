import requests

data = {
    'username': 'chickenz',
    'tweets': [
        'hello!', 'goodbye!', 'bockbock', {
            'id':1,   'text': 'my first tweet!'}
    ]
    
}


requests.post('https://eo34i31up0182kw.m.pipedream.net', json=data)