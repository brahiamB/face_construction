from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.shortcuts import reverse




# Create your models here.

class Images(models.Model):
    title = models.CharField(max_length=50)
    job= models.CharField(max_length=256, choices=[('Excavation','Excavation'),('Demolition','Demolition'),
    ('Snow','Snow'), ('Asphalt paving','Asphalt paving'), ('Concrete pavement' , 'Concret pavement'),
    ('Commercila Pavement', 'Commercial Pavement') ])

    
    picture = models.ImageField(upload_to='static/images')
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
     return ('image_detail', (),
          {
             'slug': self.job,
          })

     def save(self, *args, **kwargs):
        if not self.job:
            self.job = slugify(self.title)
            super(Images, self).save(*args, **kwargs)
    
    
        class Meta:
            model = Images
            fields =['title', 'picture']






