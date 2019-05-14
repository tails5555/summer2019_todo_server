from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import TodoElement
from .serializers import TodoElementSerializer

# 작성자 : tails5555(tails5555@naver.com)
# 작성날짜 : 2019/05/14

'''
    AlertAPIViewSet 는 할 일 데이터 목록을 보여주기 이전에 비동기 호출하여 보여주는 알림 전용 API View 입니다.
    * 할 일 목록 중 기한이 지난 데이터가 있으면 자동으로 완료 처리하고 반환합니다.
    * 위의 해당사항이 없으면 알림창이 안 나오게끔 React 에서 처리합니다.
    * 알림 데이터만 가져오기 때문에 get 메소드만 작성했습니다.

    - get 메소드 (/alerts/)
        알림창에 실릴 데이터입니다.
        반환하는 alert_message 는 알림창의 내용입니다.
        titles 는 기한이 이미 지난 할 일들의 제목입니다.
'''

class AlertAPIViewSet(APIView) :
    def get(self, request, format=None) :
        todos = TodoElement.objects.filter(deadline__lte=datetime.now())
        if len(todos) > 0 :
            titles = []
            for todo in todos :
                titles.append(todo.title)
                todo.completed = True
                todo.save()
            return Response(status=200, data={ 
                'alert_message' : '아래 할 일 목록은 마감 기간이 지나 자동으로 완료 처리했습니다.',
                'titles' : titles
            })
        else :
            return Response(status=200, data={ 
                'alert_message' : '현재까지 마감 시간이 지난 할 일이 없습니다.',
                'titles' : []
            })

'''
    CheckAPIViewSet 는 할 일 중 하나를 체크하기 위한 API View 입니다.
    * 데이터 일부만 변경하기 때문에 put 메소드만 작성했습니다.

    - put 메소드 (/checker/<pk>/)
        할 일 데이터의 완료 여부를 수정하는 메소드입니다.
        할 일 데이터가 존재하지 않으면 404 Status 를 반환했습니다.
'''

class CheckAPIViewSet(APIView) :
    def put(self, request, pk, format=None) :
        try:
            todo = TodoElement.objects.get(id=pk)
        except TodoElement.DoesNotExist :
            return Response(status=404, data={ 'message' : '할 일 데이터가 존재하지 않습니다. 다시 시도하세요.' })
        else :    
            todo.completed = not todo.completed
            todo.save()
            return Response(status=200, data={ 'todo_element' : TodoElementSerializer(instance=todo).data })

'''
    TodoAPIViewSet 는 할 일 데이터를 관리하는 API View 입니다.
    * CRUD 과정이 이뤄지기 때문에 get, post, put, delete 메소드를 작성했습니다.
    * get 메소드 중 단일 데이터를 가져올 일이 없어서 작성하지 않았습니다.
    * 정상 처리 중 GET, PUT, DELETE 가 200 상태를 반환하고, POSt 는 201 를 반환합니다.
    * Form Validation 에러는 400 에러를 반환했습니다.
    * 마찬가지로 할 일 데이터가 존재하지 않으면 404 Status 를 반환했습니다.

    - get 메소드 (/todos/)
        할 일 목록을 전부 가져오는 메소드입니다.
        우선순위가 큰 것을 1번째, 등록 순서를 2번째로 역정렬 처리했습니다.

    - post 메소드 (/todos/)
        할 일을 추가하는 메소드입니다.

    - put 메소드 (/todos/<pk>/)
        할 일을 수정하는 메소드입니다.
    
    - delete 메소드 (/todos/<pk>/)
        할 일을 삭제하는 메소드입니다.
'''

class TodoAPIViewSet(APIView) :    
    def get(self, request, format=None) :
        todos = TodoElement.objects.all().order_by('-priority', '-pk')
        serializer = TodoElementSerializer(todos, many=True)
        return Response(status=200, data={ 'todo_list' : serializer.data })

    def post(self, request, format=None) :
        form = request.data.get('todo_form')
        serializer = TodoElementSerializer(data=form)
        
        if serializer.is_valid(raise_exception=True):
            success_data = serializer.save()
            return Response(status=201, data={ 'message' : '할 일({})이 추가 되었습니다.'.format(success_data.title) })
        else :
            return Response(status=400, data=serializer.errors)

    def put(self, request, pk, format=None) :
        try:
            todo = TodoElement.objects.get(id=pk)
        except TodoElement.DoesNotExist :
            return Response(status=404, data={ 'message' : '할 일 데이터가 존재하지 않습니다. 다시 시도하세요.' })
        else :
            form = request.data.get('todo_form')
            serializer = TodoElementSerializer(data=form, instance=todo)
            
            if serializer.is_valid(raise_exception=True):
                success_data = serializer.save()
                return Response(status=200, data={ 'message' : '할 일({})이 수정 되었습니다.'.format(todo.title) })
            else :
                return Response(status=400, data=serializer.errors)

    def delete(self, request, pk, format=None) :
        try:
            todo = TodoElement.objects.get(id=pk)
        except TodoElement.DoesNotExist:
            return Response(status=404, data={ 'message' : '할 일 데이터가 존재하지 않습니다. 다시 시도하세요.' })    
        else :
            todo.delete()
            return Response(status=200, data={ 'message' : '할 일({})이 삭제 되었습니다.'.format(todo.title) })