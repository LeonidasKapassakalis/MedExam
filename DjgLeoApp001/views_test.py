# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.db.models import Q
from django.shortcuts import render
from django_tables2 import RequestConfig
from django.utils.html import mark_safe
from  django.urls import reverse
from django.conf import settings

import itertools
import django_filters
import django_tables2 as tables

from models import BioExamination
from .models import BioExaminationDetail
from .models import Examname


class BioExaminationDetailFilter(django_filters.FilterSet):
    class Meta:
        model = BioExaminationDetail
        exclude = ('BioExaminationId','notes')
        fields = {
#            'value': ['gte', 'lte'],
            'examnameid': ['exact', ],
#            'examnameid__groupexam' : ['exact', ],
#            'examnameid__bioexaminationcategory': ['exact', ],
#            'BioExaminationId__peopleid': ['exact', ],
        }

class BioExaminationDetailFilterAll(django_filters.FilterSet):
    class Meta:
        model = BioExaminationDetail
        exclude = ('BioExaminationId','notes')
        fields = {
            'examnameid': ['exact', ],
#            'BioExaminationId__peopleid': ['exact', ],
        }


class BioExaminationDetailFilterEx(django_filters.FilterSet):
    ex = django_filters.CharFilter(label='Ex filter', method='filter_ex')
    search_fields = ['examnameid__name' , ]

    def filter_ex(self, qs, name, value):
        if value:
            q_parts = value.split()

            q_totals = Q()

            combinatorics = itertools.product([True, False], repeat=len(q_parts) - 1)
            possibilities = []
            for combination in combinatorics:
                i = 0
                one_such_combination = [q_parts[i]]
                for slab in combination:
                    i += 1
                    if not slab: # there is a join
                        one_such_combination[-1] += ' ' + q_parts[i]
                    else:
                        one_such_combination += [q_parts[i]]
                possibilities.append(one_such_combination)

            for p in possibilities:
                list1=self.search_fields
                list2=p
                perms = [zip(x,list2) for x in itertools.permutations(list1,len(list2))]

                for perm in perms:
                    q_part = Q()
                    for p in perm:
                        q_part = q_part & Q(**{p[0]+'__icontains': p[1]})
                    q_totals = q_totals | q_part

            qs = qs.filter(q_totals)

        print 'AAA' , qs
        return qs

    class Meta:
        model = BioExaminationDetail
        fields = ['ex']


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
        exclude = ['BioExaminationId','id']
#        exclude = ['id',]
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

class BioExaminationDetTable2(BioExaminationDetTable):
    class Meta:
        model = BioExaminationDetail
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        exclude = ['id',]
        attrs = {'class': 'paleblue'}


def BioExaminationDetailFiltered(request,exampk):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    data = BioExaminationDetail.objects.all().filter(BioExaminationId=exampk)
    filter = BioExaminationDetailFilter(request.GET, queryset=data)
    table = BioExaminationDetTable(filter.qs)
#     table = BioExaminationDetTable(BioExaminationDetail.objects.all().filter(BioExaminationId=exampk))
    p = BioExamination.objects.get(id=exampk).peopleid
    e = BioExamination.objects.get(id=exampk)

    RequestConfig(request, paginate={'per_page': 20}).configure(table)
    return render(request, 'General/Generic_Table_view_filter_panel.html',
                  {'objects': table,
                   'filter' : filter,
                   'page_title': u'Ανάληση Εργαστηριακών για ' + p.name + ' ' + p.surname + ' ' + e.dateofexam.strftime('%d/%m/%Y'),
                   'form_name':  u'Ανάληση Εργαστηριακών για ' + p.name + ' ' + p.surname + ' ' + e.dateofexam.strftime('%d/%m/%Y'),
                   'param_action1': reverse('DjgLeoApp001:createexambiodet'),
                   'param_action1_name': 'Προσθήκη'})


from django.db.models import Q

def BioExaminationDetailFilteredAll(request,peoplepk):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    p_object = Q()
    pp = []
    initaa = 0
    for x in BioExamination.objects.all().filter(peopleid=peoplepk):
        aa = x.id
        pp.append(x.id)
        p_object.add(Q(BioExaminationId=aa), Q.OR)
        if initaa == 0:
            initaa = x.id

    print initaa
    print p_object
    data = BioExaminationDetail.objects.all().filter(p_object)
    filter = BioExaminationDetailFilterAll(request.GET, queryset=data)
    table = BioExaminationDetTable2(filter.qs)
    p = BioExamination.objects.get(id=initaa).peopleid
    e = BioExamination.objects.get(id=initaa)

    RequestConfig(request, paginate={'per_page': 20}).configure(table)
    return render(request, 'General/Generic_Table_view_filter_panel.html',
                  {'objects': table,
                   'filter' : filter,
                   'page_title': u'Ανάληση Εργαστηριακών για ' + p.name + ' ' + p.surname,
                   'form_name':  u'Ανάληση Εργαστηριακών για ' + p.name + ' ' + p.surname,
                   'param_action1': reverse('DjgLeoApp001:createexambiodet'),
                   'param_action1_name': 'Προσθήκη'})




#########################################################################################################################

from views_people import PeopleTable
from models import People

class PeopleFilter(django_filters.FilterSet):
    class Meta:
        model = People
        exclude = ('id','photo')


def PeopleFiltered(request):

    data = People.objects.all()
    filter = PeopleFilter(request.GET, queryset=data)
    table = PeopleTable(filter.qs)

    RequestConfig(request, paginate={'per_page': 20}).configure(table)
    return render(request, 'General/Generic_Table_view_filter_panel.html',
                  {'objects': table,
                   'filter' : filter,
                   'page_title': u'Ανάληση Εργαστηριακών για ',
                   'form_name':  u'Ανάληση Εργαστηριακών για ',
                   'param_action1': reverse('DjgLeoApp001:createexambiodet'),
                   'param_action1_name': 'Προσθήκη'})


def Graphos(request):
    data = [
        ['Year', 'Sales', 'Expenses', 'Items Sold', 'Net Profit', 'All'],
        ['2004', 1000, 400, 100, 600, 100],
        ['2005', 1170, 460, 120, 310, 100],
        ['2006', 660, 1120, 50, -460, 100],
        ['2007', 1030, 540, 100, 200, 100],
        ]

    from graphos.sources.simple import SimpleDataSource
    from graphos.renderers.gchart import LineChart
    from graphos.renderers.gchart import ColumnChart
    from graphos.renderers.gchart import BarChart
    from graphos.renderers.gchart import PieChart
    from graphos.renderers.gchart import AreaChart
    from graphos.renderers.gchart import TreeMapChart
    from graphos.renderers.gchart import CandlestickChart
    from graphos.renderers.gchart import GaugeChart

#    from graphos.renderers.highcharts import LineChart



    # DataSource object
    data_source = SimpleDataSource(data=data)
    # Chart object
    chart  = LineChart(data_source)
    chart1 = BarChart(data_source)
    context = {'chart': chart, 'chart1': chart1 }
    return render(request, 'char.html', context)


