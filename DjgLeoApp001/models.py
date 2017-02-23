# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from django_datatables_view.base_datatable_view import BaseDatatableView

from django.core.urlresolvers import reverse

class Country(models.Model):
    id = models.AutoField
    name = models.CharField(u'Χώρα', max_length=50, unique=True)
    abbr = models.CharField(u'Χώρα(2)', max_length=2, unique=True)
    telephoneext = models.CharField(u'Τηλ', max_length=4) 

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listcountry')


class Examschema(models.Model):
    name = models.CharField(u'Σχήμα', unique=True, max_length=150)
    sequence = models.CharField(u'Σειρά',max_length=50, blank=True, null=True)
    notes = models.CharField(verbose_name=u'Σημειώσεις',max_length=150, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listexamschema')


class Locations(models.Model):
    id = models.AutoField
    name = models.CharField(u'Οναμασία',unique=True, max_length=50)
    address = models.CharField(u'Διεύθυνση', max_length=200, blank=True, null=True)
    phone = models.CharField(u'Τηλέφωνα', max_length=60, blank=True, null=True)
    mail = models.CharField(u'Email', max_length=50, blank=True, null=True)
    tk = models.CharField(u'TK', max_length=5, blank=True, null=True)
    text = models.TextField(u'Σχόλια', blank=True, null=True)
    hospital = models.NullBooleanField(u'Νοσοκομείο')
    medicalcenter = models.NullBooleanField(u'Ιατρικό Κέντρο')
    eopyy = models.NullBooleanField(u'ΕΟΠΠΥ')
    contact = models.TextField(u'Σύνδεσμος', blank=True, null=True)
    countryid = models.ForeignKey(Country, verbose_name=u'Χώρα')
    peoples = models.ManyToManyField('People', verbose_name=u'Ατομα', blank=True, null=True ) #TODO Delete null

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listlocation')


class People(models.Model):
    id = models.AutoField
    name = models.CharField(u'Όνομα',max_length=30)
    surname = models.CharField(u'Επώνυμο',max_length=50)
    dateofbirth = models.DateField(u'Ημερομηνία Γέννησης', blank=True, null=True)
    nationality = models.CharField(u'Υπηκοότητα',max_length=20, blank=True, null=True)
    countryid = models.ForeignKey(Country, verbose_name=u'Χώρα', db_column='CountryId')
    phone = models.CharField(u'Τηλέφωνο',max_length=60, blank=True, null=True)
    fax = models.CharField(u'FAX',max_length=60, blank=True, null=True)
    mobile = models.CharField(u'Κινητό',max_length=60, blank=True, null=True)
    mail = models.CharField(u'Email', max_length=250, blank=True, null=True)
    ispatient = models.NullBooleanField(u'Ασθενής',db_column='IsPatient')   
    isdoctor = models.NullBooleanField(u'Γιατρός',db_column='IsDoctor')   
    canlogin = models.NullBooleanField('CanLogin')
    accessonlyhisfile = models.NullBooleanField('Access Only His File')
    notes = models.CharField(verbose_name=u'Σημειώσεις', max_length=8192, blank=True, null=True)
    photo = models.BinaryField('Photo', blank=True, null=True)

    class Meta:
        ordering = ('surname','name')

    def __unicode__(self):
        return self.surname + ' ' + self.name

    def get_absolute_url(self):
        if self.isdoctor:
            return reverse('DjgLeoApp001:listd')
        else:
            return reverse('DjgLeoApp001:listp')

#max_digits=10, decimal_places=4,

class Examname(models.Model):
    name = models.CharField(verbose_name=u'Ονομασία', unique=True, max_length=100)
    sname = models.CharField(verbose_name=u'Συντμηση', max_length=25)
    minvalue = models.DecimalField(verbose_name=u'Ελάχιστο', default=0, max_digits=10, decimal_places=4 )
    maxvalue = models.DecimalField(verbose_name=u'Μέγιστο',  default=0, max_digits=10, decimal_places=4)
    comments = models.CharField(verbose_name=u'Σχόλια', max_length=250, blank=True, null=True)
    RESULT_TYPES = (
        (1, 'Αριθμητικό'),
        (2, 'Κείμενο'),
        (3, 'Αριθμητικό + Κείμενο'),
        (4, 'Εκτενές Κείμενο'),
        (5, 'Λογικό'),
        (9, 'Άλλο'),
    )
    result_type = models.IntegerField(max_length=1, choices=RESULT_TYPES, verbose_name=u'Είδος Απάντησης')
    bioexaminationcategory = models.ForeignKey('BioExaminationCategory', verbose_name=u'Κατηγορία', blank=True,null=True)
    groupexam = models.ForeignKey('GroupExam', verbose_name=u'Ομάδα(Group)', blank=True, null=True)
    mm = models.ForeignKey('mm', verbose_name=u'Mονάδα Mέτρησης(Min/Max)', blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', 'sname')

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listexamname')


class ExaminationCategory(models.Model):
    name = models.CharField(verbose_name=u'Ονομασία',max_length=50, unique=True)
    sname = models.CharField(verbose_name=u'Σύντμηση',max_length=15)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', 'sname')

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listexamcategory')


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
    peopleid = models.ForeignKey(People, verbose_name=u'Ασθενής')
    doctorid = models.ForeignKey(People, verbose_name=u'Γιατρός',limit_choices_to={'isdoctor': True} , related_name = 'Examination0Doctor')
    categorid = models.ForeignKey(ExaminationCategory,verbose_name=u'Κατηγορία')
    dateofexam = models.DateField(verbose_name=u'Ημερομηνία Εξέτασης')
    notes   = models.CharField(verbose_name=u'Σημειώσεις',max_length=8192, blank=True, null=True)
    comments = models.CharField(verbose_name=u'Σχόλια',max_length=8192, blank=True, null=True)

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
    notes       = models.CharField(verbose_name=u'Σημειώσεις',max_length=100)


class DoctorSpeciality(models.Model):
    name = models.CharField(verbose_name=u'Ονομασία',max_length=50, unique=True)
    sname = models.CharField(verbose_name=u'Σύντμηση',max_length=15)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', 'sname')

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listdoctorspec')


# OperationsCategory
class OperationCategory(models.Model):
    name = models.CharField(verbose_name=u'Ονομασία',max_length=50, unique=True)
    sname = models.CharField(verbose_name=u'Σύντμηση',max_length=15)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', 'sname')

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listoperationcategory')


# OperationsExamination
class Operations(models.Model):
    peopleid = models.ForeignKey(People,verbose_name=u'Ασθενής')
    doctorid = models.ForeignKey(People,verbose_name=u'Γιατρός', limit_choices_to={'isdoctor': True}, related_name='OperationDoctor')
    categorid = models.ForeignKey(OperationCategory,verbose_name=u'Κατηγορία')
    dateof = models.DateField(verbose_name=u'Ημερομηνία')
    notes = models.CharField(verbose_name=u'Σημειώσεις',max_length=8192, blank=True, null=True)
    comments = models.CharField(verbose_name=u'Σχόλια',max_length=8192, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listoperation', kwargs={'Patient': self.peopleid.id})

    def __unicode__(self):
        a = self.dateofexam
        return self.peopleid.surname + ' ' + self.peopleid.name + ' ' + a.strftime('%d/%m/%Y') + ' + ' + self.notes[:100]

    class Meta:
        ordering = ('dateof',)


# BioExaminationCategory
class BioExaminationCategory(models.Model):
    name = models.CharField(verbose_name=u'Ονομασία',max_length=50, unique=True)
    sname = models.CharField(verbose_name=u'Σύντμηση',max_length=15)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', 'sname')

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listbioexamcategory')


# BioExamination
class BioExamination(models.Model):
    peopleid = models.ForeignKey(People, verbose_name=u'Ασθενής')
    doctorid = models.ForeignKey(People, verbose_name=u'Γιατρός', limit_choices_to={'isdoctor': True} , related_name = 'ExaminationBioDoctor')
    categorid = models.ForeignKey(ExaminationCategory, verbose_name=u'Κατηγορία')
    examsschema = models.ManyToManyField('Examschema', verbose_name = u'Σχήμα')
    dateofexam = models.DateField(verbose_name=u'Ημερομηνία Εξέτασης')
    notes   = models.CharField(verbose_name=u'Σημειώσεις',max_length=8192, blank=True, null=True)
    comments = models.CharField(verbose_name=u'Σχόλια',max_length=8192, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listexambio', kwargs={'Patient': self.peopleid.id})

    def __unicode__(self):
        a=self.dateofexam
        return self.peopleid.surname + ' ' + self.peopleid.name +  ' ' +a.strftime('%d/%m/%Y') + ' + ' + self.notes[:100]

    class Meta:
        ordering = ('-dateofexam',)



class BioExaminationDetail(models.Model):
    BioExaminationId = models.ForeignKey(BioExamination, verbose_name='Αφορά')
    examnameid = models.ForeignKey(Examname, verbose_name='Εξέταση')
    value = models.FloatField('Τιμή', blank = True, null = True )
    notes = models.CharField(verbose_name=u'Σημειώσεις',max_length=255, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listexambiodet', kwargs={'exampk': self.BioExaminationId.pk})

    class Meta:
        unique_together = (("BioExaminationId", "examnameid" ),)
        ordering = ('BioExaminationId','examnameid','id')

    def __unicode__(self):
        return self.examnameid.name

# MedicineCategory
class MedicineCategory(models.Model):
    id = models.AutoField
    name = models.CharField(verbose_name=u'Ονομασία',max_length=50, unique=True)
    sname = models.CharField(verbose_name=u'Σύντμηση',max_length=15)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', 'sname')

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listmedicinecategory')


# Medicine
class Medicine(models.Model):
    peopleid  = models.ForeignKey(People,verbose_name=u'Ασθενής')
    doctorid  = models.ForeignKey(People,verbose_name=u'Γιατρός', limit_choices_to={'isdoctor': True} , related_name = 'MedicineDoctor')
    categorid = models.ForeignKey(MedicineCategory,verbose_name=u'Κατηγορία')
    dateof    = models.DateField(verbose_name=u'Ημερομηνία')
    datestart = models.DateField(verbose_name=u'Από')
    dateend   = models.DateField(verbose_name=u'Έως')
    notes     = models.CharField(verbose_name=u'Σημειώσεις',max_length=8192, blank=True, null=True)

    class Meta:
        unique_together = (("peopleid", "doctorid", "categorid", "dateof" ),)
        ordering = ('-dateof',)

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listmedicine', kwargs={'Patient': self.peopleid.id})

    def __unicode__(self):
        a=self.dateofexam
        return self.peopleid.surname + ' ' + self.peopleid.name +  ' ' +a.strftime('%d/%m/%Y') + ' + ' + self.notes[:100]


class GroupExam(models.Model):
    name = models.CharField(verbose_name=u'Ονομασία', max_length=50, unique=True)
    sname = models.CharField(verbose_name=u'Σύντμηση', max_length=15)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listgroupexam')

    class Meta:
        ordering = ('name',)


class MMType(models.Model):
    name = models.CharField(verbose_name=u'Ονομασία', max_length=50, unique=True)
    sname = models.CharField(verbose_name=u'Σύντμηση', max_length=15)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listmmtype')

    class Meta:
        ordering = ('name',)


class MM(models.Model):
    name = models.CharField(verbose_name=u'Ονομασία', max_length=50, unique = True)
    sname = models.CharField(verbose_name=u'Σύντμηση', max_length=15)
    mmtype = models.ForeignKey('MMType', verbose_name=u'Είδος', blank=True, null=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('DjgLeoApp001:listmm')

    class Meta:
        ordering = ('name',)

