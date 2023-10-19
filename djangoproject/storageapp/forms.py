import datetime

from django import forms

from storageapp.models import Order


class ClientForm(forms.Form):
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


class ProductForm(forms.Form):

    title = forms.CharField(max_length=100)
    description = forms.Textarea()
    price = forms.DecimalField(max_digits=10, decimal_places=2,)
    count = forms.IntegerField(min_value=0.0)
    date_update = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
            }
        )
    )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"