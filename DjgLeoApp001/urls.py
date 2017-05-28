from django.conf.urls import url


from . import views

from . import views_test

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

    url(r'^examinationsper/([0-9]+)/$', views.ExaminationsListPer.as_view(), name='examinationsper'),
    url(r'^examinationsper1/([0-9]+)/$', views.examination_list_per, name='examinationspert'),
    url(r'^examinationsListPerDoctor/([0-9]+)/$', views.ExaminationsListPerDoctor.as_view(),name='examinationsListPerDoctor'),
    url(r'^examinationsListPerDoctorPatient/([0-9]+)/([0-9]+)/$', views.ExaminationsListPerDoctorPatient.as_view(),name='examinationsperdoctorpatient'),

#ExamBio
    url(r'^listexambio/(?P<Patient>[0-9]+)/$', views.BioExaminationList, name='listexambio'),
    url(r'^detailexambio/(?P<pk>[0-9]+)/$', views.BioExaminationDetailView.as_view(), name='detailexambio'),
    url(r'^updateexambio/(?P<pk>[0-9]+)/$', views.BioExaminationUpdate.as_view(), name='updateexambio'),
    url(r'^deleteexambio/(?P<pk>[0-9]+)/$', views.BioExaminationDelete.as_view(), name='deleteexambio'),
    url(r'^createexambio/$', views.BioExaminationCreare.as_view(), name='createexambio'),
    url(r'^massupdateexambio/(?P<pk>[0-9]+)/$', views.MassBioExaminationDetailUpdate, name='massupdateexambio'),

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

#Location
    url(r'^listlocation/$', views.LocationList, name='listlocation'),
    url(r'^detaillocation/(?P<pk>[0-9]+)/$', views.LocationDetailView.as_view(), name='detaillocation'),
    url(r'^updatelocation/(?P<pk>[0-9]+)/$', views.LocationUpdate.as_view(), name='updatelocation'),
    url(r'^deletelocation/(?P<pk>[0-9]+)/$', views.LocationDelete.as_view(), name='deletelocation'),
    url(r'^createlocation/$', views.LocationCreare.as_view(), name='createlocation'),

#examname
    url(r'^listexamname/$', views.ExamnameList, name='listexamname'),
    url(r'^detailexamname/(?P<pk>[0-9]+)/$', views.ExamnameDetailView.as_view(), name='detailexamname'),
    url(r'^updateexamname/(?P<pk>[0-9]+)/$', views.ExamnameUpdate.as_view(), name='updateexamname'),
    url(r'^deleteexamname/(?P<pk>[0-9]+)/$', views.ExamnameDelete.as_view(), name='deleteexamname'),
    url(r'^createexamname/$', views.ExamnameCreare.as_view(), name='createexamname'),


#mm
    url(r'^listmm/$', views.MMList, name='listmm'),
    url(r'^updatemm/(?P<pk>[0-9]+)/$', views.MMUpdate.as_view(), name='updatemm'),
    url(r'^createmm/$', views.MMCreate.as_view(), name='createmm'),


#mmtype
    url(r'^listmmtype/$', views.MMTypeList, name='listmmtype'),
    url(r'^updatemmtype/(?P<pk>[0-9]+)/$', views.MMTypeUpdate.as_view(), name='updatemmtype'),
    url(r'^createmmtype/$', views.MMTypeCreate.as_view(), name='createmmtype'),


#groupexam
    url(r'^listgroupexam/$', views.GroupExamList, name='listgroupexam'),
    url(r'^updategroupexam/(?P<pk>[0-9]+)/$', views.GroupExamUpdate.as_view(), name='updategroupexam'),
    url(r'^creategroupexam/$', views.GroupExamCreate.as_view(), name='creategroupexam'),


#medicinecategory
    url(r'^listmedicinecategory/$', views.MedicineCategoryList, name='listmedicinecategory'),
    url(r'^updatemedicinecategory/(?P<pk>[0-9]+)/$', views.MedicineCategoryUpdate.as_view(), name='updatemedicinecategory'),
    url(r'^createmedicinecategory/$', views.MedicineCategoryCreate.as_view(), name='createmedicinecategory'),


