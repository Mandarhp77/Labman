from django.db import models

class Books(models.Model):
    name        = models.CharField(max_length=100)
    book_writer = models.CharField(max_length=100)
    booktype    = models.CharField(max_length=100)
    update_date = models.DateField()
    price       = models.IntegerField()
    availabality= models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "books"
