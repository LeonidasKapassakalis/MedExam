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
# Examname
#['name','sname','minvalue','maxvalue','result_type','comments', 'bioexaminationcategory','groupexam','mm']
from .models import Examname

class ExamnameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = Examname
        fields = ['name', 'sname','result_type', 'comments', 'bioexaminationcategory', 'groupexam', 'minvalue', 'maxvalue', 'mm']

class ExamnameTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = Examname
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id']
        sequence = ['name', 'detail', 'sname', 'result_type', 'bioexaminationcategory', 'groupexam', 'mm' ,'minvalue','maxvalue']

    def render_detail(self, record):
        rev = reverse('DjgLeoApp001:detailexamname', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:blue">Λεπ.</span></a>')

#@login_required
def ExamnameList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = ExamnameTable(Examname.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Εξετάσεις',
                    'page_title': u'Εξετάσεις',
                    'form_name': u'Εξετάσεις',
                    'param_action1': reverse('DjgLeoApp001:createexamname'),
                    'param_action1_name': 'Προσθήκη'})

class ExamnameDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Examname

    def get_context_data(self, **kwargs):
        context = super(ExamnameDetailView, self).get_context_data(**kwargs)
        return context

    def test_func(self):
        return True

class ExamnameCreare(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Examname
    form_class = ExamnameForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class ExamnameUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Examname
    form_class = ExamnameForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class ExamnameDelete(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, DeleteView):
    model = Examname
    def test_func(self):
        return True

########################################################################################################