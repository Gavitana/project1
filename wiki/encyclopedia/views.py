from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request,title):
	return render(request, "encyclopedia/page.html", {
		"title":util.get_entry(title)
		})

def search(request):
    if request.method == "POST":
        query = request.POST['q'] 
        entries = util.list_entries()
        if query == entries:
            return render(request, "encyclopedia/page.html", {
        "title":util.get_entry(title)
        })