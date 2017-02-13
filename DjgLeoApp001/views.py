# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.forms.models import modelform_factory
from django import forms

import django_tables2 as tables
from django.shortcuts import render
from django_tables2 import RequestConfig
from django.utils.html import mark_safe
from  django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from datetimewidget.widgets import DateTimeWidget
from datetimewidget.widgets import DateWidget

class ModelFormWidgetMixin(object):
    def get_form_class(self):
        return modelform_factory(self.model, fields=self.fields, widgets=self.widgets)

GlobPeopleid=0
GlobDoctorid=0
GlobPeopleidNum=0
GlobDoctoridNum=0

import datetime

from models import People

from django.contrib.admin import AdminSite
class MyAdminSite(AdminSite):
        pass

mysite = MyAdminSite()


def MainMenu(request):
    return render(request, 'NewMenuBootStrap.html')
#    return render(request, 'baseMenu.html')
#    return render(request, 'baseMenu.html',{'user': request.user, 'site_header': mysite.site_header, 'has_permission': mysite.has_permission(request),
#                                            'site_url': mysite.site_url})

def NewMenu(request):
    return render(request, 'NewMenu.html')

def NewMenu1(request):
    return render(request, 'NewMenuBootStrap.html')

from django.shortcuts import render
def people0(request):
    return render(request, 'people.html' , {'people': People.objects.all(), 'add_url_leo': 'locationcreate' } )

from models import Examination0
def examination00(request):
    return render(request, 'people.html', {'people': Examination0.objects.all()})



from models import Examname
def people1(request):
    return render(request, 'people.html', {'people': Examname.objects.all()})


def people10(request):
    return render(request, 'people0.html', {'my-table':Examname.objects.all()})

def detail(request, id):
    return HttpResponse("You're looking at question %s." % id)

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def current_datetime2(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})

def test(request):
    return render_to_response('mypage.html', {'title': 'Leonidas','current_section':'Kapa'})

def results(request, id):
    try:
        p=People.objects.get(pk=id)
        return render_to_response('myPeople.html', {'title': 'Leonidas', 'current_section': 'Kapa','p':p})
    except People.DoesNotExist:
        return HttpResponse("People does not exist")

def results0(request, id):
    try:
        p=People.objects.get(pk=id)
        response = "You're looking at the results of question %s %s." % (p.name,p.surname)
    except People.DoesNotExist:
        response = "People does not exist"
#        raise Http404("People does not exist")
#    return render(request,response)
    return HttpResponse(response)

def people_det(request, id):
    try:
        p = People.objects.get(pk=id)
        response = "You're looking for people %s %s." % (p.name, p.surname)
    except People.DoesNotExist:
        response = "People does not exist"
    return HttpResponse(response)


def vote(request,id):
    return HttpResponse("You're voting on question %s." % id)


def index(request):
    latest_question_list = People.objects.order_by('-name')[:5]
    output = ', '.join([q.name+' '+q.surname+'\n' for q in latest_question_list])
    return HttpResponse(output)
#    return HttpResponse(latest_question_list)


from django.http import HttpResponseRedirect

from forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
##            send_mail(
##                cd['subject'],
##                cd['message'],
##                cd.get('email', 'noreply@example.com'),
##                ['siteowner@example.com'],
##            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})


class PeopleList(ListView):
    model = People

class PeopleDetailView(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,DetailView):
    model = People

    def test_func(self):
        return True


class PeopleCreare(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,CreateView):
    model = People
    fields = ['id', 'name', 'surname', 'mail', 'dateofbirth', 'nationality',
              'countryid', 'phone', 'mail', 'mobile', 'ispatient', 'isdoctor', 'canlogin',
              'accessonlyhisfile', 'notes']
    template_name_suffix = '_create_form'
    success_url = '/publishers/'

    widgets = {
        'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
        'dateofbirth': DateWidget(attrs={'id': "id_dateofbirth"}, bootstrap_version=3)
        }
    def test_func(self):
        return True


class PeopleUpdate(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,UpdateView):
    model = People
    fields = ['id','name','surname','mail','dateofbirth','nationality',
              'countryid','phone','mail','mobile','ispatient','isdoctor','canlogin',
              'accessonlyhisfile','notes']
    template_name_suffix = '_update_formt'
#    success_url = '/publishers/'
    success_url = '/tables10/'
    widgets = {
        'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
        'dateofbirth': DateWidget(attrs={'id': "id_dateofbirth"}, bootstrap_version=3)
        }
    def test_func(self):
        return True


class PeopleDelete(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,DeleteView):
    model = People
    fields = ['name','surname','notes','mail']
    success_url = '/publishers/'
    def test_func(self):
        return True




#Examination0
from models import Examination0

def ExaminationsListPer000(request):
    queryset  = Examination0.objects.all()
    table = Examination0(queryset)
    RequestConfig(request).configure(table)
    return render(request, 'examination0_list.html', {'object_list': table})

from django.contrib.auth.decorators import login_required
#@login_required(login_url='/login/')

from django.conf import settings
from django.shortcuts import redirect

