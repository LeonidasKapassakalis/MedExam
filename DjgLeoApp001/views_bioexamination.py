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

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from datetimewidget.widgets import DateTimeWidget, DateWidget , TimeWidget

from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError

from .views import ModelFormWidgetMixin

########################################################################################################
#BioExamination
#['peopleid','doctorid','examsschema','categorid','dateofexam','notes','comments']


from .models import BioExamination
from .models import People

class BioExaminationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = BioExamination
        fields = ['peopleid', 'doctorid', 'examsschema', 'categorid', 'category' ,'dateofexam', 'notes', 'comments']
        widgets = {
             'dateofexam': DateWidget(attrs={'id': "id_dateof"}, bootstrap_version=3),
             'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
             'comments': forms.Textarea(attrs={'cols': 100, 'rows': 10})
             }


class BioExaminationTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')],orderable=False,empty_values=[''])
    detaildet = tables.LinkColumn('item_detaildet', args=[('pk')], orderable=False, empty_values=[''])
    class Meta:
        model = BioExamination
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['peopleid','id']
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
    request.session['patient_id'] = Patient
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    p = People.objects.get(pk=Patient)
    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table,
                    'page_title': u'Βιοχημικές για ' + p.name + ' ' + p.surname,
                    'form_name': u'Βιοχημικές για ' + p.name + ' ' + p.surname,
                    'param_action1': reverse('DjgLeoApp001:createexambio'),
                    'param_action1_name': 'Προσθήκη'})


class BioExaminationDetailView(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,DetailView):
    model = BioExamination
    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['page_title'] = u'Στοιχεία Βιοχημικών ' +  context['object'].peopleid.surname + ' ' \
                                + context['object'].peopleid.name + ' ' + str(context['object'].dateofexam)
        context['form_name'] = u'Στοιχεία Βιοχημικών '
        return context
    def test_func(self):
        return True

class BioExaminationCreare(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = BioExamination
    form_class = BioExaminationForm
    template_name = 'General/General_cu_form.html'

    def get_initial(self):
        return  {'peopleid': self.request.session['patient_id']}

    def test_func(self):
        return True


class BioExaminationUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = BioExamination
    form_class = BioExaminationForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class BioExaminationDelete(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,DeleteView):
    model = BioExamination
    def test_func(self):
        return True


########################################################################################################
#TODO

from .models import BioExaminationDetail
from .models import Examname
from .models import GroupExam

class BioExaminationDetailList(ListView):
    model = BioExaminationDetail

def MassBioExaminationDetailUpdate(request, pk):
    BioExamTable = BioExamination.objects.get(pk=pk)
    for x in BioExamTable.category.all():
        for y in Examname.objects.filter(bioexaminationcategory=x.pk):
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

    # def MassBioExaminationDetailUpdate(request, pk):
    #     BioExamTable = BioExamination.objects.get(pk=pk)
    #     for x in BioExamTable.examsschema.all():
    #         for y in Examname.objects.filter(groupexam=x.pk):
    #             a = BioExaminationDetail()
    #             a.BioExaminationId = BioExamTable
    #             a.examnameid = y
    #             a.value = 0
    #             try:
    #                 a.save()
    #             except:
    #                 print y.name
    #                 a.clean()
    #                 pass
    #     return BioExaminationList(request, BioExamTable.peopleid.pk)



        ########################################################################################################