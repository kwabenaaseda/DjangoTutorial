from django.http import HttpResponse, HttpRequest
from .models import Collection, Piece
from django.shortcuts import render
from django.db.models import Count
import random

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    """Main genres listing page"""
    all_collections = Collection.objects.all()
    context = {
        "all_collections": all_collections
    }
    return render(request, "genre/genretemplate.html", context)

def details(request: HttpRequest, collection_id: int) -> HttpResponse:
    """Individual collection details page"""
    collection = Collection.objects.get(pk=collection_id)
    piece = Piece.objects.filter(collection=collection)
    context = {
        "app_pieces": piece
    }
    return render(request, "genre/details.html", context)

def homepage(request: HttpRequest) -> HttpResponse:
    """New homepage with featured collections and stats"""
    # Get all collections
    collections = Collection.objects.all()
    
    # Get total counts
    total_collections = collections.count()
    total_pieces = Piece.objects.count()
    
    # Get a random featured collection
    featured_collection = None
    if total_collections > 0:
        featured_collection = random.choice(collections)
        featured_pieces = Piece.objects.filter(collection=featured_collection)[:4]  # Get first 4 pieces
    
    # Get collections with piece counts
    collections_with_counts = Collection.objects.annotate(piece_count=Count('piece'))
    
    # Get some random pieces for the "random picks" section
    all_pieces = list(Piece.objects.all())
    random_pieces = random.sample(all_pieces, min(6, len(all_pieces))) if all_pieces else []
    
    context = {
        'collections': collections_with_counts,
        'total_collections': total_collections,
        'total_pieces': total_pieces,
        'featured_collection': featured_collection,
        'featured_pieces': featured_pieces if featured_collection else [], # type: ignore
        'random_pieces': random_pieces,
    }
    return render(request, "genre/homepage.html", context)