class ExaminationsList(LoginRequiredMixin,UserPassesTestMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Examination0

    def test_func(self):
        return True


#    def test_func(self):
#        return self.request.user.email.endswith('com')

class ExaminationsList0(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,ListView):
    model = Examination0

    def __init__(self, *args, **kwargs):
        super(ExaminationsList, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'notes',
                'peopleid',
                'categorid'
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )

    def test_func(self):
        return True




from django.shortcuts import get_object_or_404

class ExaminationsListPer(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    model = Examination0
    template_name = 'examination_list_per_person.html'
#    queryset  = Examination0.dahl_objects.all()
#    queryset  = Examination0.leo_objects.all()
#    queryset  = Examination0.objects.filter(peopleid=1)
    def get_queryset(self):
        self.id = get_object_or_404(People,id=self.args[0])
        self.name = get_object_or_404(People,id=self.args[0])
        return Examination0.objects.filter(peopleid=self.id)

    def get_context_data(self, **kwargs):
# Call the base implementation first to get a context
        context = super(ExaminationsListPer, self).get_context_data(**kwargs)
# Add in the publisher
        context['publisher'] = self.id
        context['name'] = u' για ' + self.name.surname + ' ' +  self.name.name
        return context

    def test_func(self):
        return True


class ExaminationsListPerDoctor(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    model = Examination0
    template_name = 'examination_list_per_person.html'
    def get_queryset(self):
        self.id = get_object_or_404(People,id=self.args[0])
        self.name = get_object_or_404(People,id=self.args[0])
        return Examination0.objects.filter(doctorid=self.id)

    def get_context_data(self, **kwargs):
        context = super(ExaminationsListPerDoctor, self).get_context_data(**kwargs)
        context['publisher'] = self.id
        context['name'] = u' απο ' +  self.name.surname
        return context

    def test_func(self):
        return True


class ExaminationsListPerDoctorPatient(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,ListView):
    model = Examination0
    template_name = 'examination_list_per_person.html'
    def get_queryset(self):
        self.did = get_object_or_404(People,id=self.args[0])
        self.dname = get_object_or_404(People,id=self.args[0])
        self.pid = get_object_or_404(People,id=self.args[1])
        self.pname = get_object_or_404(People,id=self.args[1])

        return Examination0.objects.filter(doctorid=self.did,peopleid=self.pid)

    def get_context_data(self, **kwargs):
        context = super(ExaminationsListPerDoctorPatient, self).get_context_data(**kwargs)
        context['publisher'] = self.pid
        context['name'] = u' για ' + self.pname.name + ' ' + self.pname.surname + u' απο ' + self.dname.name + ' ' + self.dname.surname
        return context

    def test_func(self):
        return True


from models import ExaminationCategory

class ExaminationsListPerCategory(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,ListView):
    model = Examination0
    def get_queryset(self):
        self.id = get_object_or_404(ExaminationCategory,id=self.args[0])
        return Examination0.objects.filter(categorid=self.id)

    def test_func(self):
        return True


from django.views.generic.detail import DetailView

class ExaminationDetail(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,DetailView):
    model = Examination0

    def test_func(self):
        return True


from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget

class ExaminationCreare(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,CreateView):
    model = Examination0
    fields = ['peopleid','doctorid','categorid','dateofexam','notes','comments']
    template_name_suffix = '_create_form'
    success_url = '/examinations/'
    widgets = {
        'dateofexam': DateWidget(attrs={'id': "id_dateofexam"}, bootstrap_version=3),
        'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
        'comments': forms.Textarea(attrs={'cols': 100, 'rows': 5}),
        }

    def test_func(self):
        return True


class ExaminationUpdate(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,UpdateView):
    model = Examination0
    fields = ['peopleid','doctorid','categorid','dateofexam','notes','comments']
    readonly_fields = ('peopleid','categorid','dateofexam')
    template_name_suffix = '_update_form'
    success_url = '/examinations/'
    widgets = {
        'dateofexam': DateWidget(attrs={'id': "id_dateofexam"}, bootstrap_version=3),
        'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10, 'readonly' : True}),
        'comments': forms.Textarea(attrs={'cols': 100, 'rows': 5, 'readonly' : True}),
        }

    def test_func(self):
        return True


class ExaminationDelete(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,DeleteView):
    model = Examination0
    fields = ['peopleid','doctorid','categorid','dateofexam','notes','comments']
    success_url = '/examinations/'

    def test_func(self):
        return True


class ExaminationTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])
    edit = tables.LinkColumn('item_edit', args=[('pk')],orderable=False,empty_values=[''])
#    delete = tables.LinkColumn('item_delete', args=[('pk')],orderable=False,empty_values=[''])
    class Meta:
        model = Examination0
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id','nationality','idoncontry','ispatient','notes','isdoctor','canlogin','accessonlyhisfile','photo','notes'] 
#        fields
        sequence = ['dateofexam','...']

    def render_edit(self, record):
        return mark_safe('<a href=/examinationupd/' + str(record.pk) + '/><span style="color:blue">Edit</span></a>')

    def render_delete(self, record):
        return mark_safe('<a href=/examinationdel/' + str(record.pk) + '/><span style="color:red">Delete</span></a>')

    def render_detail(self, record):
        return mark_safe('<a href=/examinationdet/' + str(record.pk) + '/><span style="color:green">View</span></a></a>')


def examination_list(request):
    table = ExaminationTable(Examination0.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'people.html', {'people': table, 'page_title' : 'Εξετάσεις', 'add_url_leo': 'examinationcreate' })


#Crispy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, MultiField

class ExampleForm0(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,CreateView):
    model = People
    fields = ['name', 'surname', 'notes', 'mail', 'dateofbirth', 'nationality', 'countryid',
              'phone', 'fax', 'mail', 'ispatient', 'isdoctor', 'canlogin',
              'accessonlyhisfile', 'notes']
    success_url = '/examinations'

    def __init__(self, *args, **kwargs):
        super(ExampleForm0, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm0'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'get'
        self.helper.form_action = '/examinations'

#        self.template = 'example_form0.html'

#        self.helper.form_class = 'form-inline'
#        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
#        self.helper.field_template = 'bootstrap3/layout/multifield.html'

#        self.helper.form_class = 'form-horizontal'
#        self.helper.label_class = 'col-lg-2'
#        self.helper.field_class = 'col-lg-8'

        self.helper.layout = Layout(
            HTML("{% extends 'base.html' %}"),
            Fieldset(
                    'Please mr {{ user.username }}',
                    'name',
                    'surname',
                    'dateofbirth',
                    'countryid',
                    'nationality'
            ),
            Fieldset(
            'Contact Information',
            'mail',
            'phone',
            'fax'
            )
        )

        self.helper.add_input(Submit('submit', 'Submit'))

#        self.helper.layout.append(HTML("<p>whatever</p>"))


    def get_context_data(self, **kwargs):
        context = super(ExampleForm0, self).get_context_data(**kwargs)
        context['helper'] = self.helper
        return context

    def test_func(self):
        return True


from django.shortcuts import render

from  django.shortcuts import render_to_response
from django.template import RequestContext

def index1(request):
    example_form0 = ExampleForm0()
    return render_to_response("example_form0.html",
                              {"form": example_form0 ,"example_form0": example_form0},)

#DataTables
import django
from django.views.generic import View, TemplateView
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.defaultfilters import timesince

import datatableview
from datatableview import Datatable, ValuesDatatable, columns, SkipRecord
from datatableview.views import DatatableView, MultipleDatatableView, XEditableDatatableView
from datatableview.views.legacy import LegacyDatatableView
from datatableview import helpers

class ValidColumnFormatsView(TemplateView):
    template_name = "valid_column_formats.html"

import re    

class DemoMixin(object):
    description = """Missing description!"""
    implementation = """Missing implementation details!"""

    def get_template_names(self):
        """ Try the view's snake_case name, or else use default simple template. """
        name = self.__class__.__name__.replace("DatatableView", "")
        name = re.sub(r'([a-z]|[A-Z]+)(?=[A-Z])', r'\1_', name)
        return [name.lower() + ".html", "example_base.html"]

    def get_context_data(self, **kwargs):
        context = super(DemoMixin, self).get_context_data(**kwargs)
        context['implementation'] = self.implementation

        # Unwrap the lines of description text so that they don't linebreak funny after being put
        # through the ``linebreaks`` template filter.
        alert_types = ['info', 'warning', 'danger']
        paragraphs = []
        p = []
        alert = False
        for line in self.__doc__.splitlines():
            line = line[4:].rstrip()
            if not line:
                if alert:
                    p.append(u"""</div>""")
                    alert = False
                paragraphs.append(p)
                p = []
            elif line.lower()[:-1] in alert_types:
                p.append(u"""<div class="alert alert-{type}">""".format(type=line.lower()[:-1]))
                alert = True
            else:
                p.append(line)
        description = "\n\n".join(" ".join(p) for p in paragraphs)
        context['description'] = re.sub(r'``(.*?)``', r'<code>\1</code>', description)

        return context
    

# Column configurations
class ZeroConfigurationDatatableView(DemoMixin, DatatableView):
    """
    If no columns are specified by the view's ``Datatable`` configuration object (or no
    ``datatable_class`` is given at all), ``DatatableView`` will use all of the model's local
    fields.  Note that this does not include reverse relationships, many-to-many fields (even if the
    ``ManyToManyField`` is defined on the model directly), nor the special ``pk`` field, but DOES
    include ``ForeignKey`` fields defined directly on the model.

    Note that fields will automatically use their ``verbose_name`` for the frontend table headers.

    WARNING:
    When no columns list is explicitly given, the table will end up trying to show foreign keys as
    columns, generating at least one extra query per displayed row.  Implement a ``get_queryset()``
    method on your view that returns a queryset with the appropriate call to ``select_related()``.
    """

    model = Examination0

    implementation = u"""
    class ZeroConfigurationDatatableView(DatatableView):
        model = Entry
    """

# Column configurations
class ZeroConfigurationDatatableView0(DemoMixin, DatatableView):
    """
    If no columns are specified by the view's ``Datatable`` configuration object (or no
    ``datatable_class`` is given at all), ``DatatableView`` will use all of the model's local
    fields.  Note that this does not include reverse relationships, many-to-many fields (even if the
    ``ManyToManyField`` is defined on the model directly), nor the special ``pk`` field, but DOES
    include ``ForeignKey`` fields defined directly on the model.

    Note that fields will automatically use their ``verbose_name`` for the frontend table headers.

    WARNING:
    When no columns list is explicitly given, the table will end up trying to show foreign keys as
    columns, generating at least one extra query per displayed row.  Implement a ``get_queryset()``
    method on your view that returns a queryset with the appropriate call to ``select_related()``.
    """

    model = Examname

    implementation = u"""
    class ZeroConfigurationDatatableView(DatatableView):
        model = Examname
    """
    
###Locations>

import models

class LocationTable(tables.Table):
    edit = tables.LinkColumn('item_edit', args=[('pk')],orderable=False,empty_values=[''])
    detail = tables.LinkColumn('item_detail', args=[('pk')],orderable=False,empty_values=[''])
    delete = tables.LinkColumn('item_delete', args=[('pk')],orderable=False,empty_values=[''])
    class Meta:
        model = models.Locations
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['phone', 'hospital', 'medicalcenter', 'eopyy', 'contact']
#        fields
#        sequence = ['name','surname','countryid','phone','...']

    def render_edit(self,record):
        return mark_safe('<a href=/locationupd/'+str(record.pk)+'/><span style="color:blue">Edit</span></a>')

    def render_delete(self,record):
        return mark_safe('<a href=/locatiodel/'+str(record.pk)+'/><span style="color:red">Delete</span></a>')

    def render_detail(self,record):
        return mark_safe('<a href=/location/'+str(record.pk)+'/><span style="color:green">Det.◙</span></a></a>')

#✔
#✘
#☺☻▓▒■□▪▫▲►▼◄◊○◌●◘▬◙☼⌂
#< span class ="false" > ✘ < / span >
#< span class ="false" > ✘ < / span >
#<span style="color:blue">


def locations_list(request):
    table = LocationTable(models.Locations.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'people.html', {'people': table, 'add_url_leo':'locationcreate', 'page_title':u'Τοποθεσία'})

class LocationDetailView(DetailView):
    model = models.Locations

    def get_context_data(self, **kwargs):
        context = super(LocationDetailView, self).get_context_data(**kwargs)
        return context

class LocationCreare(CreateView):
    model = models.Locations
    fields =  ['name', 'address', 'phone', 'mail', 'tk', 'text', 'hospital', 'medicalcenter', 'eopyy', 'contact', 'countryid','peoples']
    template_name_suffix = '_create_form'

class LocationUpdate(UpdateView):
    model = models.Locations
    fields =  ['name', 'address', 'phone', 'mail', 'tk', 'text', 'hospital', 'medicalcenter', 'eopyy', 'contact', 'countryid','peoples']
    template_name_suffix = '_update_form'
    success_url = '/locations/'

class LocationDelete(DeleteView):
    model = models.Locations
    fields = ['name','surname','notes','mail']
    success_url = '/locations/'

###Locations<

###MultiExamForm>

from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin.widgets import AdminTimeWidget
from django.contrib.admin.widgets import AdminSplitDateTime

from django.contrib.admin import widgets

class CustomAdminSplitDateTime(AdminSplitDateTime):
    def __init__(self, attrs=None):
        widgets = [AdminDateWidget, AdminTimeWidget(attrs=None, format='%I:%M %p')]
        forms.MultiWidget.__init__(self, widgets, attrs)    

class MultiExamForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    phone = forms.CharField()
    mail = forms.EmailField(required=False)
    tk = forms.CharField()
    text = forms.CharField()
    #hospital = forms.NullBooleanField(db_column='Hospital')  # Field name made lowercase.
    #medicalcenter = models.NullBooleanField(db_column='MedicalCenter')  # Field name made lowercase.
    #eopyy = models.NullBooleanField(db_column='EOPYY')  # Field name made lowercase.
#    contact = forms.CharField()
    #countryid = forms.ForeignKey(Country, db_column='CountryId')  # Field name
    CHOICES = (('1', 'First',), ('2', 'Second',))
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    choice_field1 = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
#    choice_field2 = forms.SplitDateTimeField()
#    choice_field3 = forms.SplitDateTimeWidget()
    choice_field4 = forms.DateField(widget=widgets.AdminDateWidget())

#    start_datetime = forms.DateField(
#        widget=CustomAdminSplitDateTime())
#    end_datetime= forms.DateField(
#        widget=CustomAdminSplitDateTime())
        

    OPTIONS = (
                ("AUT", "Austria"),
                ("DEU", "Germany"),
                ("NLD", "Neitherlands"),
                ("GRE", "Greece"),
                )
    Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=OPTIONS)

    countries1 = forms.ModelChoiceField(queryset=People.objects.all())

    countries2 = forms.ModelMultipleChoiceField(queryset=People.objects.all())

    


def MultiExam(request):
    if request.method == 'POST':
        form = MultiExamForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print cd['mail']
            print cd['Countries']
            print cd['countries1']
            print cd['countries2']
##            send_mail(
##                cd['subject'],
##                cd['message'],
##                cd.get('email', 'noreply@example.com'),
##                ['siteowner@example.com'],
##            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = MultiExamForm()
    return render(request, 'contact_form.html', {'form': form})

def MultiExam0(request):
    if request.method == 'POST':
        form = MultiExamForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
##            send_mail(
##                cd['subject'],
##                cd['message'],
##                cd.get('email', 'noreply@example.com'),
##                ['siteowner@example.com'],
##            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = MultiExamForm()
    return render(request, 'contact_form0.html', {'form': form})

    

class ExaminationsListPerTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])
    edit = tables.LinkColumn('item_edit', args=[('pk')],orderable=False,empty_values=[''])
    delete = tables.LinkColumn('item_delete', args=[('pk')],orderable=False,empty_values=[''])
    class Meta:
        model = Examination0
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id','nationality','idoncontry','ispatient','notes','isdoctor','canlogin','accessonlyhisfile','photo','notes']
#        fields
#        sequence = ['dateofexam','...']

    def render_edit(self, record):
        return mark_safe('<a href=/examinationupd/' + str(record.pk) + '/><span style="color:blue">Edit</span></a>')

    def render_delete(self, record):
        return mark_safe('<a href=/examinationdel/' + str(record.pk) + '/><span style="color:red">Delete</span></a>')

    def render_detail(self, record):
        return mark_safe('<a href=/examinationdet/' + str(record.pk) + '/><span style="color:green">View</span></a></a>')


