from django.urls import include, path

urlpatterns = [
    path('user/', include('api.controllers.user.urls')),
    path('chathead/', include('api.controllers.chathead.urls')),
    path('chatmessage/', include('api.controllers.chatmessage.urls')),
]