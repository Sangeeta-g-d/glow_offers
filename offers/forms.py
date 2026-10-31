from django import forms

from .models import Offer


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ["title", "description", "image", "link", "is_pinned"]
        labels = {
            "title": "Offer title",
            "description": "Short description (optional, up to 3 lines)",
            "image": "Product image",
            "link": "Offer link",
            "is_pinned": "Pin this offer to the top",
        }
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Buy 1 Get 1 on lip balms"}),
            "description": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Hydrating tinted balms in 6 shades. Offer valid till Sunday."}
            ),
            "link": forms.URLInput(attrs={"placeholder": "https://shop.example.com/offer"}),
            "image": forms.ClearableFileInput(attrs={"accept": "image/*"}),
        }

    def clean_description(self):
        text = self.cleaned_data["description"].strip()
        if len(text.splitlines()) > 3:
            raise forms.ValidationError("Keep the description to 3 lines or fewer.")
        return text
