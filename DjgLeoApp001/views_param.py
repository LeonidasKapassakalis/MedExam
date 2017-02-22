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
from .models import MM

class MMForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = MM
        fields = ['name', 'sname', 'mmtype']

class MMTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = MM
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id']
        sequence = ['name', 'sname', '...']

    def render_detail(self, record):
        rev = reverse('DjgLeoApp001:updatemm', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Ενημέρωση</span></a>')

#@login_required
def MMList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = MMTable(MM.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Εξετάσεις',
                    'page_title': u'Μονάδες Μέτρησης',
                    'form_name': u'Μονάδες Μέτρησης',
                    'param_action1': reverse('DjgLeoApp001:createmm'),
                    'param_action1_name': 'Προσθήκη'})

class MMCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = MM
    form_class = MMForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class MMUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MM
    form_class = MMForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

########################################################################################################

########################################################################################################
from .models import MMType

class MMTypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = MMType
        fields = ['name', 'sname']

class MMTypeTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = MMType
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id']
        sequence = ['name', 'sname', '...']

    def render_detail(self, record):
        rev = reverse('DjgLeoApp001:updatemmtype', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Ενημέρωση</span></a>')

#@login_required
def MMTypeList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = MMTypeTable(MMType.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Εξετάσεις',
                    'page_title': u'Είδος Μονάδων Μέτρησης',
                    'form_name': u'Είδος Μονάδων Μέτρησης',
                    'param_action1': reverse('DjgLeoApp001:createmmtype'),
                    'param_action1_name': 'Προσθήκη'})

class MMTypeCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = MMType
    form_class = MMTypeForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class MMTypeUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MMType
    form_class = MMTypeForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

########################################################################################################

########################################################################################################
from .models import GroupExam

class GroupExamForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = GroupExam
        fields = ['name', 'sname']

class GroupExamTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = GroupExam
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id']
        sequence = ['name', 'sname', '...']

    def render_detail(self, record):
        rev = reverse('DjgLeoApp001:updategroupexam', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Ενημέρωση</span></a>')

#@login_required
def GroupExamList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = GroupExamTable(GroupExam.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Εξετάσεις',
                    'page_title': u'GroupExamList',
                    'form_name': u'GroupExamList',
                    'param_action1': reverse('DjgLeoApp001:creategroupexam'),
                    'param_action1_name': 'Προσθήκη'})

class GroupExamCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = GroupExam
    form_class = GroupExamForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class GroupExamUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = GroupExam
    form_class = GroupExamForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

########################################################################################################

########################################################################################################
from .models import MedicineCategory

class MedicineCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = MedicineCategory
        fields = ['name', 'sname']

class MedicineCategoryTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = MedicineCategory
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id']
        sequence = ['name', 'sname', '...']

    def render_detail(self, record):
        rev = reverse('DjgLeoApp001:updatemedicinecategory', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Ενημέρωση</span></a>')

#@login_required
def MedicineCategoryList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = MedicineCategoryTable(MedicineCategory.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Εξετάσεις',
                    'page_title': u'MedicineCategoryList',
                    'form_name': u'MedicineCategoryList',
                    'param_action1': reverse('DjgLeoApp001:createmedicinecategory'),
                    'param_action1_name': 'Προσθήκη'})

class MedicineCategoryCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = MedicineCategory
    form_class = MedicineCategoryForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class MedicineCategoryUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MedicineCategory
    form_class = MedicineCategoryForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

########################################################################################################

########################################################################################################
from .models import BioExaminationCategory

class BioExaminationCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = BioExaminationCategory
        fields = ['name', 'sname']

class BioExaminationCategoryTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = BioExaminationCategory
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id']
        sequence = ['name', 'sname', '...']

    def render_detail(self, record):
        rev = reverse('DjgLeoApp001:updatebioexaminationcategory', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Ενημέρωση</span></a>')

#@login_required
def BioExaminationCategoryList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = BioExaminationCategoryTable(BioExaminationCategory.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Εξετάσεις',
                    'page_title': u'BioExaminationCategoryList',
                    'form_name': u'BioExaminationCategoryList',
                    'param_action1': reverse('DjgLeoApp001:createbioexaminationcategory'),
                    'param_action1_name': 'Προσθήκη'})

class BioExaminationCategoryCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = BioExaminationCategory
    form_class = BioExaminationCategoryForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class BioExaminationCategoryUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BioExaminationCategory
    form_class = BioExaminationCategoryForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

