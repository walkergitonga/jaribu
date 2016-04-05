from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Inquiry
from .forms import InquiryForm

# Create your views here.
def inquiry_list(request):
    inquiries = Inquiry.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'contact/inquiry_list.html', {'inquiries': inquiries})

def inquiry_detail(request, pk):
    inquiry = get_object_or_404(Inquiry, pk=pk)
    return render(request, 'contact/inquiry_detail.html', {'inquiry': inquiry})

def inquiry_new(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.date = timezone.now()
            inquiry.save()
            return redirect('inquiry_detail', pk=inquiry.pk)
    else:
        form = InquiryForm()
    return render(request, 'contact/inquiry_edit.html', {'form': form})

def inquiry_edit(request, pk):
    inquiry = get_object_or_404(Inquiry, pk=pk)
    if request.method == "POST":
        form = InquiryForm(request.POST, instance=inquiry)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.date = timezone.now()
            inquiry.save()
            return redirect('inquiry_detail', pk=inquiry.pk)
    else:
        form = InquiryForm(instance=inquiry)
    return render(request, 'contact/inquiry_edit.html', {'form': form})


