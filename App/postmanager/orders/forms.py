from .models import Orders
from  django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['title', 'sender_name', 'sender_addres', 'receiver_name', 'receiver_addres',  'weight']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'sender_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя отправителя'
            }),
            'sender_addres': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес отправителя'
            }),
            'receiver_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя получателя'
            }),
            'receiver_addres': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес получателя'
            }), 
            'weight': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вес посылки, г.'
            }),
        }
