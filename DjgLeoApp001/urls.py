from django.conf.urls import url


from . import views


app_name = 'DjgLeoApp001'
urlpatterns = [
    url(r'^$', views.index, name='index'),

#    url(r'^list/$', views.PublisherList.as_view(), name='list'),
    url(r'^list/$', views.person_list, name='list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.PeopleDetailView.as_view(), name='detail'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.PeopleUpdate.as_view(), name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.PeopleDelete.as_view(), name='delete'),
    url(r'^create/$', views.PeopleCreare.as_view(), name='create'),
    url(r'^listd/', views.doctor_list, name='doctor_list'),
    url(r'^listp/', views.patient_list, name='patient_list'),

#Exams
    url(r'^listexam/(?P<Patient>[0-9]+)/$', views.ExaminationList, name='listexam'),
    url(r'^detailexam/(?P<pk>[0-9]+)/$', views.ExaminationDetailView.as_view(), name='detailexam'),
    url(r'^updateexam/(?P<pk>[0-9]+)/$', views.ExaminationUpdate.as_view(), name='updateexam'),
    url(r'^deleteexam/(?P<pk>[0-9]+)/$', views.ExaminationDelete.as_view(), name='deleteexam'),
    url(r'^createexam/$', views.ExaminationCreare.as_view(), name='createexam'),

#ExamBio
    url(r'^listexambio/(?P<Patient>[0-9]+)/$', views.BioExaminationList, name='listexambio'),
    url(r'^detailexambio/(?P<pk>[0-9]+)/$', views.BioExaminationDetailView.as_view(), name='detailexambio'),
    url(r'^updateexambio/(?P<pk>[0-9]+)/$', views.BioExaminationUpdate.as_view(), name='updateexambio'),
    url(r'^deleteexambio/(?P<pk>[0-9]+)/$', views.BioExaminationDelete.as_view(), name='deleteexambio'),
    url(r'^createexambio/$', views.BioExaminationCreare.as_view(), name='createexambio'),
    url(r'^updateexambio/(?P<pk>[0-9]+)/$', views.MassBioExaminationDetailUpdate, name='updateexambio'),

#ExamBioDet
    url(r'^listexambiodet/(?P<exampk>[0-9]+)/$', views.BioExaminationDetList, name='listexambiodet'),
    url(r'^detailexambiodet/(?P<pk>[0-9]+)/$', views.BioExaminationDetDetailView.as_view(), name='detailexambiodet'),
    url(r'^updateexambiodet/(?P<pk>[0-9]+)/$', views.BioExaminationDetUpdate.as_view(), name='updateexambiodet'),
    url(r'^deleteexambiodet/(?P<pk>[0-9]+)/$', views.BioExaminationDetDelete.as_view(), name='deleteexambiodet'),
    url(r'^createexambiodet/$', views.BioExaminationDetCreare.as_view(), name='createexambiodet'),

    url(r'^BioExaminationDetailList/$', views.BioExaminationDetailList.as_view(), name='BioExaminationDetailList'),

#Operation
    url(r'^listoperation/(?P<Patient>[0-9]+)/$', views.OperationList, name='listoperation'),
    url(r'^detailoperation/(?P<pk>[0-9]+)/$', views.OperationDetailView.as_view(), name='detailoperation'),
    url(r'^updateoperation/(?P<pk>[0-9]+)/$', views.OperationUpdate.as_view(), name='updateoperation'),
    url(r'^deleteoperation/(?P<pk>[0-9]+)/$', views.OperationDelete.as_view(), name='deleteoperation'),
    url(r'^createoperation/$', views.OperationCreare.as_view(), name='createoperation'),

#Medicine
    url(r'^listmedicine/(?P<Patient>[0-9]+)/$', views.MedicineList, name='listmedicine'),
    url(r'^detailmedicine/(?P<pk>[0-9]+)/$', views.MedicineDetailView.as_view(), name='detailmedicine'),
    url(r'^updatemedicine/(?P<pk>[0-9]+)/$', views.MedicineUpdate.as_view(), name='updatemedicine'),
    url(r'^deletemedicine/(?P<pk>[0-9]+)/$', views.MedicineDelete.as_view(), name='deletemedicine'),
    url(r'^createmedicine/$', views.MedicineCreare.as_view(), name='createmedicine'),

]