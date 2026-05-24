import random
import string

def generate_short_code(length=6):
    """Generate a random alphanumeric short code"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def shorten_url(original_url, model_class):
    """Create a shortened URL or return existing one"""
    # Check if this URL already exists
    existing = model_class.objects.filter(original_url=original_url).first()
    if existing:
        return existing.short_code
    
    # Generate unique short code
    while True:
        code = generate_short_code()
        if not model_class.objects.filter(short_code=code).exists():
            break
    
    # Create new record
    shortened = model_class.objects.create(
        original_url=original_url,
        short_code=code
    )
    return code