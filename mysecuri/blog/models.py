import datetime

from django.db import models
from django.contrib.auth.models import User
from markdown import markdown
from tagging.fields import TagField
from django.core.urlresolvers import reverse


class Category(models.Model):
    description = models.TextField()

    slug = models.SlugField(unique=True,
                            help_text="Suggested value automatically generated from title.\
                            Must be unique.")
    title = models.CharField(max_length=250,
                             help_text='Maximum 250 characters.')

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"

    class Admin:
        pass

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/categories/%s/" % self.slug


class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (1, 'Live'),
        (2, 'Draft'),
        (3, 'Hidden'),
    )

    title = models.CharField(max_length=250,
                             help_text="Maximum 250 characters.")
    excerpt = models.TextField(blank=True,
                               help_text="A short summary of the entry. Optional.")
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    # Fields to store generated HTML.
    body_html = models.TextField(editable=False, blank=True)
    excerpt_html = models.TextField(editable=False, blank=True)

    # Metadata
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(help_text="Suggested value automatically generated from title.")

    status = models.IntegerField(choices=STATUS_CHOICES,
                                 default=LIVE_STATUS,
                                 help_text="Only entries with 'Live' status will be\
                                           publicly displayed.")

     # Categorization
    categories = models.ManyToManyField(Category)
    tags = TagField(help_text="Separate tags with spaces.")

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "Entries"

    class Admin:
        pass

    def __unicode__(self):
        return self.title

    def save(self):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save()

    @models.permalink
    def get_absolute_url(self):
        return reverse('entry-detail', kwargs={'pk': self.pk})
