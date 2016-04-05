from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Inquiry

# Create your views here.
def inquiry_list(request):
    inquiries = Inquiry.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'contact/inquiry_list.html', {'inquiries': inquiries})

def inquiry_detail(request, pk):
    inquiry = get_object_or_404(Inquiry, pk=pk)
    return render(request, 'contact/inquiry_detail.html', {'inquiry': inquiry})

