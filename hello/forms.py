from django import forms

class FileForm(forms.Form):
    newFile = forms.FileField(
            label = 'Select a file',
            required = True,
            )
