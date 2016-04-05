from django.shortcuts import render
from django.utils import timezone
from .models import Inquiry

# Create your views here.
def inquiry_list(request):
    inquiries = Inquiry.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'contact/inquiry_list.html', {'inquiries': inquiries})