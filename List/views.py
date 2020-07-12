from django.shortcuts import render

def list(request):
    location_list = 3
    return render(request, 'List/list.html', { 'location_list': location_list })