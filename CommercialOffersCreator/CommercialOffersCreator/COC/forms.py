from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['denomination', 'address', 'index', 'telephone', 'contactPersonPhoneNumber', 'contactPersonEmail', 'price_group_discounts']

        widgets = {
            'denomination': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'index': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'contactPersonPhoneNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'contactPersonEmail': forms.TextInput(attrs={'class': 'form-control'}),
            'price_group_discounts':forms.SelectMultiple(attrs={'class':'form-control'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['denomination', 'description', 'box_quantity', 'min_order_quantity', 'price_group', 'cost', 'list_price']

        widgets = {
            'denomination': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'box_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'min_order_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price_group': forms.Select(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'list_price': forms.NumberInput(attrs={'class': 'form-control'}),

        }


class PriceGroupFrom(forms.ModelForm):
    class Meta:
        model = PriceGroup
        fields = ['denomination']

        widgets = {
            'denomination': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PriceGroupDiscountFrom(forms.ModelForm):
    class Meta:
        model = PriceGroupDiscount
        fields = ['price_group', 'discount']

        widgets = {
            'price_group': forms.Select(attrs={'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control'}),
        }
