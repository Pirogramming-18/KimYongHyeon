from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
def reviewsCreate(request, *args, **kwargs):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            #explain, src 제외
            newReview = Review.objects.create(
                title = form.cleaned_data["title"],
                director = form.cleaned_data["director"],
                actor = form.cleaned_data["actor"],
                genre = form.cleaned_data["genre"],
                stars = form.cleaned_data["stars"],
                createDate = form.cleaned_data["createDate"],  
                runtime = form.cleaned_data["runtime"],    
                content = form.cleaned_data["content"]    
            )
            return redirect("/")
        else:
            return render(request, "reviews/reviews_create.html", {'form': form})
    else:
        form = ReviewForm()
        return render(request, "reviews/reviews_create.html", {'form': form})

def reviewsDelete(request, pk, *args, **kwargs):
    review = Review.objects.get(id=pk)
    review.delete()
    return redirect("/")

def reviewsUpdate(request, pk, *args, **kwargs):
    review = Review.objects.get(id=pk)
    form = ReviewForm(instance=review)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            #explain, src 제외
            review.title = form.cleaned_data["title"]
            review. director = form.cleaned_data["director"]
            review.actor = form.cleaned_data["actor"]
            review.genre = form.cleaned_data["genre"]
            review.stars = form.cleaned_data["stars"]
            review.createDate = form.cleaned_data["createDate"]
            review.runtime = form.cleaned_data["runtime"]
            review.content = form.cleaned_data["content"]   
            review.save()
            return redirect(f"/reviews-detail/{pk}")
        else:
            return render(request, "reviews/reviews_create.html", {'form': form})
    return render(request, "reviews/reviews_update.html", {"form": form, "pk": pk})

def reviewsList(request, *args, **kwargs):
    reviews = Review.objects.all()
    return render(request, "reviews/reviews_list.html", {"reviews": reviews})

def reviewsDetail(request, pk, *args, **kwargs):
    review = Review.objects.get(id=pk)
    return render(request, "reviews/reviews_detail.html", {"review": review})
