from django.shortcuts import render

# home view.
def home(request):
    return render(request, 'home.html', {})

# africa-fund view.
def africafund(request):
    return render(request, 'africafund.html', {})

# terms view
def mnterms(request):
    return render(request, 'mn-terms.html', {})

# terms view
def afroterms(request):
    return render(request, 'afro-terms.html', {})