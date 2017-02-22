"""DjgLeo001 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from DjgLeoApp001 import views
from DjgLeoApp001 import models
from DjgLeoApp001 import forms

#from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^menu/', views.NewMenu),
    url(r'^menu1/', views.NewMenu1),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # url(r'^(?P<question_id>[0-9]+)/people_det/$', views.people_det, name='people_det'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # url(r'^leo/', views.index, name='index'),
    # url(r'^vote/(?P<id>[0-9]{4})', views.vote, name='vote'),  # , {'id':1}),
    # url(r'^result/(?P<id>[0-9])', views.results, name='results'),
    # url(r'^date/', views.current_datetime2, name='date'),
    # url(r'^test/', views.test, name='test'),
    # url(r'^(?P<id>[0-9]+)/people_det/$', views.people_det, name='people_det0'),
    # url(r'^people_det/(?P<id>[0-9]+)/$', views.people_det, name='people_det1' ),
    # url(r'^people_det2/(?P<id>[0-9]+)/$', views.results, name='people_det2'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # url(r'^tables0/', views.people0 , name='tables0'),
    # url(r'^tables100/', views.examination00, name='tables100'),
    # url(r'^tables101/', views.examination_list, name = 'examination_list'),
    # url(r'^tables10/', views.person_list, name='person_list'),

    #url(r'^tables222/(?P<pk>[0-9]+)/$', views.ExaminationsListPer_Table, name='ExaminationsListPer_Table'),

    # url(r'^locations/', views.locations_list, name='locations'),
    # url(r'^location/(?P<pk>[0-9]+)/$', views.LocationDetailView.as_view(), name='location'),
    # url(r'^locationupd/(?P<pk>[0-9]+)/$', views.LocationUpdate.as_view(), name='locationupd'),
    # url(r'^locationdel/(?P<pk>[0-9]+)/$', views.LocationDelete.as_view(), name='locationdel'),
    # url(r'^locationcre/$', views.LocationCreare.as_view(), name='locationcreate'),

    # url(r'^tables1/', views.people1, name='people1'),
    # url(r'^tables3/', models.ZeroConfigurationDatatableView.as_view(), name='order_list_json'),
    # url(r'^contact/$', views.contact, name='contact'),
    # url(r'^publishers/$', views.PeopleList.as_view(), name='publishers'),
    # url(r'^publisher/(?P<pk>[0-9]+)/$', views.PeopleDetailView.as_view(), name='publisher'),
    # url(r'^publisherupd/(?P<pk>[0-9]+)/$', views.PeopleUpdate.as_view(), name='publishersupd'),
    # url(r'^publisherdel/(?P<pk>[0-9]+)/$', views.PeopleDelete.as_view(), name='publisherdel'),
    # url(r'^publishercre/$', views.PeopleCreare.as_view(), name='publishercreate'),
#    url(r'^report_builder/', include('report_builder.urls')),

    url(r'^DjgLeoApp001/', include('DjgLeoApp001.urls')),

    # url(r'^examinationsper/([0-9]+)/$', views.ExaminationsListPer.as_view(), name='examinationsper'),
    # url(r'^examinationsper1/([0-9]+)/$', views.examination_list_per , name='examinationspert'),
    # url(r'^examinationsListPerDoctor/([0-9]+)/$', views.ExaminationsListPerDoctor.as_view(), name='examinationsperdoctor'),
    # url(r'^examinationsListPerDoctorPatient/([0-9]+)/([0-9]+)/$', views.ExaminationsListPerDoctorPatient.as_view(), name='examinationsperdoctorpatient'),
    #
    # url(r'^examinationspercategory/([0-9]+)/$', views.ExaminationsListPerCategory.as_view(), name='examinationspercategory'),
    # url(r'^examinations/$', views.ExaminationsList.as_view(), name='examinations'),
    #
    # url(r'^examinationupd/(?P<pk>[0-9]+)/$', views.ExaminationUpdate.as_view(), name='examinationupd'),
    # url(r'^examinationdet/(?P<pk>[0-9]+)/$', views.ExaminationDetail.as_view(), name='examinationdet'),
    # url(r'^examinationdel/(?P<pk>[0-9]+)/$', views.ExaminationDelete.as_view(), name='examinationdel'),
    # url(r'^examinationcre/$', views.ExaminationCreare.as_view(), name='examinationcreate'),
    #
    # url(r'^contact0/$', forms.index, name='contact0'),
    # url(r'^contact1/$', views.ExampleForm0.as_view(), name = 'contact1'),

#DataTables
    url(r'^contact999/$',views.ZeroConfigurationDatatableView.as_view(), name='contact999'),
    url(r'^contact998/$',views.ZeroConfigurationDatatableView0.as_view(), name='contact998'),

    url(r'^multiexam/$', views.MultiExam, name='MultiExamForm'),
    url(r'^multiexam0/$', views.MultiExam0, name='MultiExamForm0'),

#    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'admin/login.html'}),
#    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),

#    url(r'^logina/$', include('django.contrib.auth.urls')),

    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),

    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^password_change/$', views.password_change, name='password_change'),
    url(r'^password_change/done/$', views.password_change_done, name='password_change_done'),
    url(r'^password_reset/$', views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),

    url(r'^admin/', admin.site.urls),

    url(r'', views.MainMenu, name='MainMenu'),
]
