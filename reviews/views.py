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
    review = Review.objects.get(pk=pk)
    context = {
        'review': review,
    }
    return render(request, 'reviews/detail.html', context)

# 글 삭제
def delete(request, pk):
    if request.method == 'POST':
        Review.objects.get(pk=pk).delete()

    return redirect('reviews:index')

# 글 업데이트

def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect('reviews:detail', review.pk)
    elif request.method == 'GET':
        form = ReviewForm(instance=review)
    
    context = {
        'form':form
    }

    return render(request, 'reviews/update.html', context)
