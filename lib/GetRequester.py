import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url=url

    def get_response_body(self):
        response=requests.get(self.url)
        return response.content
        
    def load_json(self):
        result=self.get_response_body()
        return json.loads(result)


result=GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json').load_json()
print(result)
