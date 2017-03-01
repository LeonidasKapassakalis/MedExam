# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django import forms

import django_tables2 as tables
from django.shortcuts import render
from django_tables2 import RequestConfig
from django.utils.html import mark_safe
from  django.urls import reverse
from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import permission_required

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from datetimewidget.widgets import DateTimeWidget, DateWidget , TimeWidget

from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError

from .views import ModelFormWidgetMixin
from .views import get_spec_user

########################################################################################################

#['name','surname','dateofbirth','nationality','countryid','phone','fax','mobile','mail'\
#    ,'ispatient','isdoctor','canlogin','accessonlyhisfile','notes','photo']



from .models import People

class PeopleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__ , self).__init__(*args, **kwargs)

    class Meta:
        model = People
        fields = ['name', 'surname', 'dateofbirth', 'nationality', 'countryid', 'phone', 'fax', 'mobile', 'mail' \
                  ,'ispatient','isdoctor','canlogin','accessonlyhisfile','notes']
        widgets = {
            'dateofbirth': DateWidget(attrs={'id': "id_dateof"}, bootstrap_version=3),
            'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10})
            }


class PeopleDetailView(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,DetailView):
    model = People

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['page_title'] = u'Στοιχεία ' +  context['object'].surname + ' '  +  context['object'].name
        context['form_name'] = u'Αναλυτικά Στοιχεία Ατόμου '
        return context

    def test_func(self):
        return True


class PeopleCreare(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = People
    form_class = PeopleForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True


class PeopleUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = People
    form_class = PeopleForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True


class PeopleDelete(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,DeleteView):
    model = People
    fields = ['name','surname','notes','mail']
    def test_func(self):
        return True

@permission_required('People.view', login_url='/login/')
def patient_list(request):
#     u = User.objects.get(username=request.user)
#     if request.user.is_superuser or request.user.is_staff:
#         print 'Super'
#
#     us = SpecialUsers.objects.get(user=request.user)
#
#     # qlist = []
#     # q_object = Q()
#     # for x in us.peoples.all():
#     #     a=('id',str(x.id))
#     #     qlist.append(a)
#
#     q_object = Q()
# #    print q_object
#     bb=[]
#     for x in us.peoples.all():
#         aa=x.id
#         bb.append(x.id)
#         q_object.add(Q(id=aa),Q.OR)
#     global GlobPeopleid
#     GlobPeopleid = bb[:]
#        print q_object
# #    qlist.append(('ispatient','1'))
#     q_list = [Q(x) for x in qlist]
#     print  q_list
#     print q_object
#     print reduce(operator.or_, q_list)

    userparam=get_spec_user(request)

    # if userparam[0]:
    #     table = PatientListTable(models.People.objects.all().filter(ispatient=True))
    # else:
    #     table = PatientListTable(models.People.objects.all().filter(userparam[7]))

    table = PatientListTable(People.objects.all().filter(userparam[7]))

#    table = PatientListTable(models.People.objects.all().filter(ispatient=1).filter(reduce(operator.or_,q_list)))
#    table = PatientListTable(models.People.objects.all().filter(ispatient=1))

    RequestConfig(request, paginate={'per_page': 25}).configure(table)
    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table,
                   'page_title': u'Ασθενείς',
                   'form_name': u'Ασθενείς',
                   'param_action1': reverse('DjgLeoApp001:create'),
                   'param_action1_name': 'Προσθήκη'})


class PeopleTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', verbose_name=('Delete'))
#    detail = tables.LinkColumn('item_detail', args=[('pk')],orderable=False,empty_values=[''])
#    detail1 = tables.LinkColumn('item_detail1', args=[('pk')], orderable=False, empty_values=[''])
#    amend = tables.CheckBoxColumn(verbose_name=('Amend'), accessor='pk')
    class Meta:
        model = People
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['nationality','id','idoncontry','ispatient','isdoctor','canlogin','accessonlyhisfile','photo','notes']
        sequence = ['selection','name','surname','countryid','phone','...']

    def render_detail(self, record):
        return mark_safe('<a href=/DjgLeoApp001/detail/' + str(record.pk) + '/><span style="color:green">Λεπτομέριες</span></a></a>')


    def render_detail1(self, record):
        aaa='<input type="checkbox" name=' + str(record.pk) + ' value=' + str(record.pk) +' > '
        return mark_safe(aaa)


@permission_required('People.view', login_url='/login/')
def person_list(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = PeopleTable(People.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'General/Generic_Table_view_Selection.html',
                  {'objects': table,
                   'page_title': u'Άτομα',
                   'form_name': u'Άτομα',
                   'param_action1': reverse('DjgLeoApp001:create'),
                   'param_action1_name': 'Προσθήκη'})


class DoctorListTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')],orderable=False,empty_values=[''])
#    exams  = tables.LinkColumn('item_exams', args=[('pk')],orderable=False,empty_values=[''])
    class Meta:
        model = People
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['dateofbirth', 'nationality', 'countryid', 'ispatient', 'isdoctor', 'canlogin', 'accessonlyhisfile', 'notes' ,'id', 'photo']
        sequence = ['name','surname','...']

    def render_exams(self, record):
        return mark_safe('<a href=/DjgLeoApp001/examinationsListPerDoctor/'+str(record.pk)+'/><span style="color:blue">Εξετάσεις</span></a>')

    def render_detail(self,record):
        return mark_safe('<a href=/DjgLeoApp001/detail/'+str(record.pk)+'/><span style="color:green">Λεπτομέριες</span></a></a>')


@permission_required('People.view', login_url='/login/')
def doctor_list(request):
    table = DoctorListTable(People.objects.all().filter(isdoctor=1))
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table,
                   'page_title': u'Γιατροί',
                   'form_name': u'Γιατροί' ,
                   'param_action1': reverse('DjgLeoApp001:create'),
                   'param_action1_name': 'Προσθήκη'})


#Patient Table
class PatientListTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')],orderable=False,empty_values=[''])
    exam   = tables.LinkColumn('item_exam', args=[('pk')],orderable=False,empty_values=[''])
    exambio  = tables.LinkColumn('item_exambio', args=[('pk')],orderable=False,empty_values=[''])
    medicine  = tables.LinkColumn('item_medicine', args=[('pk')],orderable=False,empty_values=[''])
    operation  = tables.LinkColumn('item_operation', args=[('pk')],orderable=False,empty_values=[''])
    class Meta:
        model = People
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
