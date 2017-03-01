from django.shortcuts import render
from django.views.generic import TemplateView, ListView
import django_tables2
from .models import BioExaminationDetail

from django.db.models import Q
import django_filters
import itertools

import django_tables2 as tables

class BioExaminationDetailTable(tables.Table):
    class Meta:
        model = BioExaminationDetail

class BioExaminationDetailFilter(django_filters.FilterSet):
    class Meta:
        model = BioExaminationDetail
        exclude = ()


class BioExaminationDetailFilterEx(django_filters.FilterSet):
    ex = django_filters.CharFilter(label='Ex filter', method='filter_ex')
    search_fields = ['title', 'author', 'category', 'id', ]

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

        return qs

    class Meta:
        model = BioExaminationDetail
        fields = ['ex']


class FilteredSingleTableView(django_tables2.SingleTableView):
    filter_class = None

    def get_table_data(self):
        data = super(FilteredSingleTableView, self).get_table_data()
        self.filter = self.filter_class(self.request.GET, queryset=data)
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(FilteredSingleTableView, self).get_context_data(**kwargs)
        context['filter'] = self.filter
        return context


class BioExaminationDetailFilteredSingleTableView(FilteredSingleTableView):
    model = BioExaminationDetail
    table_class = BioExaminationDetailTable
    filter_class = BioExaminationDetailFilter


class BioExaminationDetailSingleTableView(django_tables2.SingleTableView):
    model = BioExaminationDetail
    table_class = BioExaminationDetailTable


class FilteredTableView(ListView):
    model = BioExaminationDetail

    def get_context_data(self, **kwargs):
        context = super(FilteredTableView, self).get_context_data(**kwargs)
        filter = BioExaminationDetail.filters.BookFilter(self.request.GET, queryset=self.object_list)

        table = BioExaminationDetail.tables.BookTable(filter.qs)
        django_tables2.RequestConfig(self.request, ).configure(table )

        context['filter'] = filter
        context['table'] = table
        return context


class FilterExListView(ListView):
    model = BioExaminationDetail

    def get_context_data(self, **kwargs):
        context = super(FilterExListView, self).get_context_data(**kwargs)
        filter = BioExaminationDetail.filters.BookFilterEx(self.request.GET, queryset=self.object_list)

        table = BioExaminationDetail.tables.BookTable(filter.qs)
        django_tables2.RequestConfig(self.request, ).configure(table )

        context['filter'] = filter
        context['table'] = table

        return context



