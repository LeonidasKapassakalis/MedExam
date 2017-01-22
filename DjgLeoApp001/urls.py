from django.conf.urls import url


from . import views


app_name = 'DjgLeoApp001'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # url(r'^(?P<question_id>[0-9]+)/people_det/$', views.people_det),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # url(r'^leo/', views.index, name='index'),
    # url(r'^vote/(?P<id>[0-9]{4})', views.vote, name='vote'),  # , {'id':1}),
    # url(r'^result/(?P<id>[0-9])', views.results, name='results'),
    # url(r'^date/', views.current_datetime2),
    # url(r'^test/', views.test),
    # url(r'^(?P<id>[0-9]+)/people_det/$', views.people_det),
    # url(r'^people_det/(?P<id>[0-9]+)/$', views.people_det),
    # url(r'^people_det2/(?P<id>[0-9]+)/$', views.results),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
]