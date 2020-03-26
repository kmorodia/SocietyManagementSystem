from django.urls import path
from notice.views import (
	create_notice_view,
	detail_notice_view,
)

app_name = 'notice'

urlpatterns = [
    path('create/', create_notice_view, name="create"),
    path('<slug>/', detail_notice_view, name="detail"),
]