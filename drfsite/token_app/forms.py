from django import forms
from .models import *
from django.forms import ValidationError


class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ['name', 'amount', 'price']
        labels = {
            'name': 'Название',
            'amount': 'Колличество',
            'price': 'Цена за шт',
        }

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            raise ValidationError('Amount must be more than 0')

        return amount

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError('Price must be more than 0')

        return price