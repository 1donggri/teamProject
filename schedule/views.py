from django.shortcuts import render, redirect
from .models import Post
from .forms import ScheduleForm
from django.core.paginator import Paginator

# Create your views here.
def view_schedule(request):
    all_posts = Post.objects.all().order_by('pub_date')
    page = int(request.GET.get('p', 1))
    pagenator = Paginator(all_posts, 5)
    posts = pagenator.get_page(page)
    return render(request, 'schedule/view_schedule.html', {'posts': posts})

def write_schedule(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)

        if form.is_valid():
            # form의 모든 validators 호출 유효성 검증 수행
            # user_id = request.session.get('user')
            # user = User.objects.get(pk=user_id)

            schedule = Post()
            schedule.title = form.cleaned_data['title']
            # # 검증에 성공한 값들은 사전타입으로 제공 (form.cleaned_data)
            # # 검증에 실패시 form.error 에 오류 정보를 저장
            schedule.username = form.cleaned_data['username']
            schedule.pub_date = form.cleaned_data['pub_date']
            schedule.save()

            return redirect('schedule:view_schedule')

    else:
        form = ScheduleForm()

    return render(request, 'schedule/write_schedule.html', {'form': form})

def delete(request, posts_id):
    post = Post.objects.get(id=posts_id)
    post.delete()
    posts = Post.objects.all().order_by('-id')
    return render(request, 'schedule/view_schedule.html', {'posts': posts})