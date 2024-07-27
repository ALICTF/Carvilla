from django.db import models


# Order by datetime
class OrderByDateTime(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-datetime_created')


class Brand(models.Model):
    title = models.CharField(verbose_name='title', max_length=255)
    description = models.TextField()
    # picture = models.ImageField(verbose_name='picture', upload_to='/car/img/%Y/%m/')

    datetime_created = models.DateTimeField(auto_now_add=True)
    datatime_modified = models.DateTimeField(auto_now=True)

    objects = OrderByDateTime()
    
    def __str__(self):
        return self.title


class Car(models.Model):
    title = models.CharField(verbose_name='title', max_length=255)
    description = models.TextField(verbose_name='description')
    maker = models.CharField(verbose_name='maker', max_length=200)
    price = models.PositiveIntegerField(verbose_name='price')
    # picture = models.ImageField(verbose_name='picture', upload_to='/car/img/%Y/%m/')
    
    datetime_created = models.DateTimeField(auto_now_add=True)
    datatime_modified = models.DateTimeField(auto_now=True)

    objects = OrderByDateTime()
    
    def __str__(self):
        return self.title
