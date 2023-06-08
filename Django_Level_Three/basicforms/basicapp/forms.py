from django import forms 
from django.core import validators





class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    textarea = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_date = super().clean()
        email = all_clean_date['email']
        vmail = all_clean_date['verify_email']


        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")

    


