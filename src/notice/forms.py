from django import forms

from notice.models import NoticePost 


class CreateNoticePostForm(forms.ModelForm):

	class Meta:
		model = NoticePost
		fields = ['title', 'body', 'image']