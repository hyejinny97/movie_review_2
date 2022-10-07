from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review

# Create your views here.
# 목록 페이지
def index(request):
    reviews = Review.objects.all().order_by('-pk')

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/index.html', context)

# 글 작성 페이지 및 데이터 생성
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('reviews:detail', review.pk)
    elif request.method == 'GET':
        form = ReviewForm()

    context = {
        'form': form,
    }

    return render(request, 'reviews/create.html', context)

# 글 상세 페이지
def detail(request, pk):
    return render(request, 'reviews/detail.html')