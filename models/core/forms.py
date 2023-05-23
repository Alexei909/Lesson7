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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].empty_label = 'Категория не выбрана'

    class Meta:
        model = models.Phone
        fields = ('phone_name', 'name_oc', 'volume_memory', 'on_sale', 'date_of_issue', 'company', 'shop')

        