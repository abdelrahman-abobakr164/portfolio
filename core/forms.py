from django import forms



class ContactForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    message = forms.CharField(required=True, widget=forms.TextInput())