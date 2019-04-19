###### inside books_app urls ########
from django.conf.urls import url,include

from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.books),
    url(r'^(?P<number>\d+)$',views.detail),
    url(r'^add_book$',views.add_book),
    url(r'^add_fav/(?P<number>\d+)$',views.add_fav),
    url(r'^unfav/(?P<number>\d+)$',views.unfav),
    url(r'^update_book$',views.update_book),
    url(r'^myfav$',views.myFav),
]
