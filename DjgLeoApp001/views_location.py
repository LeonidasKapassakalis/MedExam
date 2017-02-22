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

########################################################################################################
#'name','address','phone','mail','tk','text','hospital','medicalcenter','eopyy','contact','countryid','peoples'

# Locations
from .models import Locations

class LocationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = Locations
        fields = ['name','address','phone','mail','tk','text','hospital','medicalcenter','eopyy','contact','countryid','peoples']


class LocationsTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = Locations
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        fields = ['name', 'tk', 'phone', 'mail', 'hospital', 'medicalcenter', 'eopyy','countryid']
        sequence = ['name', 'tk', '...']

    def render_detail(self, record):
        rev = reverse('DjgLeoApp001:detaillocation', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Λεπτομέρειες</span></a>')



def LocationList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = LocationsTable(Locations.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Τοποθεσίες',
                    'page_title': u'Τοποθεσίες',
                    'form_name': u'Τοποθεσίες',
                    'param_action1': reverse('DjgLeoApp001:createlocation'),
                    'param_action1_name': 'Προσθήκη'})


class LocationCreare(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model = Locations
    form_class = LocationForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True


class LocationUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Locations
    form_class = LocationForm
    template_name = 'General/General_cu_form.html'

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super(self.__class__, self).get_form_kwargs(*args, **kwargs)
        form_kwargs['request'] = self.request
        return form_kwargs

    def test_func(self):
        return True


class LocationDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Locations

    def test_func(self):
        return True


class LocationDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Locations

    def test_func(self):
        return True

########################################################################################################
