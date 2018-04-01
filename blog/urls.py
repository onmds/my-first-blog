from django.conf.urls import url
from . import views

# 뷰가 보이게 url 생성(url을 만들어 장고가 뷰로 보내 게시글이 보일수 있게)
# -> post 상세 페이지 내 뷰 추가 
urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/upload/$', views.upload_file, name='upload'),
	]