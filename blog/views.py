from django.shortcuts import redirect, render
from .models import Post, Tag
from django.db.models import Count
from .services.tag_generator import generate_tags
from django.views import View
from .forms import PostForm
import logging


logger = logging.getLogger(__name__)


# def main(request):
#     posts = Post.objects.select_related('author').prefetch_related('tags', 'likes', 'reposts', 'comments').annotate(likes_count=Count('likes'), reposts_count=Count('reposts'), comments_count=Count('comments')).order_by('-created_at')

#     print(generate_tags("There's nothing quite like driving a powerful sports car on an open road. The sound of the engine, the smooth acceleration, and the beautiful design make every journey exciting. For car lovers, it's not just about transportation; it's about passion, freedom, and performance. 🏎️🔥"))  # Example usage of the generate_tags function

#     context = {
#         'posts': posts,
#     }
#     return render(request, 'blog/main.html', context)


class MainView(View):
    def get_context(self, request):
        create_post_form = PostForm()
        posts = Post.objects.filter(author=request.user).select_related('author').prefetch_related('tags', 'likes', 'reposts', 'comments').annotate(likes_count=Count('likes'), reposts_count=Count('reposts'), comments_count=Count('comments')).order_by('-created_at')
        context = {
            'posts': posts,
            'posts_count': posts.count(), 
            'user_following': request.user.following.count(),
            'user_followers': request.user.followers.count(),
            'create_post_form': create_post_form
        }
        return context


    def get(self, request):
        context = self.get_context(request)
        return render(request, 'blog/main.html', context)


    def post(self, request):
        # content = request.POST.get('content').strip()
        if 'create_post' in request.POST:
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()

                try:
                    gen_tags = generate_tags(post.content)
                    if gen_tags:
                        tags = [Tag.objects.get_or_create(name=name)[0] for name in gen_tags]
                        post.tags.add(*tags)
                    post.tags_generated = True
                    post.save(update_fields=['tags_generated'])
                except Exception:
                    logger.exception(
                        "Failed to regenerate tags for post %s",
                        post.pk
                    )
                return redirect('main')

            context = self.get_context(request)
            context['create_post_form'] = form

            return render(request, 'blog/main.html', context)
        return redirect('main')
      
    