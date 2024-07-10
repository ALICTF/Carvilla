from django.db import models

class Brand(models.Model):
    title = models.CharField(verbose_name='title', max_length=255)
    description = models.TextField()
    # picture = models.ImageField(verbose_name='picture', upload_to='/car/img/%Y/%m/')

    datetime_created = models.DateTimeField(auto_now_add=True, editable=True)
    datatime_modified = models.DateTimeField(auto_now=True, editable=True)
    
    def __str__(self):
        return self.title

class Car(models.Model):
    title = models.CharField(verbose_name='title', max_length=255)
    description = models.TextField(verbose_name='description')
    maker = models.CharField(verbose_name='maker', max_length=200)
    price = models.PositiveIntegerField(verbose_name='price')
    # picture = models.ImageField(verbose_name='picture', upload_to='/car/img/%Y/%m/')
    
    datetime_created = models.DateTimeField(auto_now_add=True, editable=True)
    datatime_modified = models.DateTimeField(auto_now=True, editable=True)
    
    def __str__(self):
        return self.title
