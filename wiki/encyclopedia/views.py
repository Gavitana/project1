from django.shortcuts import render
from django import forms
from . import util
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import default_storage
from django.shortcuts import redirect
import random
from .models import Person

class NewEntryForm(forms.Form):
	entry = forms.CharField(label = "Name of entry")
	comment= forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":150}),label = "Entry Text")


def index(request):
	return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request,title):
	return render(request, "encyclopedia/page.html" ,{
		"title":util.get_entry(title),
		"entry":title
		})

def search(request):
	if request.method == "POST":
		query = request.POST['q']
		entries = util.list_entries()
		for entry in entries:
			if query in entry:
				return render(request, "encyclopedia/search_result.html", {
                "title": entries,
                "title_page":entry
                	})
			else:
				return render(request, "encyclopedia/Pagenotfound.html")

def add(request):
	if request.method == "POST":
		form = NewEntryForm(request.POST)
		if form.is_valid():
			entry = form.cleaned_data["entry"]
			comment = form.cleaned_data["comment"]
			if entry in util.list_entries():
				return render(request, "encyclopedia/error.html")
			else:
				entries = util.save_entry(entry,comment)
				return HttpResponseRedirect(reverse('encyclopedia:index'))
		else:
			return render(request, "encyclopedia/add.html",{
				"form":form
				})
	return render(request, "encyclopedia/add.html" , {
		"form":NewEntryForm()
	})

def edit(request, title):
	f = default_storage.open(f"entries/{title}.md")
	x = f.read().decode("utf-8")

	if request.method == "GET":
		return render(request, "encyclopedia/edit.html",{
			"content":x,
			"title":title
		})


	title = request.POST['Name of Entry']
	content = request.POST['comment']
	if request.method == "POST":
		util.save_entry(title, content)
		return redirect('encyclopedia:page', title=title)

def random_page(request):
	entries = util.list_entries()
	selected_page = random.choice(entries)
	return redirect('encyclopedia:page', title=selected_page)

def persona(request):
	return render(request, "encyclopedia/persons.html",{
		"persons":Person.objects.all()
	})
