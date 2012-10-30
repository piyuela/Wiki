from django.conf.urls import *

from models import Article

urlpatterns = patterns('',
	url(r' ^$',
		'django.views.generix.list_detail.object_list',
		{
			'queryset': Article.published.all()
		},
		name='wiki_article_index'),
	url(r'^article/(?P<slug>[-\w]+)$',
		'django.views.generic.list_detail.object_detail',
		{
			'queryset': Article.objects.all(),
		},
		name='wiki_article_detail'),
	url(r'^history/(?P<slug>[-\w]+)$',
		'wiki.views/article_history',
		name='wiki_article_history'),
	url(r'^add/articles$',
		'wiki.views.add_article',
		name='wiki_article_add'),
	url(r'^edit/article/(?P<slug>[-\w]+)$',
		'wiki.views.edit_article',
		name='wiki_article_edit'),
)

