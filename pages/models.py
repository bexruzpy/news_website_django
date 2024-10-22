from django.db import models



class News(models.Model):
    title = models.CharField(max_length=200)  # Post sarlavhasi
    content = models.TextField()  # Post mazmuni
    created_at = models.DateTimeField(auto_now_add=True)  # Post yaratilgan vaqt
    updated_at = models.DateTimeField(auto_now=True)  # Post yangilangan vaqt

