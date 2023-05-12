from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from core import models, forms, filters
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.db.models import Q
from django.urls import reverse_lazy


class TitleMixin:
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_title()
        return context


def index(request):
    user = request.user.username
    context={'user': user,
             'title':'Главная страница'
}
    return render(request=request, template_name='core/index.html', context=context)

def phone_detail(request, pk):
    phone = models.Phone.objects.get(id=pk)
    context = {'phone': phone,
               'title': 'Телефон'
}
    return render(request=request, template_name='core/phone.html', context=context)


class PhoneList(TitleMixin, ListView):
    model = models.Phone
    template_name = 'core/phone_list.html'
    context_object_name = 'phones'
    title = 'Список телефонов'

    def get_queryset(self):
        return self.get_filter().qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filter()
        context['count'] = self.get_queryset().count()
        return context

    def get_filter(self):
        return filters.PhoneFilter(self.request.GET)

class PhoneCreate(TitleMixin, CreateView):
    model = models.Phone
    template_name = 'core/phone_create.html'
    form_class = forms.PhoneForm
    success_url = reverse_lazy('core:phone_list')


class PhoneUpdate(TitleMixin, UpdateView):
    model = models.Phone
    template_name = 'core/phone_create.html'
    form_class = forms.PhoneForm
    success_url = reverse_lazy('core:phone_list')


class PhoneDelete(TitleMixin, DeleteView):
    model = models.Phone
    template_name = 'core/phone_delete.html'
    success_url = reverse_lazy('core:phone_list')
