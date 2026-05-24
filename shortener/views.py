from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import ShortenedURL
from .shortener import shorten_url

def home(request):
    """Home page with form to shorten URLs"""
    short_url = None
    
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        if original_url:
            # Ensure URL starts with http:// or https://
            if not original_url.startswith(('http://', 'https://')):
                original_url = 'https://' + original_url
            
            code = shorten_url(original_url, ShortenedURL)
            # Build full short URL from request
            short_url = request.build_absolute_uri(f'/{code}/')
    
    return render(request, 'home.html', {'short_url': short_url})

def redirect_to_original(request, short_code):
    """Redirect from short code to original URL"""
    shortened = get_object_or_404(ShortenedURL, short_code=short_code)
    shortened.increment_clicks()
    return redirect(shortened.original_url)

def stats(request, short_code):
    """View stats for a shortened link"""
    shortened = get_object_or_404(ShortenedURL, short_code=short_code)
    return render(request, 'stats.html', {'link': shortened})