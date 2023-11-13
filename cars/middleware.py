from django.http import HttpResponseForbidden

class URLBlockingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Liste as URLs que você deseja bloquear
        blocked_urls = ['addcar/', 'update_cars/', 'delete_car/']

        # Verifique se a URL da solicitação está na lista de URLs bloqueadas
        if request.path_info in blocked_urls:
            return HttpResponseForbidden("Acesso proibido")

        return self.get_response(request)