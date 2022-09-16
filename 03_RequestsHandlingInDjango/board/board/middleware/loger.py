from datetime import datetime
import os


class UserInfo:
    def __init__(self, get_response):
        self.get_response = get_response
        self.time = datetime.now()

    def __call__(self, request):
        response = self.get_response(request)
        url_name = request.path
        method = request.method
        way = os.path.abspath('request_info')
        with open(way, 'w') as file:
            file.write('URL : {url}\nMETHOD : {method}\nTIME : {time}'.format(
                url=url_name, method=method, time=self.time
            ))
        return response

