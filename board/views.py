from django.shortcuts import render, redirect
from .forms import BoardForm
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    pagenator = Paginator(all_boards, 5)
    boards = pagenator.get_page(page)
    return render(request, 'board/list.html', {"boards": boards})

def post(request):
    if request.method == "POST":
        form = BoardForm(request.POST, request.FILES)

        if form.is_valid():
            # form의 모든 validators 호출 유효성 검증 수행
            # user_id = request.session.get('user')
            # user = User.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            # # 검증에 성공한 값들은 사전타입으로 제공 (form.cleaned_data)
            # # 검증에 실패시 form.error 에 오류 정보를 저장
            board.author = form.cleaned_data['name']
            board.file = form.cleaned_data['file']
            board.save()

            return redirect('board:list')

    else:
        form = BoardForm()

    return render(request, 'board/post.html', {'form': form})

def delete(request, board_id):
    board = Board.objects.get(id=board_id)
    board.delete()
    boards = Board.objects.all().order_by('-id')
    return render(request, 'board/list.html', {'boards': boards})
