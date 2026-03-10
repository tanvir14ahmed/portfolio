from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'id': 'contact-name',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your Email',
                'id': 'contact-email',
                'required': True,
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Your Message',
                'id': 'contact-message',
                'rows': 5,
                'required': True,
            }),
        }
