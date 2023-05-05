from django.shortcuts import render
from core import models
from django.views.generic import DetailView, ListView
from django.http import HttpResponse

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
    


