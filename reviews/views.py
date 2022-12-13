from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View

from .forms import ReviewForm
from .models import Review


# Create your views here.
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/submit-success")
        return render(request, "reviews/review.html", {
            "form": form
        })


def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            # form_data = form.cleaned_data
            # review = Review(
            #     username=form_data.get("username"),
            #     review_text=form_data.get("review_text"),
            #     rating=form_data.get("rating")
            # )
            # review.save()
            form.save()
            return HttpResponseRedirect("/submit-success")
    else:
        form = ReviewForm()
    return render(request, "reviews/review.html", {
        "form": form
    })


def submit_success(request):
    return render(request, "reviews/submit_success.html")
