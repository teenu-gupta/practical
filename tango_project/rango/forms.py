from django import forms
from rango.models import Category , Page

class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=120, help_text= "Please enter the title of Page")
	url = forms.URLField(max_length= 120, help_text = "Please enter the URL")
	views = forms.IntegerField(widget= forms.HiddenInput(), initial = 0)
	class Meta:
		model = Page
		fields = ('title', 'url' , 'views')


class CategoryForm(forms.ModelForm):
	name = forms.CharField(help_text="Please enter the Category Name",max_length = 128)
	class Meta:
		model = Category
