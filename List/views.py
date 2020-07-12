from django.shortcuts import render

def list(request):
    return render(request, 'List/list.html', {})