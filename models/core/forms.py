from django import forms

from core import models


class PhoneSearch(forms.Form):
    phone_name = forms.CharField(label='Поиск по названию', required=False, help_text='Поиск по названию телефона', max_length=255)


    def clean(self):
        name = self.cleaned_data.get('phone_name')
        if '/' in name:
            raise forms.ValidationError('Имя не должно содержать "/"!')
        return name
    

class PhoneForm(forms.ModelForm):
    phone_name = forms.CharField(label='Модель телефона', required=False)
    name_oc = forms.CharField(label='Название ОС', required=False)
    volume_memory = forms.IntegerField(label='Объём памяти', min_value=0, required=False)


    def clean_phone_name(self):
        phone_name = self.cleaned_data.get('phone_name')
        if  phone_name.isdigit():
            raise forms.ValidationError('Имя должно быть строкой!')
        return phone_name
    

    class Meta:
        model = models.Phone
        fields = '__all__'