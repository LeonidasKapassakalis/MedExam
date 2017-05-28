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

########################################################################################################
# Medicine
#['peopleid','doctorid','categorid','dateof','datestart','dateend','notes']

from .models import Medicine
from .models import People


class MedicineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = Medicine
        fields = ['peopleid', 'doctorid', 'categorid', 'dateof', 'datestart', 'dateend', 'docfile', 'notes']
        widgets = {
            'dateof': DateWidget(attrs={'id': "id_dateof"}, bootstrap_version=3),
            'datestart': DateWidget(attrs={'id': "id_dateof"}, bootstrap_version=3),
            'dateend': DateWidget(attrs={'id': "id_dateof"}, bootstrap_version=3),
            'notes': forms.Textarea(attrs={'cols': 100, 'rows': 10})
            }



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
@permission_required('Medicine.view')
def MedicineList(request, Patient):
#    if not request.user.is_authenticated:
#        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = MedicineTable(Medicine.objects.all().filter(peopleid=Patient))
    request.session['patient_id'] = Patient
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    p = People.objects.get(pk=Patient)
    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Φάρμακα',
                    'page_title': u'Φάρμακα για ' + p.name + ' ' + p.surname,
                    'form_name': u'Φάρμακα για ' + p.name + ' ' + p.surname,
                    'param_action1': reverse('DjgLeoApp001:createmedicine'),
                    'param_action1_name': 'Προσθήκη'})

class MedicineDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Medicine

    def get_context_data(self, **kwargs):
        context = super(MedicineDetailView, self).get_context_data(**kwargs)
        return context

    def test_func(self):
        return True

class MedicineCreare(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'General/General_cu_form.html'

    def get_initial(self):
        return  {'peopleid': self.request.session['patient_id']}

    def test_func(self):
        return True

class MedicineUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class MedicineDelete(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, DeleteView):
    model = Medicine
    def test_func(self):
        return True

########################################################################################################