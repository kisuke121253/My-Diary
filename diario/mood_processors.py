from django.utils import timezone
from .models import MoodLog

def mood_status(request):
    if not request.user.is_authenticated:
        return {}
    today = timezone.now().date()
    already_submitted = MoodLog.objects.filter(user=request.user, date=today).exists()
    return {'already_submitted': already_submitted}
