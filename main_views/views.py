from django.shortcuts import get_object_or_404, render
from .models import Book, Review


def show_main(request):
    return render(request, "index.html", {"books": Book.objects.all(),
                                          "reviews": Review.objects.all()})




