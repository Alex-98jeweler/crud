from django.http import JsonResponse


class Process400:
    def __init__(self, get_response) -> None:
        self._get_response = get_response

    def __call__(self, request) :
        return self._get_response(request)

    def process_exception(self, request, exception):
        return JsonResponse({
            'status': 'error',
            'code': 400,
        })
        
        