from django.shortcuts import render
from operator import attrgetter
from notice.models import NoticePost

def home_screen_view(request):
	
	context = {}
	notice_posts = sorted(NoticePost.objects.all(), key=attrgetter('date_updated'), reverse=True)
	context['notice_posts'] = notice_posts

	return render(request, "personal/home.html", context)