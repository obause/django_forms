from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review


# Create your views here.
class ReviewView(CreateView):  # CreateView benötigt kein ModelForm (ReviewForm Klasse) mehr
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/submit-success"


# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/submit-success"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {
#             "form": form
#         })

#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/submit-success")
#         return render(request, "reviews/review.html", {
#             "form": form
#         })


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


class SubmitSuccessView(TemplateView):
    template_name = "reviews/submit_success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Funktioniert"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=0)
        return data


class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = review.id == int(favorite_id)
        return context


# class ReviewDetailView(TemplateView):
#     template_name = "reviews/review_detail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs['id']
#         review = Review.objects.get(pk=review_id)
#         context['review'] = review
#         return context

class FavoriteView(View):
    def post(self, request):
        review_id = request.POST.get("review_id")
        # review = Review.objects.get(pk=review_id)
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect(f"/reviews/{review_id}")
