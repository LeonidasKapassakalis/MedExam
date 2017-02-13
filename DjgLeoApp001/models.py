# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from __future__ import unicode_literals

from django.db import models

from django_datatables_view.base_datatable_view import BaseDatatableView

from django.core.urlresolvers import reverse

class Country(models.Model):
    id = models.AutoField
    name = models.CharField(u'Χώρα', max_length=50)
    abbr = models.CharField(u'Χώρα(2)', max_length=2) 
    telephoneext = models.CharField(u'Τηλ', max_length=4) 

    def __unicode__(self):
        return self.name

class Examschema(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)
    sequence = models.CharField(max_length=50, blank=True, null=True)
    notes = models.CharField(max_length=150, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Locations(models.Model):
    id = models.AutoField
    name = models.CharField(db_column='Name', unique=True, max_length=50) 
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  
    phone = models.CharField(db_column='Phone', max_length=60, blank=True, null=True)   
    mail = models.CharField(db_column='Mail', max_length=50, blank=True, null=True)   
    tk = models.CharField(db_column='TK', max_length=5, blank=True, null=True)   
    text = models.TextField(db_column='Text', blank=True, null=True)
    hospital = models.NullBooleanField(db_column='Hospital')   
    medicalcenter = models.NullBooleanField(db_column='MedicalCenter')   
    eopyy = models.NullBooleanField(db_column='EOPYY')   
    contact = models.TextField(db_column='CONTACT', blank=True, null=True)
    countryid = models.ForeignKey(Country, db_column='CountryId')   
    peoples = models.ManyToManyField('People')

    def __unicode__(self):
        return self.name

class People(models.Model):
    id = models.AutoField
    name = models.CharField(u'Όνομα', db_column='Name', max_length=30)   
    surname = models.CharField(u'Επώνυμο',db_column='Surname', max_length=50)   
    dateofbirth = models.DateField(u'Ημερομηνία Γέννησης',db_column='DateOfBirth', blank=True, null=True)   
    nationality = models.CharField(u'Υπηκοότητα',db_column='Nationality', max_length=20, blank=True, null=True)   
    countryid = models.ForeignKey(Country, verbose_name='Χώρα', db_column='CountryId')   
    phone = models.CharField(u'Τηλεφωνο',db_column='Phone', max_length=60, blank=True, null=True)   
    fax = models.CharField(u'FAX',db_column='Fax', max_length=60, blank=True, null=True)   
    mobile = models.CharField(u'Κινητό',db_column='mobile', max_length=60, blank=True, null=True)   
    mail = models.CharField(db_column='Mail', max_length=250, blank=True, null=True)   
    ispatient = models.NullBooleanField(u'Ασθενής',db_column='IsPatient')   
    isdoctor = models.NullBooleanField(u'Γιατρός',db_column='IsDoctor')   
    canlogin = models.NullBooleanField(db_column='CanLogin')   
    accessonlyhisfile = models.NullBooleanField(db_column='AccessOnlyHisFile')   
    notes = models.CharField(db_column='Notes', max_length=8192, blank=True, null=True)   
    photo = models.BinaryField(db_column='Photo', blank=True, null=True)   

    class Meta:
        ordering = ('surname','name')

    def __unicode__(self):
        return self.surname + ' ' + self.name


class Examname(models.Model):
    name = models.TextField(db_column='Name', unique=True)
    sname = models.CharField(db_column='SName', max_length=25)   
    groupexam_id = models.IntegerField(db_column='GroupExam_Id')   
    mm_id = models.IntegerField(db_column='MM_Id')   
    min = models.TextField(db_column='Min', blank=True, null=True)
    max = models.TextField(db_column='Max', blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=250, blank=True, null=True)   
    is_numeric = models.NullBooleanField(db_column='Is_Numeric')   
    is_text = models.NullBooleanField(db_column='Is_Text')   
    is_memo = models.NullBooleanField(db_column='Is_Memo')   
    bioexaminationcategory= models.ForeignKey('BioExaminationCategory',blank=True,null=True)

    def __unicode__(self):
        return self.name

class Mm(models.Model):
    pk = models.AutoField
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)   
    sname = models.CharField(db_column='SName', max_length=8, blank=True, null=True)   

    def __unicode__(self):
        return self.name

class ExaminationCategory(models.Model):
    name = models.CharField(max_length=50)
    sname = models.CharField(max_length=15)    

    def __unicode__(self):
        return self.name

# First, define the Manager subclass.

def get_filter_manager(*args, **kwargs):
    class FilterManager(models.Manager):
        "Custom manager filters standard query set with given args."
        def get_query_set(self):
            return super(FilterManager, self).get_query_set().filter(*args, **kwargs)
    return FilterManager()

##class Article(models.Model):
##    ...
##    objects = get_filter_manager(deleted=False, author__deleted=False)
##    deleted_articles = get_filter_manager(deleted=True)

class DahlBookManager(models.Manager):
    def get_queryset(self):
        return super(DahlBookManager,self).get_queryset().filter(peopleid='1')


