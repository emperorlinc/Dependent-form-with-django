from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Person, City, Country
from .forms import PersonForm
from django.http import JsonResponse
import json

def index_view(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            messages.error(request, "Invalid credientials provided.")
            return redirect("index")
    context = { "form": form }
    return render(request, "index.html", context)

def getCities(request):
    data = json.loads(request.body)
    country_id = data["id"]
    cities = City.objects.filter(country__id=country_id)
    return JsonResponse(list(cities.values("id", "city")), safe=False)
