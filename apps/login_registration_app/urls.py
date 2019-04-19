##### login_registration_app urls
from django.conf.urls import url,include

from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.login_and_registration),
    url(r'^login$', views.login),
    url(r'^register$',views.register),
    url(r'^success$', views.success),
    url(r'^logout$',views.logout),
]
