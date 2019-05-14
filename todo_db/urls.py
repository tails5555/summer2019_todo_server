from django.conf.urls import url
from django.urls import path
from .views import AlertAPIViewSet, CheckAPIViewSet, TodoAPIViewSet

# 작성자 : tails5555(tails5555@naver.com)
# 작성날짜 : 2019/05/14

'''
    todo_db 의 url 는 Main Application 에서 접속하기 위한 URL Router 를 응집한 것입니다.
    각 URL 의 context 별 기능은 아래와 같습니다.

    /todos/ 는 할 일 데이터의 목록 가져오기, 추가 기능
    /todos/<PK>/ 는 할 일 데이터 수정, 삭제 기능
    /alerts/ 는 알림 데이터 가져오는 기능
    /checker/<PK> 는 할 일 완료 여부 수정 기능
'''

urlpatterns = [
    path('todos/', TodoAPIViewSet.as_view()),
    url(r'^todos/(?P<pk>[0-9]+)/$', TodoAPIViewSet.as_view()),
    path('alerts/', AlertAPIViewSet.as_view()),
    url(r'^checker/(?P<pk>[0-9]+)/$', CheckAPIViewSet.as_view())
]