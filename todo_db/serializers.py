from rest_framework import serializers
from .models import TodoElement

# 작성자 : tails5555(tails5555@naver.com)
# 작성날짜 : 2019/05/14

'''
    TodoElementSerializer 는 TodoElement 모델을 JSON, XML 등으로 변환할 수 있게 도와줍니다.
    REST API 로 이와 같은 포맷으로 되어 있는 data 를 보내거나 받을 때 이를 사용해야 합니다.
    
    - Meta 클래스
        
        django Model 를 직렬화 할 수 있게 설정하는 Inner 클래스 입니다.
        
        * model 은 django 모델 클래스를 작성합니다.
        * fields 는 XML, JSON 에서 보여줄 Field 들을 작성합니다.
        * extra_kwargs 는 Field 중에 특별한 설정이 필요할 때 사용합니다.
'''

class TodoElementSerializer(serializers.ModelSerializer) :
    class Meta :
        model = TodoElement
        fields = ('id', 'title', 'description', 'priority', 'completed', 'deadline', 'created', 'modified', )