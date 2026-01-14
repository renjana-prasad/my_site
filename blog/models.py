from django.db import models
from django.utils.text import slugify

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['caption'], name='unique_tags')
        ]

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(unique=True)
    best_film = models.ForeignKey("Posts", on_delete=models.SET_NULL,null=True,blank=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.full_name()
    
    class Meta:
        verbose_name_plural = "Director Details"
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name', 'email_address'], name='unique_details')
        ]



class Posts(models.Model):
    title = models.CharField(max_length=80)
    image = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True, db_index=True)
    release_date = models.DateField()
    directed_by = models.ForeignKey(Director, on_delete=models.SET_NULL,null=True, related_name='posts')
    summary = models.CharField(max_length=120)
    content = models.TextField(max_length=4000)
    tag = models.ManyToManyField(Tag)
    favourite = models.BooleanField(default=False)

    def tag_names(self):
        return [tag.caption for tag in self.tag.all()]   
    
    def save(self, *args, **kwargs):
        # Save first if new object to get an ID
        creating = self.pk is None
        super().save(*args, **kwargs)
        
        if creating:
            # Set slug after ID is generated
            self.slug = f"{self.id}-{slugify(self.title)}"
            # Update only the slug field to avoid re-inserting
            Posts.objects.filter(id=self.id).update(slug=self.slug)

    class Meta:
        verbose_name_plural = "Post Details"