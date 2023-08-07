from django.shortcuts import render, get_object_or_404

from .models import Hobby

# Create your views here.
def home(request):
    hobby = Hobby.objects
    return render(request, 'hobbies/home.html',{'hobby':hobby})

def detail(request, hobby_id):
    hobby_detail = get_object_or_404(Hobby, pk=hobby_id)
    return render(request, 'hobbies/detail.html', {'hobby':hobbies_detail})
