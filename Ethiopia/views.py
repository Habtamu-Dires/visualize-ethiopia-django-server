from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render

from .models import Element

# Create your views here.
def index(request):
    return render(request, "Ethiopia/index.html")

def graphs(request, id):
    item = Element.objects.get(id = id)
    if (item.file_type == 'html'):
        return render(request, 'Ethiopia/'+ id +'.html')
    elif(item.file_type == 'image'):
        return JsonResponse({'public_id': str(item.image)}, safe=False)    

def elements(request):
    elements = Element.objects.all()
    array_of_elements = []
    for element in elements:
        array_of_elements.append(element.serialize())
        

    return JsonResponse({"response": array_of_elements}, safe=False)