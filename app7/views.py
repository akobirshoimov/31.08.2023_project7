from django.shortcuts import render,get_object_or_404
from .models import Ichimliklar,Korxona
from django.http import JsonResponse

# Create your views here.
def all(request):
    all = Ichimliklar.objects.all()
    result = []
    for i in all:
        result.append({
            'name':i.name,
            'narhi':i.narhi,
            'hajmi':i.hajmi
        })
    return JsonResponse(result,safe =False)

def detail(request,detail_id):
    each = Korxona.objects.get(id=detail_id)
    each = get_object_or_404(Korxona,id=detail_id)
    info = f'nomi:{Korxona.name},{Korxona.build_in} da qurilgan'
    return JsonResponse(info)



