# -*- coding: utf-8 -*-
# Create your views here.

# from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import Http404
# from django.shortcuts import render
# from django.template.loader import get_template
# from django.template import Context
# from django.shortcuts import render_to_response
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import redirect
# from django.forms.models import modelform_factory
# from django.shortcuts import get_object_or_404
# from django import forms
#
# import django_tables2 as tables
# from django.shortcuts import render
# from django_tables2 import RequestConfig
# from django.utils.html import mark_safe
# from  django.urls import reverse
#
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.mixins import UserPassesTestMixin
#
# from django.views.generic import ListView, DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
#
# from datetimewidget.widgets import DateTimeWidget, DateWidget , TimeWidget
#
# from django.http import HttpResponseRedirect
#
# from django.contrib.admin import widgets
# from django.contrib.admin.widgets import AdminDateWidget
#
# from django.core.exceptions import ValidationError


#Use with Create Update etc to specify widgets
class ModelFormWidgetMixin(object):
    def get_form_class(self):
        return modelform_factory(self.model, fields=self.fields, widgets=self.widgets)


# import datetime
# from models import People

from django.contrib.admin import AdminSite
class MyAdminSite(AdminSite):
        pass

mysite = MyAdminSite()


def MainMenu(request):
    return render(request, 'NewMenuBootStrap.html')

def NewMenu(request):
    return render(request, 'NewMenu.html')

def NewMenu1(request):
    return render(request, 'NewMenuBootStrap.html')


# #DataTables
# from django.views.generic import View, TemplateView
# from django.conf import settings
# from django.core.urlresolvers import reverse
# from django.template.defaultfilters import timesince
#
# import datatableview
# from datatableview import Datatable, ValuesDatatable, columns, SkipRecord
# from datatableview.views import DatatableView, MultipleDatatableView, XEditableDatatableView
# from datatableview.views.legacy import LegacyDatatableView
# from datatableview import helpers
# import models
# from .models import SpecialUsers
# from django.contrib.auth.models import User
# import operator

# leo    examination_list

from django.db.models import Q

def get_spec_user(request):
    us = SpecialUsers.objects.get(user=request.user)
    p_object = Q()
    pp=[]
    for x in us.peoples.all():
        aa=x.id
        pp.append(x.id)
        p_object.add(Q(id=aa),Q.OR)

    d_object = Q()
    dd = []
    for x in us.peoples.all():
        aa=x.id
        dd.append(x.id)
        d_object.add(Q(id=aa), Q.OR)

    p1 = People.objects.get(pk=us.peopleid_id)
    p2 = People.objects.get(pk=us.altpeopleid_id)

    return (request.user.is_superuser,p1.isdoctor,p2.isdoctor,us.peopleid_id, us.altpeopleid_id,pp,dd, p_object, d_object)


from views_location import *
from views_examination import *
from views_bioexamination import *
from views_bioexaminationdetail import *
from views_medicine import *
from views_operation import *
from views_people import *
from views_examname import *
from views_for_clean import *
from views_admin import *
from views_param import *



def someurl(request):
    if request.method == 'POST':
        pks1 = request.POST.getlist("selection")
        return render(request, 'General/General_Mass_Delete.html', {'ForDelete': pks1})
    if request.method == 'GET':
        return render(request, 'General/General_Mass_Delete_Final.html')


###############################################################################
#Signals

def my_callback(sender, **kwargs):
    print("Login !")

def my_callback0(sender, **kwargs):
    print("Request finished!+++++")

def my_callback1(sender, **kwargs):
    print("Request Started!+++++")

from django.core.signals import request_finished , request_started

request_finished.connect(my_callback0)
request_started.connect(my_callback1)

from django.contrib.auth import user_logged_in

user_logged_in.connect(my_callback)

###############################################################################
