from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from .forms import movieform
# Create your views here.
def index(request):
    movie1=movie.objects.all()
    context={
        'movie_list':movie1
    }
    return  render(request,"index.html",context)
def detail(request,movie_id):
    Movie=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':Movie})
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        des = request.POST.get('des', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        movie1=movie(name=name,des=des,year=year,img=img)
        movie1.save()

    return render(request,'add.html')

def update(request,id):
    Movie=movie.objects.get(id=id)
    form=movieform(request.POST or None, request.FILES,instance=Movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':Movie})
def delete(request,id):
    if request.method=='POST':
        Movie = movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request,'delete.html')


