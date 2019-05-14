from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

# 작성자 : tails5555(tails5555@naver.com)
# 작성날짜 : 2019/05/14

'''
    Main Application 에서 접속하는 URL 이 /api/ 로 시작하면 todo_db 에 있는 기능들을 실행하는 URL Router 를 연동할 수 있습니다. 
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include('todo_db.urls')),
]
