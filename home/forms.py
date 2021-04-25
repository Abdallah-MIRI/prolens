# from django.forms import ModelForm
from django import forms


class ContactForm(forms.Form):
  client_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Your Name'}))
  client_number = forms.CharField(max_length=13, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Number'}))
  email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
  message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'massage'}))
  # cc_myself = forms.BooleanField(required=False)
  
  def __str__(self):
      return self.client_name