########################################################################################################

########################################################################################################
from .models import OperationCategory

class OperationCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = OperationCategory
        fields = ['name', 'sname']

class OperationCategoryTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = OperationCategory
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id']
        sequence = ['name', 'sname', '...']

    def render_detail(self, record):
        rev = reverse('DjgLeoApp001:updateoperationcategory', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Ενημέρωση</span></a>')

#@login_required
def OperationCategoryList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = OperationCategoryTable(OperationCategory.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Εξετάσεις',
                    'page_title': u'OperationCategoryList',
                    'form_name': u'OperationCategoryList',
                    'param_action1': reverse('DjgLeoApp001:createoperationcategory'),
                    'param_action1_name': 'Προσθήκη'})

class OperationCategoryCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = OperationCategory
    form_class = OperationCategoryForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class OperationCategoryUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = OperationCategory
    form_class = OperationCategoryForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

########################################################################################################

########################################################################################################
from .models import DoctorSpeciality

class DoctorSpecialityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = DoctorSpeciality
        fields = ['name', 'sname']

class DoctorSpecialityTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = DoctorSpeciality
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id']
        sequence = ['name', 'sname', '...']

    def render_detail(self, record):
        rev = reverse('DjgLeoApp001:updatedoctorspeciality', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Ενημέρωση</span></a>')

#@login_required
def DoctorSpecialityList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = DoctorSpecialityTable(DoctorSpeciality.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Εξετάσεις',
                    'page_title': u'DoctorSpecialityList',
                    'form_name': u'DoctorSpecialityList',
                    'param_action1': reverse('DjgLeoApp001:createdoctorspeciality'),
                    'param_action1_name': 'Προσθήκη'})

class DoctorSpecialityCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = DoctorSpeciality
    form_class = DoctorSpecialityForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class DoctorSpecialityUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DoctorSpeciality
    form_class = DoctorSpecialityForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

########################################################################################################

########################################################################################################
from .models import ExaminationCategory

class ExaminationCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = ExaminationCategory
        fields = ['name', 'sname']

class ExaminationCategoryTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = ExaminationCategory
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id']
        sequence = ['name', 'sname', '...']

    def render_detail(self, record):
        rev = reverse('DjgLeoApp001:updateexaminationcategory', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Ενημέρωση</span></a>')

#@login_required
def ExaminationCategoryList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = ExaminationCategoryTable(ExaminationCategory.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Εξετάσεις',
                    'page_title': u'ExaminationCategoryList',
                    'form_name': u'ExaminationCategoryList',
                    'param_action1': reverse('DjgLeoApp001:createexaminationcategory'),
                    'param_action1_name': 'Προσθήκη'})

class ExaminationCategoryCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ExaminationCategory
    form_class = ExaminationCategoryForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class ExaminationCategoryUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ExaminationCategory
    form_class = ExaminationCategoryForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

########################################################################################################

########################################################################################################
from .models import Examschema

class ExamSchemaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = Examschema
        fields = ['name', 'sequence', 'notes']

class ExamSchemaTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = Examschema
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id']
        sequence = ['name', '...']

    def render_detail(self, record):
        rev = reverse('DjgLeoApp001:updateexamschema', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Ενημέρωση</span></a>')

#@login_required
def ExamSchemaList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = ExamSchemaTable(Examschema.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Εξετάσεις',
                    'page_title': u'ExamSchemaList',
                    'form_name': u'ExamSchemaList',
                    'param_action1': reverse('DjgLeoApp001:createexamschema'),
                    'param_action1_name': 'Προσθήκη'})

class ExamSchemaCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Examschema
    form_class = ExamSchemaForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class ExamSchemaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Examschema
    form_class = ExamSchemaForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

########################################################################################################

########################################################################################################
from .models import Country

class CountryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = Country
        fields = ['name', 'abbr' , 'telephoneext']


class CountryTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = Country
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id']
        sequence = ['name', 'abbr', '...']

    def render_detail(self, record):
        rev = reverse('DjgLeoApp001:updatecountry', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Ενημέρωση</span></a>')

#@login_required
def CountryList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = CountryTable(Country.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Εξετάσεις',
                    'page_title': u'CountryList',
                    'form_name': u'CountryList',
                    'param_action1': reverse('DjgLeoApp001:createcountry'),
                    'param_action1_name': 'Προσθήκη'})

class CountryCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Country
    form_class = CountryForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class CountryUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Country
    form_class = CountryForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

########################################################################################################



