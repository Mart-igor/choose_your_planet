from django.shortcuts import render, get_object_or_404
from .models import Celestial, Categories

# Create your views here.
def index(request):
    celestial = Celestial.objects.filter(available=True)
    return render(request, 'main/index.html', {'celestial': celestial})

def celestial_list(request, category_slug=None):
    category = None
    categories = Categories.objects.all()
    celestial = Celestial.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Categories, slug=category_slug)
        # celestial = Celestial.objects.filter(category=category)
    return render(request, 'main/celestial.html', {'category':category,
                                                   'categories': categories,
                                                   'celestial': celestial})

def detail(request, celestial_slug):
    celesta = get_object_or_404(Celestial, slug=celestial_slug)
    return render(request, 'main/detail.html', {'celesta': celesta})
