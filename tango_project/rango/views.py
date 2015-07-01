from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Category
from models import Page
from rango.forms import CategoryForm



# Create your views here.

def index(request):
	context=RequestContext(request)
	
	category_list = Category.objects.order_by('-name')[:3]
	context_dict = {'categories': category_list}

	for category in category_list:
		#import pdb
		#pdb.set_trace()
		category.url=category.name.replace(' ','_')

	print category_list
	return render_to_response('rango/index.html',context_dict,context)

def about(request):
	context = RequestContext(request)
	context_dict= {'about_us': "About Our Company"}
	return render_to_response('rango/about.html',context_dict,context)


def category(request,category_name_url):
	context=RequestContext(request)
	category_name_url = category_name_url.replace('_',' ')
	context_dict = {'category_name' : category_name_url}
	try:
		category = Category.objects.get(name = category_name_url)
		pages = Page.objects.filter(category=category)
		context_dict['pages'] = pages
		context_dict['category']= category
	except Category.DoesNotExist:
		pass
	return render_to_response('rango/category.html',context_dict,context)

def addcategory(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save(commit=True)

			return index(request)

		else:
			form.errors
	else:
		form = CategoryForm()

	return render_to_response('rango/addcategory.html',{'form':form},context)