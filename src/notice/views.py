from django.shortcuts import render, redirect

from notice.models import NoticePost
from notice.forms import CreateNoticePostForm
from account.models import Account


def create_notice_view(request):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	form = CreateNoticePostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=request.user.email).first()
		obj.author = author
		obj.save()
		form = CreateNoticePostForm()

	context['form'] = form

	return render(request, 'notice/create_notice.html', context)