def ExaminationsListPer_Table(request,pk):
    id = get_object_or_404(People, id=pk)
    table = ExaminationsListPerTable(Examination0.objects.filter(peopleid=id))
    RequestConfig(request).configure(table)
    return render(request, 'people.html', {'people': table})

#
class DoctorListTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')],orderable=False,empty_values=[''])
    exams  = tables.LinkColumn('item_exams', args=[('pk')],orderable=False,empty_values=[''])
    class Meta:
        model = models.People
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['dateofbirth', 'nationality', 'countryid', 'ispatient', 'isdoctor', 'canlogin', 'accessonlyhisfile', 'notes' ,'id', 'photo']
        sequence = ['name','surname','...']

    def render_exams(self, record):
        return mark_safe('<a href=/examinationsListPerDoctor/'+str(record.pk)+'/><span style="color:blue">Εξετάσεις</span></a>')

    def render_detail(self,record):
        return mark_safe('<a href=/DjgLeoApp001/detail/'+str(record.pk)+'/><span style="color:green">Λεπτομέριες</span></a></a>')

def doctor_list(request):
    table = DoctorListTable(models.People.objects.all().filter(isdoctor=1))
    RequestConfig(request).configure(table)
    return render(request, 'people.html', {'people': table, 'add_url_leo':'DjgLeoApp001:create', 'page_title':u'Γιατροί','name':u'Γιατροί'})


