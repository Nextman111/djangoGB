import datetime

from django import forms


class ClientAddForm(forms.Form):
    name = forms.CharField(max_length=100, )
    email = forms.EmailField()
    phone = forms.CharField(max_length=12)
    adress = forms.CharField(max_length=100)
    date_reg = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
            }
        )
    )
