from django import forms


class ListForm(forms.Form):
	user = forms.CharField(max_length=100)
	number = forms.IntegerField()
	fields = ('user','number')