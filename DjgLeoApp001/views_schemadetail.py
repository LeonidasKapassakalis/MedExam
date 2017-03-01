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
import django_filters

########################################################################################################
# ExamSchemaDetail
#['ExamSchema','ExamName']


from .models import ExamSchemaDetail
from .models import Examschema
from .models import Examname


class SchemaDetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = ExamSchemaDetail
        fields = ['ExamSchema', 'ExamName']


class ExamSchemaDetailFilter(django_filters.FilterSet):
    class Meta:
        model = ExamSchemaDetail
        exclude = ('BioExaminationId','notes')
        fields = {
            'ExamSchema': ['exact'] ,
            'ExamName': ['exact' ]
        }


class SchemaDetailTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = ExamSchemaDetail
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id', ]
        sequence = ['ExamSchema', 'ExamName']

    def render_detail(self, record):
        rev = reverse('DjgLeoApp001:updateschemadetail', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Μεταβολή</span></a>')

# @login_required
@permission_required('ExamSchemaDetail.view')
def SchemaDetailList(request):
#    if not request.user.is_authenticated:
#        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    data = ExamSchemaDetail.objects.all()
    filter = ExamSchemaDetailFilter(request.GET, queryset=data)
    table = SchemaDetailTable(filter.qs)

    RequestConfig(request, paginate={'per_page': 25}).configure(table)


    return render(request, 'General/Generic_Table_view_filter_panel.html',
                  {'objects': table,
                    'filter': filter,
                    'page_title': u'Αναλυτκό Σχήμα Εξετάσεων',
                    'form_name': u'Αναλυτκό Σχήμα Εξετάσεων',
                    'param_action1': reverse('DjgLeoApp001:createschemadetail'),
                    'param_action1_name': 'Προσθήκη'})


class SchemaDetailDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ExamSchemaDetail

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        return context

    def test_func(self):
        return True

class SchemaDetailCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ExamSchemaDetail
    form_class = SchemaDetailForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class SchemaDetailUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ExamSchemaDetail
    form_class = SchemaDetailForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class SchemaDetailDelete(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, DeleteView):
    model = ExamSchemaDetail
    def test_func(self):
        return True

########################################################################################################