from django.db import models
from django.utils import timezone

class ShortenedURL(models.Model):
    original_url = models.URLField(max_length=2000)
    short_code = models.CharField(max_length=10, unique=True, db_index=True)
    created_at = models.DateTimeField(default=timezone.now)
    click_count = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.short_code} -> {self.original_url[:50]}"
    
    def increment_clicks(self):
        from django.db.models import F
        self.click_count = F('click_count') + 1
        self.save(update_fields=['click_count'])
        self.refresh_from_db()