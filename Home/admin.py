from django.contrib import admin

from Home.models import Pet, PetCategory, PetCategoryKind, Person

admin.site.register(Pet)
admin.site.register(PetCategory)
admin.site.register(PetCategoryKind)
admin.site.register(Person)
