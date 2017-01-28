# -*- encoding: utf-8 -*-

from django import template
from django import get_version

register = template.Library()

if get_version().split('.') < ['1', '5']:
    from django.template.defaulttags import url
    from django.core.urlresolvers import reverse

from django.contrib.admin import AdminSite
class MyAdminSite(AdminSite):
        pass

mysite = MyAdminSite()

def defadm(request):
    return {'user': request.user, 'site_header': mysite.site_header, 'has_permission': mysite.has_permission(request),
                                            'site_url': mysite.site_url , 'title' : 'Λεωνίδας Exam App' }
