import uuid
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Tag Name')
    slug = models.SlugField(unique=True, verbose_name='Tag Slug')


    def __str__(self):
        return f'#{self.name}'


    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField(verbose_name='Post Content')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    tags = models.ManyToManyField(Tag, related_name='posts', verbose_name='Tags')
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True, verbose_name='Likes')

    original_post = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='quotes', verbose_name='Original Post')
    reposts = models.ManyToManyField(User, related_name='reposted_posts', blank=True, verbose_name='Reposts')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')


    def __str__(self):
        return f'Post by {self.author.username} at {self.created_at} - {self.id}'


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Post')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    content = models.TextField(max_length=1000, verbose_name='Comment Content')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies', verbose_name='Parent Comment')
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True, verbose_name='Likes')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')


    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['created_at']