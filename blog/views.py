from django.shortcuts import redirect, render
from .models import Post, Tag
from django.db.models import Count
from .services.tag_generator import generate_tags
from django.views import View


# def main(request):
#     posts = Post.objects.select_related('author').prefetch_related('tags', 'likes', 'reposts', 'comments').annotate(likes_count=Count('likes'), reposts_count=Count('reposts'), comments_count=Count('comments')).order_by('-created_at')

#     print(generate_tags("There's nothing quite like driving a powerful sports car on an open road. The sound of the engine, the smooth acceleration, and the beautiful design make every journey exciting. For car lovers, it's not just about transportation; it's about passion, freedom, and performance. 🏎️🔥"))  # Example usage of the generate_tags function

#     context = {
#         'posts': posts,
#     }
#     return render(request, 'blog/main.html', context)


class MainView(View):
    def get(self, request):
        posts = Post.objects.filter(author=request.user).select_related('author').prefetch_related('tags', 'likes', 'reposts', 'comments').annotate(likes_count=Count('likes'), reposts_count=Count('reposts'), comments_count=Count('comments')).order_by('-created_at')
        context = {
            'posts': posts,
            'posts_count': posts.count(), 
            'user_following': request.user.following.count(),
            'user_followers': request.user.followers.count(),
        }
        return render(request, 'blog/main.html', context)

    def post(self, request):
        content = request.POST.get('content', '').strip()
        if content:
            print("Creating new post")
            new_post = Post.objects.create(content=content, author=request.user)
            tags = generate_tags(content)
            for tag_name in tags:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                new_post.tags.add(tag)
            new_post.save()
        return redirect('main')
    