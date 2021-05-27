from django import forms

from.models import ToDo, MOVIESinfo

class ToDoForm(forms.ModelForm):
	class Meta:
		model = ToDo
		fields = [
			 'Task',
			 'Description',
			]


class MOVIESinfoForm(forms.ModelForm):
	class Meta:
		model = MOVIESinfo
		fields = [
			 'title',
			 'year',
			 'runtime_min',
			 'genres',
			 'language',
			 'imdb_rating',
			 'actors',

			]