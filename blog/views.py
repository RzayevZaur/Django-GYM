from django.shortcuts import render, get_object_or_404
from .models import Category, Tag, Post,Paraqraf

def Blog(request):
    Post_views = Post.objects.all()[:3]
    Category_views = Category.objects.all()
    Tag_views = Tag.objects.all()

    Context = {
        "Post_views": Post_views,
        "Category_views": Category_views,
        "Tag_views": Tag_views,
    }
    return render(request, "blog.html", context=Context)



def Blog_details(request, slug):
    paraqraf = Paraqraf.objects.all()
    recent_posts = Post.objects.all()[:3]  
    blogdetails = get_object_or_404(Post, slug=slug)
    blog_details_views = Post.objects.all()
    Context = {
        "blogdetails": blogdetails,
        "blog_details_views": blog_details_views,
        'recent_posts': recent_posts,
        'paraqraf':paraqraf

    }
    return render(request, "blog-details.html", context=Context)