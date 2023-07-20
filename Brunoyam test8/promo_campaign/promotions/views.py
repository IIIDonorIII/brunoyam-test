from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, CampaignForm, HouseVisitForm
from .models import Campaign, HouseVisit

def index(request):
    return render(request, 'index.html')

def user_page(request):
    return render(request, 'user_page.html')

def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('user_page')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})

def campaign_statistics(request):
    campaigns = Campaign.objects.all()
    campaign_statistics = []
    
    for campaign in campaigns:
        visits_count = HouseVisit.objects.filter(campaign=campaign).count()
        campaign_statistics.append({
            'campaign': campaign,
            'visits_count': visits_count
        })
    
    return render(request, 'campaign_statistics.html', {'campaign_statistics': campaign_statistics})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_page')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def user_dashboard(request): 
    user_campaigns = Campaign.objects.filter(user=request.user)
    if request.method == 'POST':
        campaign_form = CampaignForm(request.POST)
        house_visit_form = HouseVisitForm(request.POST)
        if campaign_form.is_valid():
            campaign = campaign_form.save(commit=False)
            campaign.user = request.user
            campaign.save()
            return redirect('user_dashboard')
        elif house_visit_form.is_valid():
            house_visit = house_visit_form.save(commit=False)
            house_visit.user = request.user
            house_visit.save()
            return redirect('user_dashboard')
    else:
        campaign_form = CampaignForm()
        house_visit_form = HouseVisitForm()
    return render(request, 'user_page.html', {
        'campaign_form': campaign_form,
        'house_visit_form': house_visit_form,
        'user_campaigns': user_campaigns
    })