from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    body = models.TextField()

    def __str__(self):
        return self.title

#클래스 만들고 makemigrations, migrate -> 데이터 전송
#데이터 보내고 Admin 생성
#Admin.py, Views.py 클래스(Model) 등록
    