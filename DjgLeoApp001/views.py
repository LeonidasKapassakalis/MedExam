# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response

import datetime

from models import People

from models import Person

def MainMenu(request):
    return render(request, 'baseMenu.html')

from django.shortcuts import render
def people0(request):
    return render(request, 'people.html', {'people': People.objects.all(), 'add_url_leo': 'locationcreate'})

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

from django.views.generic import ListView

class PublisherList(ListView):
    model = People

class PublisherList0(ListView):
    model = People

from django.views.generic import DetailView

class PublisherDetailView(DetailView):
    model = People

    def get_context_data(self, **kwargs):
        context = super(PublisherDetailView, self).get_context_data(**kwargs)
#        context['now'] = timezone.now()
        return context

from django.views.generic.edit import CreateView, UpdateView, DeleteView

class PublisherCreare(CreateView):
    model = People
    fields = ['id','name','surname','mail','dateofbirth','nationality',
        'countryid','phone','mail','mobile','ispatient','isdoctor','canlogin',
        'accessonlyhisfile','notes']
    template_name_suffix = '_create_form'
    success_url = '/publishers/'

class PublisherUpdate(UpdateView):
    model = People
    fields = ['name','surname','notes','mail']
    fields = ['id','name','surname','mail','dateofbirth','nationality',
        'countryid','phone','mail','mobile','ispatient','isdoctor','canlogin',
        'accessonlyhisfile','notes']
    template_name_suffix = '_update_formt'
    success_url = '/publishers/'
    success_url = '/tables10/'    

class PublisherDelete(DeleteView):
    model = People
    fields = ['name','surname','notes','mail']
    success_url = '/publishers/'

#Examination0

from models import Examination0

def ExaminationsListPer000(request):
    queryset  = Examination0.objects.all()
    table = Examination0(queryset)
    RequestConfig(request).configure(table)
    return render(request, 'examination0_list.html', {'object_list': table})

class ExaminationsList(ListView):
    model = Examination0

class ExaminationsList0(ListView):
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



from django.shortcuts import get_object_or_404

class ExaminationsListPer(ListView):
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
        context['name'] = self.name
        return context

class ExaminationsListPerDoctor(ListView):
    model = Examination0
    template_name = 'examination_list_per_person.html'
    def get_queryset(self):
        self.id = get_object_or_404(People,id=self.args[0])
        self.name = get_object_or_404(People,id=self.args[0])
        return Examination0.objects.filter(doctorid=self.id)

    def get_context_data(self, **kwargs):
        context = super(ExaminationsListPerDoctor, self).get_context_data(**kwargs)
        context['publisher'] = self.id
        context['name'] = self.name
        return context


class ExaminationsListPerDoctorPatient(ListView):
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
        context['name'] = self.pname.name + ' ' + self.pname.surname + u' απο ' + self.dname.name + ' ' + self.dname.surname
        return context




from models import ExaminationCategory    

class ExaminationsListPerCategory(ListView):
    model = Examination0
    def get_queryset(self):
        self.id = get_object_or_404(ExaminationCategory,id=self.args[0])
        return Examination0.objects.filter(categorid=self.id)

from django.views.generic.detail import DetailView

class ExaminationDetail(DetailView):
    model = Examination0

from django.forms.models import modelform_factory
from django import forms
class ModelFormWidgetMixin(object):
    def get_form_class(self):
        return modelform_factory(self.model, fields=self.fields, widgets=self.widgets)    

from django.contrib.admin import widgets

class ExaminationCreare(ModelFormWidgetMixin,CreateView):
    model = Examination0
    fields = ['peopleid','doctorid','categorid','dateofexam','notes','comments']
    template_name_suffix = '_create_form'
    success_url = '/examinations/'
    widgets = {
        'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
        'comments': forms.Textarea(attrs={'cols': 100, 'rows': 5}),
        'dateofexam': widgets.AdminDateWidget,
        }

