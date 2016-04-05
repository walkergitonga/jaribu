from django.shortcuts import render

# Create your views here.
def inquiry_list(request):
    return render(request, 'contact/inquiry_list.html', {})