class DebugRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Логируем каждый запрос
        print(f"[MIDDLEWARE] Method={request.method}, Path={request.path}")
        print(f"[MIDDLEWARE] Headers={dict(request.headers)}")
        response = self.get_response(request)
        print(f"[MIDDLEWARE] Response status={response.status_code}")
        return response