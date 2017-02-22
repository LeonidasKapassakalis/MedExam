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


from DjgLeoApp001.models import SpecialUsers
from django.contrib.auth.models import AnonymousUser

def defadm(request):
    # return {'user': request.user, 'site_header': mysite.site_header, 'has_permission': mysite.has_permission(request),
    #         'site_url': mysite.site_url, 'title': 'Λεωνίδας Exam App'}

    if request.user.is_anonymous():
        return {'user': request.user , 'site_header': mysite.site_header,
                'has_permission': mysite.has_permission(request),
                'site_url': mysite.site_url, 'title': 'Λεωνίδας Exam App'}
    else:
        u = SpecialUsers.objects.get(user=request.user)
        if u:
            pl=[x.id for x in   u.peoples.all()]
            dl = [x.id for x in u.doctors.all()]
            return {'user': request.user, 'site_header': mysite.site_header, 'has_permission': mysite.has_permission(request),
                   'site_url': mysite.site_url , 'title' : 'Λεωνίδας Exam App','people' : u.peopleid ,'altpeople': u.altpeopleid,
                    'peoples': pl, 'doctors': dl}
        else:
            return {'user': request.user, 'site_header': mysite.site_header, 'has_permission': mysite.has_permission(request),
                    'site_url': mysite.site_url , 'title' : 'Λεωνίδας Exam App'}
