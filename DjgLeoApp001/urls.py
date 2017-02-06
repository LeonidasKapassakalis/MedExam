from django.conf.urls import url


from . import views


app_name = 'DjgLeoApp001'
urlpatterns = [
    url(r'^$', views.index, name='index'),
#    url(r'^list/$', views.PublisherList.as_view(), name='list'),
    url(r'^list/$', views.person_list, name='list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.PublisherDetailView.as_view(), name='detail'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.PublisherUpdate.as_view(), name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.PublisherDelete.as_view(), name='delete'),
    url(r'^create/$', views.PublisherCreare.as_view(), name='create'),

    url(r'^listd/', views.doctor_list, name='doctor_list'),
    url(r'^listp/', views.patient_list, name='patient_list'),

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