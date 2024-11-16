from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['slug'])]

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"category_slug": self.slug})
    
class Celestial(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, related_name='celestial')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    discount = models.DecimalField(max_digits=4, default=0.00, decimal_places=2)
    created =  models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=False)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['id', 'slug']), 
                   models.Index(fields=['name'])]

    def __str__(self):
        return self.name
    
