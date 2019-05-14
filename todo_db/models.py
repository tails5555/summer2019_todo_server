from django.db import models

# 작성자 : tails5555(tails5555@naver.com)
# 작성날짜 : 2019/05/14

'''
    TodoElement 는 해야 할 일들 중 하나를 저장하기 위한 Model 데이터입니다.
        
    - id
        TODO 데이터의 Primary Key 입니다.
        Auto Increment 로 자동 증가하고, TODO 데이터 수정, 삭제, 단일 조회 기능을 위해 사용합니다.
    
    - title
        TODO 의 제목입니다. 127 글자 문자를 사용합니다.
    
    - description
        TODO 의 설명문입니다. Text 필드를 사용합니다.

    - priority
        TODO 의 우선 순위입니다. 1 글자 문자를 사용합니다.
        수치가 높을수록 중요합니다.
    
    - completed
        TODO 의 완료 여부입니다. Boolean 를 사용합니다.

    - deadline
        TODO 의 마감 기한입니다. DateTime 을 사용합니다.
        이는 빈 값으로 저장할 수 있습니다. 
    
    - created
        TODO 의 생성 기간입니다. DateTime 을 사용합니다.
        최초로 생성된 이후에만 UI 에 보입니다.

    - modified
        TODO 의 수정 기간입니다. DateTime 을 사용합니다.
        수정 이후에는 created 데이터는 null 로 바뀌고, 수정 기한만 UI 에 보입니다.
'''

class TodoElement(models.Model) :
    
    # TODO 데이터 별 중요도 설정을 위해 사용하는 ENUM 데이터 입니다.
    PRIORITY_CHOICES = (
        ('5', '위급')
        ('4', '긴급'),
        ('3', '평범'),
        ('2', '여유'),
        ('1', '사소')
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=127, null=False)
    description = models.TextField(null=False)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, null=False)
    completed = models.BooleanField(null=False, default=False)
    deadline = models.DateTimeField(null=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)