class Examination0(models.Model):
    id = models.AutoField
    peopleid = models.ForeignKey(People)
    doctorid = models.ForeignKey(People, limit_choices_to={'isdoctor': True} , related_name = 'Examination0Doctor')
    categorid = models.ForeignKey(ExaminationCategory)    
    dateofexam = models.DateField()
    notes   = models.CharField(max_length=8192, blank=True, null=True)
    comments = models.CharField(max_length=8192, blank=True, null=True)

    objects = models.Manager() # The default manager.
    dahl_objects = DahlBookManager() # The Dahl-specific manager.
    leo_objects = get_filter_manager(peopleid=2)

    class Meta:
        ordering = ('-dateofexam',)

    def surname(self):
        return self.peopleid.surname + ' ' + self.peopleid.name

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listexam', kwargs={'Patient': self.peopleid.id})

    def __unicode__(self):
        a=self.dateofexam
        return self.peopleid.surname + ' ' + self.peopleid.name +  ' ' +a.strftime('%d/%m/%Y') + ' + ' + self.notes[:100]


class ZeroConfigurationDatatableView(BaseDatatableView):
    model = Examname


from django.contrib.auth.models import User

class SpecialUsers(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    peopleid    = models.ForeignKey(People, verbose_name='Άνθρωπος')
    altpeopleid = models.ForeignKey(People, verbose_name='Alt.Άνθρωπος', related_name='SpecialUserAltPeople')
    peoples     = models.ManyToManyField(People, verbose_name = 'Άνθρωποι', related_name='SpecialUserAltPeoples')
    doctors     = models.ManyToManyField(People, limit_choices_to={'isdoctor': True}, verbose_name = 'Γιατροί', related_name='SpecialUserAltDoctors')
    location    = models.ForeignKey(Locations, verbose_name='Τόπος')
    notes       = models.CharField(max_length=100)


class DoctorSpeciality(models.Model):
    name = models.CharField(max_length=50)
    sname = models.CharField(max_length=15)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

# OperationsCategory
class OperationCategory(models.Model):
    name = models.CharField(max_length=50)
    sname = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name

# OperationsExamination
class Operations(models.Model):
    peopleid = models.ForeignKey(People)
    doctorid = models.ForeignKey(People, limit_choices_to={'isdoctor': True}, related_name='OperationDoctor')
    categorid = models.ForeignKey(OperationCategory)
    dateof = models.DateField()
    notes = models.CharField(max_length=8192, blank=True, null=True)
    comments = models.CharField(max_length=8192, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listoperation', kwargs={'Patient': self.peopleid.id})

    def __unicode__(self):
        a = self.dateofexam
        return self.peopleid.surname + ' ' + self.peopleid.name + ' ' + a.strftime('%d/%m/%Y') + ' + ' + self.notes[:100]

# BioExaminationCategory
class BioExaminationCategory(models.Model):
    name = models.CharField(max_length=50)
    sname = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name

# BioExamination
class BioExamination(models.Model):
    peopleid = models.ForeignKey(People)
    doctorid = models.ForeignKey(People, limit_choices_to={'isdoctor': True} , related_name = 'ExaminationBioDoctor')
    categorid = models.ForeignKey(ExaminationCategory)
    dateofexam = models.DateField()
    notes   = models.CharField(max_length=8192, blank=True, null=True)
    comments = models.CharField(max_length=8192, blank=True, null=True)
    examsschema = models.ManyToManyField('Examschema')

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listexambio', kwargs={'Patient': self.peopleid.id})

    def __unicode__(self):
        a=self.dateofexam
        return self.peopleid.surname + ' ' + self.peopleid.name +  ' ' +a.strftime('%d/%m/%Y') + ' + ' + self.notes[:100]


class BioExaminationDetail(models.Model):
    BioExaminationId = models.ForeignKey(BioExamination)
    examnameid = models.ForeignKey(Examname, verbose_name='Εξέταση')
    value = models.FloatField('Τιμή')
    notes = models.CharField(max_length=255, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listexambiodet', kwargs={'exampk': self.BioExaminationId.pk})

    class Meta:
        unique_together = (("BioExaminationId", "examnameid" ),)
        ordering = ('BioExaminationId','id')


    def __unicode__(self):
        return self.examnameid.name

# MedicineCategory
class MedicineCategory(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    sname = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name


# Medicine
class Medicine(models.Model):
    peopleid  = models.ForeignKey(People)
    doctorid  = models.ForeignKey(People, limit_choices_to={'isdoctor': True} , related_name = 'MedicineDoctor')
    categorid = models.ForeignKey(MedicineCategory)
    dateof    = models.DateField()
    datestart = models.DateField()
    dateend   = models.DateField()
    notes     = models.CharField(max_length=8192, blank=True, null=True)

    class Meta:
        unique_together = (("peopleid", "doctorid", "categorid", "dateof" ),)

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listmedicine', kwargs={'Patient': self.peopleid.id})

    def __unicode__(self):
        a=self.dateofexam
        return self.peopleid.surname + ' ' + self.peopleid.name +  ' ' +a.strftime('%d/%m/%Y') + ' + ' + self.notes[:100]
