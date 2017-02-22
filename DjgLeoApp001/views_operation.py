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
# Operation
#['peopleid','doctorid','categorid','dateof','notes','comments']

from .models import Operations
from .models import People

class OperationsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = Operations
        fields = ['peopleid', 'doctorid', 'categorid', 'dateof', 'notes', 'comments']
        widgets = {
            'dateof': DateWidget(attrs={'id': "id_dateof"}, bootstrap_version=3),
            'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
            'comments': forms.Textarea(attrs={'cols': 100, 'rows': 10})
            }


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
    request.session['patient_id'] = Patient

    RequestConfig(request, paginate={'per_page': 25}).configure(table)
    p = People.objects.get(pk=Patient)
    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Επεμβάσεις',
                    'page_title': u'Επεμβάσεις για ' + p.name + ' ' + p.surname,
                    'form_name': u'Επεμβάσεις για ' + p.name + ' ' + p.surname,
                    'param_action1': reverse('DjgLeoApp001:createoperation'),
                    'param_action1_name': 'Προσθήκη'})


class OperationDetailView(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, DetailView):
    model = Operations

    def get_context_data(self, **kwargs):
        context = super(OperationDetailView, self).get_context_data(**kwargs)
        return context

    def test_func(self):
        return True

class OperationCreare(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, CreateView):
    model = Operations
    form_class = OperationsForm
    template_name = 'DjgLeoApp001/../DjgLeo001/templates/General/General_cu_form.html'

    def test_func(self):
        return True

class OperationUpdate(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, UpdateView):
    model = Operations
    form_class = OperationsForm
    template_name = 'DjgLeoApp001/../DjgLeo001/templates/General/General_cu_form.html'

    def test_func(self):
        return True

class OperationDelete(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, DeleteView):
    model = Operations
    def test_func(self):
        return True

########################################################################################################
