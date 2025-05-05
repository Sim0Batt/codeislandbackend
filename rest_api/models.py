from django.db import models

class Project(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    titleIt = models.CharField(max_length=255, blank=True, null=True)
    contentIt = models.TextField(blank=True, null=True)
    short_descriptionIt = models.TextField(blank=True, null=True) 
    titleEn = models.CharField(max_length=255, blank=True, null=True)
    contentEn = models.TextField(blank=True, null=True)
    short_descriptionEn = models.TextField(blank=True, null=True)  
    title_es = models.CharField(max_length=255, blank=True, null=True)
    description_es = models.TextField(blank=True, null=True)
    short_description_es = models.TextField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    tech_list = models.JSONField(default=list, blank=True, null=True)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.titleEn

class HomePageTxts(models.Model):
    about_text_it = models.TextField(default='Default about text in Italian')
    about_text_en = models.TextField(default='Default about text in English')
    about_text_es = models.TextField(default='Default about text in Spanish')
    tech_text_it = models.TextField(default='Default tech text in Italian')
    tech_text_en = models.TextField(default='Default tech text in English')
    tech_text_es = models.TextField(default='Default tech text in Spanish')
    partners_text_it = models.TextField(default='Default partners text in Italian')
    partners_text_en = models.TextField(default='Default partners text in English')
    partners_text_es = models.TextField(default='Default partners text in Spanish')



