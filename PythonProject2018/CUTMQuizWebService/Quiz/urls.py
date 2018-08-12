from django.conf.urls import url
from Quiz import views

urlpatterns = [
    url(r'^Quiz/$', views.questionBank_list),
    url(r'^Quiz/select/$', views.questionBank_category),
    url(r'^Quiz/category/$', views.category)
]
