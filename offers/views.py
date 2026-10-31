from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import OfferForm
from .models import Offer


def staff_required(view):
    return user_passes_test(
        lambda u: u.is_active and u.is_staff, login_url="/manage/login/"
    )(view)


# ---------- User page ----------
def home(request):
    offers = Offer.objects.all()
    context = {
        "pinned": [o for o in offers if o.is_pinned],
        "others": [o for o in offers if not o.is_pinned],
    }
    return render(request, "offers/home.html", context)


# ---------- Admin page ----------
@staff_required
def dashboard(request):
    if request.method == "POST":
        form = OfferForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Offer added. It is now live on the site.")
            return redirect("dashboard")
    else:
        form = OfferForm()
    return render(
        request,
        "offers/dashboard.html",
        {"form": form, "offers": Offer.objects.all()},
    )


@staff_required
@require_POST
def toggle_pin(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    offer.is_pinned = not offer.is_pinned
    offer.save(update_fields=["is_pinned"])
    messages.success(request, "Offer pinned." if offer.is_pinned else "Offer unpinned.")
    return redirect("dashboard")


@staff_required
@require_POST
def delete_offer(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    offer.delete()
    messages.success(request, "Offer removed from the site.")
    return redirect("dashboard")
