from django.shortcuts import render

from Home.models import Person, Pet, PetCategoryKind, PetCategory


def profile(request):
    try:
        context = {
            'user': Person.objects.get(username=request.user)
        }
        return render(request, 'profile.html', context)

    except:
        context = {
            'user': None
        }
        return render(request, 'profile.html', context)




def index(request):
    pets = Pet.objects.all()
    kinds = PetCategoryKind.objects.all()
    categories = PetCategory.objects.all()
    try:
        user = request.user
        user = Person.objects.get(username=user)
        context = {
            'user': user,
            'pets': pets,
            'categories': categories,
            'kinds': kinds
        }
        return render(request, 'index.html', context)
    except:
        context = {
            'user': None,
            'pets': pets,
            'categories': categories,
            'kinds': kinds
        }
        return render(request, 'index.html', context)


def contact(request):
    pets = Pet.objects.all()
    kinds = PetCategoryKind.objects.all()
    categories = PetCategory.objects.all()
    try:
        user = request.user
        user = Person.objects.get(username=user)
        context = {
            'user': user,
            'pets': pets,
            'categories': categories,
            'kinds': kinds
        }
        return render(request, 'contact.html', context)
    except:
        context = {
            'user': None,
            'pets': pets,
            'categories': categories,
            'kinds': kinds
        }
        return render(request, 'contact.html', context)


def destination(request):
    return render(request, 'destination.html')


def pricing(request):
    return render(request, 'pricing.html')


def signup(request):
    if request.method == 'POST':
        return request()
    else:
        return None