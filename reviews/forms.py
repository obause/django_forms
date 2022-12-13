from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#     username = forms.CharField(label="Dein Name", max_length=100, error_messages={
#         "required": "Der Name darf nicht leer sein",
#         "max_length": "Bitte einen kürzeren Namen eingeben"
#     })

#     review_text = forms.CharField(label="Dein Feedback", widget=forms.Textarea, max_length=500, required=False)

#     rating = forms.IntegerField(label="Deine Bewertung", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["username", "review_text", "rating"]  # for all fields: '__all__'
        # exclude = ['owner_comment']
        labels = {
            "username": "Dein Name",
            "review_text": "Dein Feedback",
            "rating": "Dein Rating"
        }
        error_messages = {
            "username": {
                "required": "Der Name darf nicht leer sein",
                "max_length": "Bitte einen kürzeren Namen eingeben"
            }
        }
