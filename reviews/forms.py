from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(label="Dein Name", max_length=100, error_messages={
        "required": "Der Name darf nicht leer sein",
        "max_length": "Bitte einen kürzeren Namen eingeben"
    })
