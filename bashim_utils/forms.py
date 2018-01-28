from django import forms

class AbyssUpdateForm(forms.Form):
	days = forms.IntegerField(label='дней', required=False)

class BashUpdateForm(forms.Form):
	pages = forms.IntegerField(label='страниц', required=False)

