from django.shortcuts import render
from django.views import View


# Create your views here.

class Index(View):
    def get(self, request):
        paramns = {}
        paramns["name"] = "Palmas Beer"
        return render(request, 'index.html', paramns)