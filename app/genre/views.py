from django.http import HttpResponse,HttpRequest
from .models import Collection, Piece
from django.shortcuts import render
# Create your views here.

def index(request: HttpRequest)  -> HttpResponse:
    all_collections = Collection.objects.all()
    context = {
        "all_collections": all_collections
    }
    return render(request, "genre/genretemplate.html", context)

def details(request: HttpRequest, collection_id: int) -> HttpResponse:
    collection = Collection.objects.get(pk=collection_id)
    piece = Piece.objects.filter(collection = collection)
    context = {
        "app_pieces": piece
    }
    return render(request,"genre/details.html", context)