from django import forms

class AddPost(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=1000, required=False, widget=forms.Textarea)
