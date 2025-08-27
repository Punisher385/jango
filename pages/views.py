from django.shortcuts import render

def home(request):
    pages = [
        {'name': 'Page 1', 'url': 'page1'},
        {'name': 'Page 2', 'url': 'page2'},
        {'name': 'Page 3', 'url': 'page3'},
        {'name': 'Page 4', 'url': 'page4'},
        {'name': 'Page 5', 'url': 'page5'},
    ]
    return render(request, 'pages/home.html', {'pages': pages, 'title': 'Home'})

def page(request, number):
    title = f"Page {number}"
    return render(request, 'pages/page.html', {'title': title})
