from django.shortcuts import render
from .models import News
# Create your views here.
def home(request):
    posts = News.objects.all()
    mid = len(posts) // 2
    try:
        asosiy_news = News.objects.get(id=request.GET.get('news'))  # `news_id` o'zgaruvchisidan foydalanish
    except:
        asosiy_news = posts[0]
    return render(
        request,
        "pages/home.html",
        {
            'news_1': posts[:mid],
            'news_2': posts[mid:],
            'asosiy_news': asosiy_news
        }
    )

def about(request):
    return render(request, "pages/about.html")
from django.shortcuts import render
from .models import News
import datetime

def today(request):
    # Bugungi sana
    today = datetime.date.today()

    # Bugungi yangiliklarni filterlash
    posts = News.objects.filter(created_at__date=today)

    mid = len(posts) // 2
    
    try:
        # GET parametr orqali asosiy yangilikni olish
        asosiy_news = News.objects.get(id=request.GET.get('news'))
    except:
        # Agar yangilik topilmasa yoki GET parametr bo'lmasa, birinchi yangilikni olish
        asosiy_news = posts[0] if posts else None

    return render(
        request,
        "pages/today.html",
        {
            'news_1': posts[:mid],
            'news_2': posts[mid:],
            'asosiy_news': asosiy_news
        }
    )

from django.shortcuts import render
from .models import News
import datetime
from django.utils.timezone import now

def yesterday(request):
    # Bugungi sana
    today = now().date()
    # Kechagi sana
    yesterday = today - datetime.timedelta(days=1)

    # Kechagi yangiliklarni filterlash
    posts = News.objects.filter(created_at__date=yesterday)

    mid = len(posts) // 2
    
    try:
        # GET parametr orqali asosiy yangilikni olish
        asosiy_news = News.objects.get(id=request.GET.get('news'))
    except:
        # Agar yangilik topilmasa yoki GET parametr bo'lmasa, birinchi yangilikni olish
        asosiy_news = posts[0] if posts else None

    return render(
        request,
        "pages/yesterday.html",
        {
            'news_1': posts[:mid],
            'news_2': posts[mid:],
            'asosiy_news': asosiy_news
        }
    )
