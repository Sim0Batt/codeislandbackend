from django.db import models

class Project(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    titleIt = models.CharField(max_length=255, default="Default title in Italian")
    contentIt = models.TextField(default='Default content in Italian')
    short_descriptionIt = models.TextField(default='Default short in Italian')  # Changed to TextField
    titleEn = models.CharField(max_length=255, default="Default title in English")
    contentEn = models.TextField(default='Default content in English')
    short_descriptionEn = models.TextField(default='Default short in English')  # Changed to TextField
    title_es = models.CharField(max_length=100, null=True, blank=True)
    description_es = models.TextField(null=True, blank=True)
    short_description_es = models.TextField(null=True, blank=True)  # Changed to TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    tech_list = models.JSONField(default=list)

    def __str__(self):
        return self.titleEn




