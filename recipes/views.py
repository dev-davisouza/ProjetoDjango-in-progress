from django.shortcuts import render, redirect
from .models import Recipe


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id, is_published=True)

    if not recipes:
        response = render(request, 'recipes/pages/404_error.html')
        response.status_code = 404
        return response

    context = {'recipes': recipes,
               'title': f'{recipes.first().category.name} | ',
               }
    return render(request, 'recipes/pages/category.html', context)


def home(request):
    if Recipe.objects.filter(is_published=True).exists():
        recipes = Recipe.objects.filter(
            is_published=True).order_by('updated_at')
        context = {'recipes': recipes, }
        return render(request, 'recipes/pages/home.html', context)
    else:
        return render(request, 'recipes/pages/Not_recipes_yet.html', status=404)


def recipe(request, id):
    if Recipe.objects.filter(pk=id).exists():
        recipe = Recipe.objects.get(pk=id)
        context = {'recipe': recipe,
                   'title': f'{recipe.title} | ',
                   'is_detail_page': True, }
        return render(request, 'recipes/pages/recipe.html', context)
    else:
        response = render(request, 'recipes/pages/404_error.html')
        response.status_code = 404
        return response