#bioexaminationcategory
    url(r'^listbioexaminationcategory/$', views.BioExaminationCategoryList, name='listbioexaminationcategory'),
    url(r'^updatebioexaminationcategory/(?P<pk>[0-9]+)/$', views.BioExaminationCategoryUpdate.as_view(), name='updatebioexaminationcategory'),
    url(r'^createbioexaminationcategory/$', views.BioExaminationCategoryCreate.as_view(), name='createbioexaminationcategory'),


#operationcategory
    url(r'^listoperationcategory/$', views.OperationCategoryList, name='listoperationcategory'),
    url(r'^updateoperationcategory/(?P<pk>[0-9]+)/$', views.OperationCategoryUpdate.as_view(), name='updateoperationcategory'),
    url(r'^createoperationcategory/$', views.OperationCategoryCreate.as_view(), name='createoperationcategory'),


#doctorspeciality
    url(r'^listdoctorspeciality/$', views.DoctorSpecialityList, name='listdoctorspeciality'),
    url(r'^updatedoctorspeciality/(?P<pk>[0-9]+)/$', views.DoctorSpecialityUpdate.as_view(), name='updatedoctorspeciality'),
    url(r'^createdoctorspeciality/$', views.DoctorSpecialityCreate.as_view(), name='createdoctorspeciality'),


#examinationcategory
    url(r'^listexaminationcategory/$', views.ExaminationCategoryList, name='listexaminationcategory'),
    url(r'^updateexaminationcategory/(?P<pk>[0-9]+)/$', views.ExaminationCategoryUpdate.as_view(), name='updateexaminationcategory'),
    url(r'^createexaminationcategory/$', views.ExaminationCategoryCreate.as_view(), name='createexaminationcategory'),


#examschema
    url(r'^listexamschema/$', views.ExamSchemaList, name='listexamschema'),
    url(r'^updateexamschema/(?P<pk>[0-9]+)/$', views.ExamSchemaUpdate.as_view(), name='updateexamschema'),
    url(r'^createexamschema/$', views.ExamSchemaCreate.as_view(), name='createexamschema'),


#schemadetail
    url(r'^listschemadetail/$', views.SchemaDetailList, name='listschemadetail'),
    url(r'^updateschemadetail/(?P<pk>[0-9]+)/$', views.SchemaDetailUpdate.as_view(), name='updateschemadetail'),
    url(r'^createschemadetail/$', views.SchemaDetailCreate.as_view(), name='createschemadetail'),




#country
    url(r'^listcountry/$', views.CountryList, name='listcountry'),
    url(r'^updatecountry/(?P<pk>[0-9]+)/$', views.CountryUpdate.as_view(), name='updatecountry'),
    url(r'^createcountry/$', views.CountryCreate.as_view(), name='createcountry'),


    # url(r'^test/$', views_test.BioExaminationDetailSingleTableView.as_view(), name='test'),
    # url(r'^testnf/$', views_test.BioExaminationDetailSingleTableView.as_view(), name='test'),
    # url(r'^testfil/$', views_test.BioExaminationDetailFilteredSingleTableView.as_view(), name='test'),
    url(r'^testf/(?P<exampk>[0-9]+)/$', views_test.BioExaminationDetailFiltered, name='testf'),
    url(r'^testfa/(?P<peoplepk>[0-9]+)/$', views_test.BioExaminationDetailFilteredAll, name='testfa'),
    url(r'^testff/$', views_test.PeopleFiltered, name='testf'),
    url(r'^testff1/$', views_test.VExamdetaislFiltered, name='testf1'),
    url(r'^Graphos/$', views_test.Graphos, name='Graphos'),
    # url(r'^testchart/$', views_test.basicline, name='testchart'),
    # url(r'^testfilex/$', views_test.BioExaminationDetailFilterEx.as_view(), name='test'),

    # url(r'^$', BookFilteredSingleTableView.as_view()),
    # url(r'^nofilter/$', BookSingleTableView.as_view()),
    # url(r'^filter2/$', FilteredTableView.as_view()),
    # url(r'^filter_ex/$', FilterExListView.as_view()),


    url(r'^someurl/$', views.someurl, name='someurl'),

]