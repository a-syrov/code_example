from django import forms

class QuotesFilterForm(forms.Form):
	ordering = forms.ChoiceField(label="", required=False, choices=[
			['-date', 'Сначала новые'],
			['date', 'Сначала старые'],			
			['rating', 'По возрастанию рейтинга'],
			['-rating', 'По убыванию рейтинга'],
			['is_comics', 'Только с комиксом'],
		])

class QuotesAbyssFilterForm(forms.Form):
	ordering = forms.ChoiceField(label="", required=False, choices=[
			['-date', 'Сначала новые'],
			['date', 'Сначала старые'],
		])