#Patient Table
class PatientListTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')],orderable=False,empty_values=[''])
    exam   = tables.LinkColumn('item_exam', args=[('pk')],orderable=False,empty_values=[''])
    exambio  = tables.LinkColumn('item_exambio', args=[('pk')],orderable=False,empty_values=[''])
    medicine  = tables.LinkColumn('item_medicine', args=[('pk')],orderable=False,empty_values=[''])
    operation  = tables.LinkColumn('item_operation', args=[('pk')],orderable=False,empty_values=[''])
    class Meta:
        model = models.People
        row_attrs = {
            'data-id': lambda record: record.pk,
        }
        attrs = {'class': 'paleblue'}
        exclude = ['dateofbirth', 'nationality', 'countryid', 'ispatient', 'isdoctor', 'canlogin', 'accessonlyhisfile', 'notes' ,'id', 'photo']
        sequence = ['name','surname','...']

    def render_detail(self,record):
        return mark_safe('<a href=/DjgLeoApp001/detail/'+str(record.pk)+'/><span style="color:green">Λεπτομέριες</span></a></a>')

    def render_exam(self, record):
        return mark_safe('<a href=/DjgLeoApp001/listexam/'+str(record.pk)+'/><span style="color:blue">Εξετάσεις</span></a>')

    def render_exambio(self, record):
        return mark_safe('<a href=/DjgLeoApp001/listexambio/'+str(record.pk)+'/><span style="color:blue">Βιοχημικές Εξετάσεις</span></a>')

    def render_medicine(self, record):
        return mark_safe('<a href=/DjgLeoApp001/listmedicine/'+str(record.pk)+'/><span style="color:blue">Φάρμακα</span></a>')

    def render_operation(self, record):
        return mark_safe('<a href=/DjgLeoApp001/listoperation/'+str(record.pk)+'/><span style="color:blue">Επεμβάσεις</span></a>')


