from django.db import models
from django.contrib.auth.models import User
from django.template.defaltfilters import slugify

#Create you model here.

class PublishedArticlesManager(models.Manager):

	def get_query_set(self):
		return super(PublishedArticlesManager, self).get_query_set().filter(is_published=True)

class Article(model.Model): 

	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=50, unique True)
	text = models.TextField(help_text="Formatted using ReST")
	author = models.ForeignKey(User)
	is_published = models.BooleanField(default= False, verbose_name="Publish?")
	created_on = models.DateTimeField(auto_now_add=True)
	object = models.Manager()
	published = PublishedArticulesManager()

	def _unicode_(self):
		return self.title

	def save(self,*args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Article, self).save(*args, **kwargs)

	@models.permalink
	def get_absolute_url(self):
		return('wiki_articule_detail', (), { ' slug': self.slug})

class Edit(model.Model):

	article = models.ForeignKey(Article)
	editor = models.ForeignKey(User)
	edited_on = models.DateTimeField(auto_now_add=True)
	summary = models.CharField(max_length=100)

	class Meta:
		orderin = ['_edited_on']

	def _unicode_(self):
		return "%s - %s - %s" %(self.summary, self.editor, self.edited_on)

	@models.permalink
	def get_absolute_url(self):
		return ('wiki_edit_detail', self.id)	
