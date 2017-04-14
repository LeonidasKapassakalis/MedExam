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
#BioExaminationDet
#['BioExaminationId','examnameid','value','notes']


from .models import BioExaminationDetail
from .models import BioExamination
from .models import Examname

class BioExaminationDetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = BioExaminationDetail
        fields = ['BioExaminationId', 'examnameid', 'value', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
            }


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
        exclude = ['BioExaminationId',]#'id']
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

from time import strftime
import locale

#@login_required
def BioExaminationDetList(request,exampk):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    table = BioExaminationDetTable(BioExaminationDetail.objects.all().filter(BioExaminationId=exampk))
    p = BioExamination.objects.get(id=exampk).peopleid
    e = BioExamination.objects.get(id=exampk)

    RequestConfig(request, paginate={'per_page': 20}).configure(table)
    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table,
                   'page_title': u'Ανάληση Εργαστηριακών για ' + p.name + ' ' + p.surname + ' ' + e.dateofexam.strftime('%d/%m/%Y'),
                   'form_name':  u'Ανάληση Εργαστηριακών για ' + p.name + ' ' + p.surname + ' ' + e.dateofexam.strftime('%d/%m/%Y'),
                    'param_action1': reverse('DjgLeoApp001:createexambiodet'),
                    'param_action1_name': 'Προσθήκη'})


class BioExaminationDetDetailView(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,DetailView):
    model = BioExaminationDetail
    def get_context_data(self, **kwargs):
        context = super(BioExaminationDetDetailView, self).get_context_data(**kwargs)
        context['page_title'] = u'Αναλυτικά Στοιχεία Εργαστηριακών ' +  context['bioexaminationdetail'].BioExaminationId.__str__()
        context['form_name'] = u'Αναλυτικά Στοιχεία Εργαστηριακών '
        context['param_action1'] = reverse('DjgLeoApp001:updateexambiodet', kwargs={'pk':context['bioexaminationdetail'].pk})
        context['param_action1_name'] = u'Μεταβολή'
        context['param_action2'] = reverse('DjgLeoApp001:deleteexambiodet', kwargs={'pk':context['bioexaminationdetail'].pk})
        context['param_action2_name'] = u'Διαγραφή'
        return context
    def test_func(self):
        return True


class BioExaminationDetCreare(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = BioExaminationDetail
    form_class = BioExaminationDetForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True


class BioExaminationDetUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = BioExaminationDetail
    form_class = BioExaminationDetForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True


class BioExaminationDetDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = BioExaminationDetail

    def test_func(self):
        return True

