from django.shortcuts import render, redirect
from .models import Review

def reviewsCreate(request, *args, **kwargs):
    if request.method == "POST":
        newReview = Review.objects.create(
            title = request.POST["title"],
            director = request.POST["director"],
            actor = request.POST["actor"],
            genre = request.POST["genre"],
            stars = request.POST["stars"],
            createDate = request.POST["createDate"],  
            runtime = request.POST["runtime"],    
            content = request.POST["content"]    
        )
        return redirect("/")
        
    return render(request, "reviews/reviews_create.html")

def reviewsDelete(request, pk, *args, **kwargs):
    review = Review.objects.get(id=pk)
    review.delete()
    return redirect("/")

def reviewsUpdate(request, pk, *args, **kwargs):
    review = Review.objects.get(id=pk)
    return render(request, "reviews/reviews_update.html", {"review": review})

def reviewsList(request, *args, **kwargs):
    reviews = Review.objects.all()
    return render(request, "reviews/reviews_list.html", {"reviews": reviews})

def reviewsDetail(request, pk, *args, **kwargs):
    review = Review.objects.get(id=pk)
    return render(request, "reviews/reviews_detail.html", {"review": review})
