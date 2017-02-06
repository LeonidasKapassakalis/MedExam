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

class Country(models.Model):
    id = models.AutoField
    name = models.CharField(u'Χώρα',db_column='Name', max_length=50)  # Field name made lowercase.
    abbr = models.CharField(u'Χώρα(2) ',db_column='Abbr', max_length=2)  # Field name made lowercase.
    telephoneext = models.CharField(u'Τηλ', db_column='telephoneext', max_length=4)  # Field name made lowercase.

    def __unicode__(self):
        return self.name


class Locations(models.Model):
    id = models.AutoField
    name = models.CharField(db_column='Name', unique=True, max_length=50)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=60, blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tk = models.CharField(db_column='TK', max_length=5, blank=True, null=True)  # Field name made lowercase.
    text = models.TextField(db_column='Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hospital = models.NullBooleanField(db_column='Hospital')  # Field name made lowercase.
    medicalcenter = models.NullBooleanField(db_column='MedicalCenter')  # Field name made lowercase.
    eopyy = models.NullBooleanField(db_column='EOPYY')  # Field name made lowercase.
    contact = models.TextField(db_column='CONTACT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    countryid = models.ForeignKey(Country, db_column='CountryId')  # Field name made lowercase.
    peoples = models.ManyToManyField('People')

    def __unicode__(self):
        return self.name

class People(models.Model):
    id = models.AutoField
    name = models.CharField(u'Όνομα', db_column='Name', max_length=30)  # Field name made lowercase.
    surname = models.CharField(u'Επώνυμο',db_column='Surname', max_length=50)  # Field name made lowercase.
    dateofbirth = models.DateField(u'Ημερομηνία Γέννησης',db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(u'Υπηκοότητα',db_column='Nationality', max_length=20, blank=True, null=True)  # Field name made lowercase.
    countryid = models.ForeignKey(Country, verbose_name='Χώρα', db_column='CountryId')  # Field name made lowercase.
    phone = models.CharField(u'Τηλεφωνο',db_column='Phone', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(u'FAX',db_column='Fax', max_length=60, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(u'Κινητό',db_column='mobile', max_length=60, blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ispatient = models.NullBooleanField(u'Ασθενής',db_column='IsPatient')  # Field name made lowercase.
    isdoctor = models.NullBooleanField(u'Γιατρός',db_column='IsDoctor')  # Field name made lowercase.
    canlogin = models.NullBooleanField(db_column='CanLogin')  # Field name made lowercase.
    accessonlyhisfile = models.NullBooleanField(db_column='AccessOnlyHisFile')  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    photo = models.BinaryField(db_column='Photo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ordering = ('surname','name')

    def __unicode__(self):
        return self.surname + ' ' + self.name

class Dates(models.Model):
    id = models.AutoField
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    peopleid = models.ForeignKey(People, db_column='PeopleId')  # Field name made lowercase.
    doctorid = models.ForeignKey(People, limit_choices_to={'isdoctor': True} , related_name = 'Doctor')
    locationid = models.ForeignKey(Locations, db_column='LocationId')  # Field name made lowercase.
    examupdated = models.NullBooleanField(db_column='ExamUpdated')  # Field name made lowercase.
    examupdateddt = models.DateTimeField(db_column='ExamUpdatedDT', blank=True,
                                             null=True)  # Field name made lowercase.
    examposted = models.NullBooleanField(db_column='ExamPosted')  # Field name made lowercase.
    examposteddt = models.DateTimeField(db_column='ExamPostedDT', blank=True,
                                            null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True,
                                    null=True)  # Field name made lowercase. This field type is a guess.
    results = models.TextField(db_column='Results', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    def __unicode__(self):
        return str(self.date) + ' ' + unicode(self.peopleid) + ' ' + unicode(self.locationid)

class Datesexamlog(models.Model):
    id = models.AutoField
    dateid = models.IntegerField(db_column='DateId')  # Field name made lowercase.
    examid = models.IntegerField(db_column='ExamId')  # Field name made lowercase.
    mmid = models.IntegerField(db_column='MMId', blank=True, null=True)  # Field name made lowercase.
    result_n = models.TextField(db_column='Result_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    result_t = models.TextField(db_column='Result_T', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    updated = models.NullBooleanField(db_column='Updated')  # Field name made lowercase.

    def __unicode__(self):
        return str(self.dateid)


class Examname(models.Model):
    id = models.AutoField
    name = models.TextField(db_column='Name', unique=True)  # Field name made lowercase. This field type is a guess.
    sname = models.CharField(db_column='SName', max_length=25)  # Field name made lowercase.
    groupexam_id = models.IntegerField(db_column='GroupExam_Id')  # Field name made lowercase.
    mm_id = models.IntegerField(db_column='MM_Id')  # Field name made lowercase.
    min = models.TextField(db_column='Min', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    max = models.TextField(db_column='Max', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comments = models.CharField(db_column='Comments', max_length=250, blank=True, null=True)  # Field name made lowercase.
    is_numeric = models.NullBooleanField(db_column='Is_Numeric')  # Field name made lowercase.
    is_text = models.NullBooleanField(db_column='Is_Text')  # Field name made lowercase.
    is_memo = models.NullBooleanField(db_column='Is_Memo')  # Field name made lowercase.

    def __unicode__(self):
        return self.name

class Examminmax(models.Model):
    id = models.AutoField
    examid = models.ForeignKey(Examname, db_column='ExamId')  # Field name made lowercase.
    mmid = models.IntegerField(db_column='MMId', blank=True, null=True)  # Field name made lowercase.
    mfa = models.IntegerField(db_column='MFA')  # Field name made lowercase.
    minvalue = models.TextField(db_column='MinValue', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    maxvalue = models.TextField(db_column='MaxValue', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    def __unicode__(self):
        return self.examid

class Examschema(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(db_column='Name', unique=True, max_length=150, blank=True, null=True)  # Field name made lowercase.
    sequence = models.CharField(db_column='Sequence', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=150, blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
        return self.name

class Examschemadet(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    examschemaid = models.ForeignKey(Examschema, db_column='ExamSchemaid')  # Field name made lowercase.
    groupexamid = models.IntegerField(db_column='GroupExamId')  # Field name made lowercase.
    aa = models.IntegerField(db_column='AA')  # Field name made lowercase.

class Groupexam(models.Model):
    id = models.AutoField
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    sname = models.CharField(db_column='SName', max_length=50)  # Field name made lowercase.

    def __unicode__(self):
        return self.name


class Groupmm(models.Model):
    id = models.AutoField
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sname = models.CharField(db_column='SName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
        return self.name


class Keystable(models.Model):
    table = models.CharField(db_column='Table', primary_key=True, max_length=20)  # Field name made lowercase.
    currentkey = models.IntegerField(db_column='CurrentKey')  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated', blank=True, null=True)  # Field name made lowercase.


class Mfa(models.Model):
    id = models.AutoField
    fromage = models.IntegerField(db_column='FromAge')  # Field name made lowercase.
    toage = models.IntegerField(db_column='ToAge')  # Field name made lowercase.
    sex = models.IntegerField(db_column='SEX')  # Field name made lowercase.

class Mm(models.Model):
    id = models.AutoField
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sname = models.CharField(db_column='SName', max_length=8, blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
        return self.name

class Mm2Mm(models.Model):
    id = models.AutoField
    fromid = models.IntegerField(db_column='Fromid')  # Field name made lowercase.
    toid = models.IntegerField(db_column='Toid')  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=50, blank=True, null=True)  # Field name made lowercase.

class ExaminationCategory(models.Model):
    id = models.AutoField
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

    def surname(self):
        return self.peopleid.surname + ' ' + self.peopleid.name

    def __unicode__(self):
        a=self.dateofexam
        return self.peopleid.surname + ' ' + self.peopleid.name +  ' ' +a.strftime('%d/%m/%Y') + ' + ' + self.notes[:100]


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

class SqliteSpFunctions(models.Model):
    name = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)

class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)  # This field type is a guess.
    idx = models.TextField(blank=True, null=True)  # This field type is a guess.
    stat = models.TextField(blank=True, null=True)  # This field type is a guess.

class SqliteVsLinksNames(models.Model):
    name = models.TextField(blank=True, null=True)
    alias = models.TextField(blank=True, null=True)

class SqliteVsProperties(models.Model):
    parenttype = models.TextField(db_column='parentType', blank=True, null=True)  # Field name made lowercase.
    parentname = models.TextField(db_column='parentName', blank=True, null=True)  # Field name made lowercase.
    propertyname = models.TextField(db_column='propertyName', blank=True, null=True)  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='propertyValue', blank=True, null=True)  # Field name made lowercase.

class Person(models.Model):
    name = models.CharField(max_length=100)

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
    id = models.AutoField
    name = models.CharField(max_length=50)
    sname = models.CharField(max_length=15)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