class ExaminationUpdate(ModelFormWidgetMixin,UpdateView):
    model = Examination0
    fields = ['peopleid','doctorid','categorid','dateofexam','notes','comments']
    readonly_fields = ('peopleid','categorid','dateofexam')
    template_name_suffix = '_update_form'
    success_url = '/examinations/'
    widgets = {
        'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10, 'readonly' : True}),
        'comments': forms.Textarea(attrs={'cols': 100, 'rows': 5, 'readonly' : True}),
        'dateofexam': widgets.AdminDateWidget(attrs={'cols': 100, 'rows': 10, 'readonly' : True}),
        }
   

class ExaminationDelete(DeleteView):
    model = Examination0
    fields = ['peopleid','doctorid','categorid','dateofexam','notes','comments']
    success_url = '/examinations/'

    


import django_tables2 as tables
from django.shortcuts import render
from django_tables2 import RequestConfig
from django.utils.html import mark_safe
from  django.urls import reverse

class PeopleTable(tables.Table):
    edit = tables.LinkColumn('item_edit', args=[('pk')],orderable=False,empty_values=[''])
    exam = tables.LinkColumn('item_exam', args=[('pk')],orderable=False,empty_values=[''])    
    delete = tables.LinkColumn('item_delete', args=[('pk')],orderable=False,empty_values=[''])    
    class Meta:
        model = People
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['nationality','id','idoncontry','ispatient','isdoctor','canlogin','accessonlyhisfile','photo','notes']
#        fields
        sequence = ['name','surname','countryid','phone','...']

    def render_edit(self, record):
        return mark_safe('<a href=/publisherupd/' + str(record.pk) + '/><span style="color:blue">Edit</span></a>')

    def render_delete(self, record):
        return mark_safe('<a href=/publisherdel/' + str(record.pk) + '/><span style="color:red">Delete</span></a>')

    def render_exam(self, record):
        return mark_safe('<a href=/examinationsper/' + str(record.pk) + '/><span style="color:green">Exams◙</span></a></a>')


def person_list(request):
    table = PeopleTable(People.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'people.html', {'people': table, 'add_url_leo': 'publishercreate', 'page_title': u'Άνθρωποι'})


def people10(request):
    queryset  = People.objects.all()
    table = PeopleTable(queryset)
    RequestConfig(request).configure(table)
    return render(request, 'people.html', {'people': table})



class ExaminationTable(tables.Table):
    edit = tables.LinkColumn('item_edit', args=[('pk')],orderable=False,empty_values=[''])
    delete = tables.LinkColumn('item_delete', args=[('pk')],orderable=False,empty_values=[''])    
    class Meta:
        model = Examination0
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
#        exclude = ['nationality','idoncontry','ispatient','isdoctor','canlogin','accessonlyhisfile','photo','notes'] 
#        fields
#        sequence = ['name','surname','countryid','phone','...']

    def render_edit(self, record):
        return mark_safe('<a href=/examinationupd/' + str(record.pk) + '/><span style="color:blue">Edit</span></a>')

    def render_delete(self, record):
        return mark_safe('<a href=/examinationdel/' + str(record.pk) + '/><span style="color:red">Delete</span></a>')

    def render_detail(self, record):
        return mark_safe('<a href=/examinationsper/' + str(record.pk) + '/><span style="color:green">Exams◙</span></a></a>')


def examination_list(request):
    table = ExaminationTable(Examination0.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'people.html', {'people': table, 'page_title' : 'Malakies', 'add_url_leo': 'examinationcreate' })


#Crispy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, MultiField

class ExampleForm0(CreateView):
    model = People
    fields = ['name', 'surname', 'notes', 'mail', 'dateofbirth', 'nationality', 'countryid',
              'idoncontry', 'phone', 'fax', 'mail', 'ispatient', 'isdoctor', 'canlogin',
              'accessonlyhisfile', 'notes']
    success_url = '/examinations'

    def __init__(self, *args, **kwargs):
        super(ExampleForm0, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm0'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'get'
        self.helper.form_action = '/examinations'


#        self.helper.form_class = 'form-inline'
#        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
#        self.helper.field_template = 'bootstrap3/layout/multifield.html'

#        self.helper.form_class = 'form-horizontal'
#        self.helper.label_class = 'col-lg-2'
#        self.helper.field_class = 'col-lg-8'

        self.helper.layout = Layout(
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
