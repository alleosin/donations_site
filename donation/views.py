from django.shortcuts import render, get_object_or_404
from .models import Acceptor, Donation
from .forms import DonationForm

# Create your views here.
def view_page(request, username):
    owner = get_object_or_404(Acceptor, login=username)
    if request.user == username:
        donations = Donation.objects.filter(acceptor = owner).order_by("-created_date")
    context = {
        "owner": owner,
        "donations": donations,
    }
    return render(request, "user_page.html", context)

def donate(request, username):
    if request.method == "POST":
        donation_form = DonationForm(data=request.POST)
        if donation_form.is_valid():
            new_donate = donation_form.save(commit=False)
            if new_donate.donater == "":
                new_donate.donater = "Ananim"
            new_donate.acceptor = username
            new_donate.save()
    else:
        donation_form = DonationForm()
    return render(request,
                  "donation.html",
                  {"donation_form": donation_form})
