# Generated by Django 3.2.2 on 2021-06-16 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'verbose_name': '게시판', 'verbose_name_plural': '게시판'},
        ),
        migrations.AlterField(
            model_name='board',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
        migrations.AlterField(
            model_name='board',
            name='content',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='board',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='작성일'),
        ),
        migrations.AlterField(
            model_name='board',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='최종수정일'),
        ),
        migrations.AlterModelTable(
            name='board',
            table='boards',
        ),
    ]