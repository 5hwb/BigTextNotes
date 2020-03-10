from django import forms

class EditPostForm(forms.Form):
    text = forms.TextField(label='Text post to edit')
    text_colour = forms.CharField(label='Text colour')
    bg_colour = forms.CharField(label='Background colour')
