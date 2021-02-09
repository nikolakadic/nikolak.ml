class CORSMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = '*'
        response[
            'Access-Control-Allow-Headers'] = 'Content-Type, Access-Control-Allow-Headers, Authorization, ' \
                                              'X-Requested-With'

        return response