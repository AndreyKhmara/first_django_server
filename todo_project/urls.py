from django.urls import path, include

urlpatterns = [
    path("todo/", include('todo.urls')),
    path('auth/', include('auth_app.urls')),
]
