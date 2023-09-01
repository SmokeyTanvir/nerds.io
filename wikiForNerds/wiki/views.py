from django.shortcuts import render
import markdown2
from . import util
from django.http import HttpResponse
import re

def convert_to_html(md_title):
    content = util.get_entry(md_title)
    # Render the modified Markdown content
    html_content = markdown2.markdown(content, extras=["fenced-code-blocks"])

    if content == None:
        return None
    else:
        return html_content

def index(request):
    return render(request, "index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = convert_to_html(title)
    if content == None:
        return render(request, "error.html")

    return render(request, "entry.html", {
        "title": title,
        "content": content
        })

def create(request):
    if(request.method == "POST"):
        entry_title = request.POST["title"]
        entry_content = request.POST["content"]
        util.save_entry(entry_title, entry_content)

    return render(request, "create.html")


def random(request):
    return render(request, "random.html")