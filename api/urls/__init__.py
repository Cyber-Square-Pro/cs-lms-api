from .authentication import urlpatterns as authentication_urls
from .accounts  import urlpatterns as accounts_urls
 

urlpatterns = [
    *authentication_urls,
    *accounts_urls
]