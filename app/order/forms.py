from django import forms

from order.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        models = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']