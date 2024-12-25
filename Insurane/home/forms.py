from django import forms


class Contactforms(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    messsage = forms.CharField(widget=forms.Textarea)