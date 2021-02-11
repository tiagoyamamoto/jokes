import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import jokes.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jokes_project.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket":
        URLRouter(
            jokes.routing.websocket_urlpatterns
        ),
})
