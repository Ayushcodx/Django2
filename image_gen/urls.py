from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from image_gen.views import generate_image_home

urlpatterns = [
    path('', generate_image_home, name='generate_img'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
