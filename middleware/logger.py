
class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('Request before:', request)
        response = self.get_response(request)
        print('Response after:', response)
        return response