# leo    examination_list

from .models import SpecialUsers
from django.contrib.auth.models import User
from django.db.models import Q
import operator

def patient_list(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    u = User.objects.get(username=request.user)
    if request.user.is_superuser or request.user.is_staff:
        print 'Super'
    us = SpecialUsers.objects.get(user=request.user)

    # qlist = []
    # q_object = Q()
    # for x in us.peoples.all():
    #     a=('id',str(x.id))
    #     qlist.append(a)

    q_object = Q()
#    print q_object
    bb=[]
    for x in us.peoples.all():
        aa=x.id
        bb.append(x.id)
        q_object.add(Q(id=aa),Q.OR)
    global GlobPeopleid
    GlobPeopleid = bb[:]
#        print q_object

# #    qlist.append(('ispatient','1'))
#     q_list = [Q(x) for x in qlist]
#     print  q_list
#     print q_object
#     print reduce(operator.or_, q_list)

    table = PatientListTable(models.People.objects.all().filter(q_object))

#    table = PatientListTable(models.People.objects.all().filter(ispatient=1).filter(reduce(operator.or_,q_list)))
#    table = PatientListTable(models.People.objects.all().filter(ispatient=1))

    RequestConfig(request).configure(table)
    return render(request, 'people.html', {'people': table, 'add_url_leo':'DjgLeoApp001:create', 'page_title':u'Ασθενείς','name': u'Ασθενείς' })

class PeopleTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')],orderable=False,empty_values=[''])
#    edit = tables.LinkColumn('item_edit', args=[('pk')],orderable=False,empty_values=[''])
#    exam = tables.LinkColumn('item_exam', args=[('pk')],orderable=False,empty_values=[''])
#    delete = tables.LinkColumn('item_delete', args=[('pk')],orderable=False,empty_values=[''])
    class Meta:
        model = People
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['nationality','id','idoncontry','ispatient','isdoctor','canlogin','accessonlyhisfile','photo','notes']
#        fields
        sequence = ['name','surname','countryid','phone','...']

    def render_detail(self, record):
        return mark_safe('<a href=/DjgLeoApp001/detail/' + str(record.pk) + '/><span style="color:green">Λεπτομέριες</span></a></a>')

#    def render_edit(self, record):
#        return mark_safe('<a href=/publisherupd/' + str(record.pk) + '/><span style="color:blue">Edit</span></a>')

#    def render_delete(self, record):
#        return mark_safe('<a href=/publisherdel/' + str(record.pk) + '/><span style="color:red">Delete</span></a>')

#    def render_exam(self, record):
#        return mark_safe('<a href=/examinationsper/' + str(record.pk) + '/><span style="color:green">Exams◙</span></a></a>')

#@login_required
def person_list(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = PeopleTable(People.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'people.html', {'people': table, 'add_url_leo': 'DjgLeoApp001:create', 'page_title': u'Άνθρωποι'})


def people10(request):
    queryset  = People.objects.all()
    table = PeopleTable(queryset)
    RequestConfig(request).configure(table)
    return render(request, 'people.html', {'people': table})

###MultiExamForm<


def examination_list_per(request,pk):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    id = get_object_or_404(People, id=pk)
    table = ExaminationTable(Examination0.objects.filter(peopleid=pk))
    RequestConfig(request).configure(table)
    return render(request, 'people.html', {'people': table, 'page_title' : 'Εξετάσεις', 'add_url_leo': 'examinationcreate' })


########################################################################################################
#BioExamination

from .models import BioExamination

class BioExaminationTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')],orderable=False,empty_values=[''])
    detaildet = tables.LinkColumn('item_detaildet', args=[('pk')], orderable=False, empty_values=[''])
    class Meta:
        model = BioExamination
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['peopleid', 'examsschema', 'comments' , 'id']
        sequence = ['dateofexam','doctorid','categorid','...']

    def render_detail(self, record):
        rev=reverse('DjgLeoApp001:detailexambio', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href='+rev+u'><span style="color:red">Λεπτομέρειες</span></a>')
    
    def render_detaildet(self, record):
        rev=reverse('DjgLeoApp001:listexambiodet', kwargs={'exampk': str(record.pk)})
        return mark_safe('<a href='+rev+u'><span style="color:red">Αναλυτικά</span></a>')


#@login_required
def BioExaminationList(request,Patient):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = BioExaminationTable(BioExamination.objects.all().filter(peopleid=Patient))
    global GlobPeopleidNum
    GlobPeopleidNum = Patient
    RequestConfig(request).configure(table)
    p = People.objects.get(pk=Patient)
    return render(request, 'people.html', {'people': table, 'add_url_leo': 'DjgLeoApp001:createexambio', 'page_title': u'aaa',
                                           'name': u'Βιοχημικές για ' + p.name + ' ' + p.surname})


class BioExaminationCreare(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,CreateView):
    model = BioExamination
    fields = ['peopleid','doctorid','categorid','dateofexam','examsschema','notes','comments']
    template_name_suffix = '_create_form'
    widgets = {
        'dateofexam': DateWidget(attrs={'id': "id_dateofexam"}, bootstrap_version=3),
        'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
        'comments': forms.Textarea(attrs={'cols': 100, 'rows': 10})
        }
    global GlobPeopleidNum
    def get_initial(self):
        return  {'peopleid': GlobPeopleidNum}

    def test_func(self):
        return True

class BioExaminationDetailView(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,DetailView):
    model = BioExamination
    def get_context_data(self, **kwargs):
        context = super(BioExaminationDetailView, self).get_context_data(**kwargs)
        return context
    def test_func(self):
        return True

class BioExaminationUpdate(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,UpdateView):
    model = BioExamination
    fields = ['peopleid', 'doctorid', 'categorid', 'dateofexam', 'examsschema', 'notes', 'comments']
    template_name_suffix = '_update_form'
    widgets = {
        'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
        'comments': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
        'dateofexam': DateWidget(attrs={'id': "id_dateofexam"}, bootstrap_version=3)
        }
    def test_func(self):
        return True

class BioExaminationDelete(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,DeleteView):
    model = BioExamination
    def test_func(self):
        return True

####

########################################################################################################

########################################################################################################
# Medicine

from .models import Medicine

class MedicineTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = Medicine
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['peopleid', 'comments', 'id']
        sequence = ['dateof', 'doctorid', '...']

    def render_detail(self, record):
        rev = reverse('DjgLeoApp001:detailmedicine', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Λεπτομέρειες</span></a>')

# @login_required
def MedicineList(request, Patient):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = MedicineTable(Medicine.objects.all().filter(peopleid=Patient))
    global GlobPeopleidNum
    GlobPeopleidNum = Patient
    RequestConfig(request).configure(table)
    p = People.objects.get(pk=Patient)
    return render(request, 'people.html',
                  {'people': table, 'add_url_leo': 'DjgLeoApp001:createmedicine', 'page_title': u'Φάρμακα' ,
                  'name': u'Φάρμακα για ' + p.name + ' ' + p.surname})


class MedicineCreare(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, CreateView):
    model = Medicine
    fields = ['peopleid', 'doctorid', 'categorid', 'dateof', 'datestart', 'dateend', 'notes']
    template_name_suffix = '_create_form'
    widgets = {
        'dateof': DateWidget(attrs={'id': "id_dateof"}, bootstrap_version=3),
        'datestart': DateWidget(attrs={'id': "id_datestart"}, bootstrap_version=3),
        'dateend': DateWidget(attrs={'id': "id_dateend"}, bootstrap_version=3),
        'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10})
    }

    global GlobPeopleidNum
    def get_initial(self):
        return  {'peopleid': GlobPeopleidNum}

    def test_func(self):
        return True

class MedicineDetailView(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, DetailView):
    model = Medicine

    def get_context_data(self, **kwargs):
        context = super(MedicineDetailView, self).get_context_data(**kwargs)
        return context

    def test_func(self):
        return True

class MedicineUpdate(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, UpdateView):
    model = Medicine
    fields = ['peopleid', 'doctorid', 'categorid', 'dateof', 'datestart', 'dateend', 'notes']
    template_name_suffix = '_update_form'
    widgets = {
        'dateof': DateWidget(attrs={'id': "id_dateof"}, bootstrap_version=3),
        'datestart': DateWidget(attrs={'id': "id_datestart"}, bootstrap_version=3),
        'dateend': DateWidget(attrs={'id': "id_dateend"}, bootstrap_version=3),
        'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10})
    }

    def test_func(self):
        return True

class MedicineDelete(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, DeleteView):
    model = Medicine
    def test_func(self):
        return True

########################################################################################################

########################################################################################################
# Operation
from .models import Operations


class OperationTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = Operations
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['peopleid', 'comments', 'id']
        sequence = ['dateof', 'doctorid', '...']

    def render_detail(self, record):
        rev = reverse('DjgLeoApp001:detailoperation', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Λεπτομέρειες</span></a>')

# @login_required
def OperationList(request, Patient):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = OperationTable(Operations.objects.all().filter(peopleid=Patient))
    global GlobPeopleidNum
    GlobPeopleidNum = Patient
    RequestConfig(request).configure(table)
    p = People.objects.get(pk=Patient)
    return render(request, 'people.html',
                  {'people': table, 'add_url_leo': 'DjgLeoApp001:createoperation', 'page_title': u'Επεμβάσεις',
                   'name': u'Επεμβάσεις για '+ p.name + ' ' + p.surname })

class OperationCreare(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, CreateView):
    model = Operations
    fields = ['peopleid', 'doctorid', 'categorid', 'dateof', 'notes', 'comments']
    template_name_suffix = '_create_form'
    widgets = {
        'dateof': DateWidget(attrs={'id': "id_dateof"}, bootstrap_version=3),
        'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
        'comments': forms.Textarea(attrs={'cols': 100, 'rows': 10})
    }
    def test_func(self):
        return True

class OperationDetailView(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, DetailView):
    model = Operations

    def get_context_data(self, **kwargs):
        context = super(OperationDetailView, self).get_context_data(**kwargs)
        return context

    def test_func(self):
        return True

class OperationUpdate(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, UpdateView):
    model = Operations
    fields = ['peopleid', 'doctorid', 'categorid', 'dateof', 'notes', 'comments']
    template_name_suffix = '_update_form'
    widgets = {
        'dateof': DateWidget(attrs={'id': "id_dateof"}, bootstrap_version=3),
        'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
        'comments': forms.Textarea(attrs={'cols': 100, 'rows': 10})
    }

    def test_func(self):
        return True

class OperationDelete(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, DeleteView):
    model = Operations
    def test_func(self):
        return True

########################################################################################################

########################################################################################################
# Examination
from .models import Examination0


class ExaminationTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = Examination0
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['peopleid', 'comments', 'id']
        sequence = ['dateofexam', 'doctorid',  '...']

    def render_detail(self, record):
        rev = reverse('DjgLeoApp001:detailexam', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Λεπτομέρειες</span></a>')

# @login_required
def ExaminationList(request, Patient):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = ExaminationTable(Examination0.objects.all().filter(peopleid=Patient))
    global GlobPeopleidNum
    GlobPeopleidNum = Patient
    RequestConfig(request).configure(table)
    p = People.objects.get(pk=Patient)
    return render(request, 'people.html',
                  {'people': table, 'add_url_leo': 'DjgLeoApp001:createexam', 'page_title': u'Επεμβάσεις',
                   'name': u'Εξετάσεις για '+ p.name + ' ' + p.surname })

class ExaminationCreare(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, CreateView):
    model = Examination0
    fields = ['peopleid', 'doctorid', 'categorid', 'dateofexam', 'notes', 'comments']
    template_name_suffix = '_create_form'
    widgets = {
        'dateofexam': DateWidget(attrs={'id': "id_dateof"}, bootstrap_version=3),
        'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
        'comments': forms.Textarea(attrs={'cols': 100, 'rows': 10})
    }

    global GlobPeopleidNum
    def get_initial(self):
        return  {'peopleid': GlobPeopleidNum}

    def test_func(self):
        return True

class ExaminationDetailView(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, DetailView):
    model = Examination0

    def get_context_data(self, **kwargs):
        context = super(ExaminationDetailView, self).get_context_data(**kwargs)
        return context

    def test_func(self):
        return True

class ExaminationUpdate(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, UpdateView):
    model = Examination0
    fields = ['peopleid', 'doctorid', 'categorid', 'dateofexam', 'notes', 'comments']
    template_name_suffix = '_update_form'
    widgets = {
        'dateofexam': DateWidget(attrs={'id': "id_dateof"}, bootstrap_version=3),
        'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
        'comments': forms.Textarea(attrs={'cols': 100, 'rows': 10})
    }

    def test_func(self):
        return True

class ExaminationDelete(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, DeleteView):
    model = Examination0

    def test_func(self):
        return True

########################################################################################################

########################################################################################################
#BioExaminationDet

from .models import BioExaminationDetail

class BioExaminationDetTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])
    update = tables.LinkColumn('item_update', args=[('pk')], orderable=False, empty_values=[''])
    delete = tables.LinkColumn('item_delete', args=[('pk')], orderable=False, empty_values=[''])
    mark   = tables.LinkColumn('item_mark', args=[('value')], orderable=False, empty_values=[''])
    class Meta:
        model = BioExaminationDetail
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}

    def render_detail(self, record):
        rev = reverse('DjgLeoApp001:detailexambiodet', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:green">Λεπ.</span></a>')
    def render_update(self, record):
        rev = reverse('DjgLeoApp001:updateexambiodet', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:blue">Μετ.</span></a>')
    def render_delete(self, record):
        rev = reverse('DjgLeoApp001:deleteexambiodet', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Δiα.</span></a>')
    def render_mark(self, record):
        if record.value > 0 :
            return mark_safe('<span style="color:green">+++</span>')
        else:
            return mark_safe('<span style="color:red">---</span>')




#@login_required
def BioExaminationDetList(request,exampk):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = BioExaminationDetTable(BioExaminationDetail.objects.all().filter(BioExaminationId=exampk))
    p = BioExamination.objects.get(id=exampk).peopleid
    return render(request, 'people.html', {'people': table, 'add_url_leo': 'DjgLeoApp001:createexambiodet',
                                           'page_title': u'aaa', 'name': u'Ανάληση Βιοχημικών για ' + p.name + ' ' + p.surname})


class BioExaminationDetCreare(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,CreateView):
    model = BioExaminationDetail
    fields = ['BioExaminationId','examnameid', 'value', 'notes']
    template_name_suffix = '_create_form'
    widgets = {
        'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10})
        }

    def test_func(self):
        return True

class BioExaminationDetDetailView(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,DetailView):
    model = BioExaminationDetail
    def get_context_data(self, **kwargs):
        context = super(BioExaminationDetDetailView, self).get_context_data(**kwargs)
        return context
    def test_func(self):
        return True

class BioExaminationDetUpdate(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,UpdateView):
    model = BioExaminationDetail
    fields = ['examnameid', 'value', 'notes']
    template_name_suffix = '_update_form'
#    rev = reverse('DjgLeoApp001:detailexambio', kwargs={'pk': str(1)})
#    rev = reverse('DjgLeoApp001:detailexambio', kwargs={'pk': str(1)})
#    success_url = rev
    widgets = {
        'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
        }
    def test_func(self):
        return True

class BioExaminationDetDelete(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,DeleteView):
    model = BioExaminationDetail
    def test_func(self):
        return True

########################################################################################################


from .models import BioExaminationDetail
from .models import Examname

class BioExaminationDetailList(ListView):
    model = BioExaminationDetail


def MassBioExaminationDetailUpdate(request, pk):
    BioExamTable = BioExamination.objects.get(pk=pk)
    for x in BioExamTable.examsschema.all():
        for y in Examname.objects.filter(groupexam_id=x.pk):
            a=BioExaminationDetail()
            a.BioExaminationId = BioExamTable
            a.examnameid = y
            a.value = 0
            try:
                a.save()
            except:
                print y.name
                a.clean()
                pass
    return BioExaminationList(request, BioExamTable.peopleid.pk)

