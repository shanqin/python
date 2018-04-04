from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name
		
@python_2_unicode_compatible		
class Tag(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name
		
@python_2_unicode_compatible		
class Post(models.Model):
	#标题
	title = models.CharField(max_length=70)
	#正文
	body = models.TextField()
	#创建时间，最后修改时间
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	#文章摘要
	excerpt = models.CharField(max_length=200,blank=True)
	#分类与标签，定义在上方
	category = models.ForeignKey(Category)
	tag = models.ManyToManyField(Tag,blank=True)
	#作者
	author = models.ForeignKey(User)
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk':self.pk})
	class Meta:
		ordering = ['-created_time']
# Create your models here.
