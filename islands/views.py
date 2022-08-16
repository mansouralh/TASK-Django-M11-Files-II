from django.http import HttpRequest, HttpResponse
from .forms import IslandForm
from django.shortcuts import redirect, render

from islands import models


def get_islands(request: HttpRequest) -> HttpResponse:
    islands: list[models.Island] = list(models.Island.objects.all())

    context = {
        "islands": islands,
    }

    return render(request, "island_list.html", context)


# def create_island(request):
#     form = IslandForm()
#     if request.method == "POST":
#         form = IslandForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("island-list")
#     context = {
#         "form": form,
#     }
#     return render(request, 'create_island.html', context)



def create_island(request: HttpRequest) -> HttpResponse:
    form = IslandForm()
    if request.method == "POST":
        form = IslandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("island-list")
    context = {
        "form": form,
    }
    return render(request, "create_island.html", context)