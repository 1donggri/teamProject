from django.db import models

# Create your models here.
class Board(models.Model):
    author = models.CharField(max_length=100, null=False, verbose_name="작성자")
    title = models.CharField(max_length=100, null=False)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    modified_date = models.DateTimeField(auto_now=True, verbose_name="최종수정일")
    file = models.FileField(null=True, upload_to="")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'boards'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'