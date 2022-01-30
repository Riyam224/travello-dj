from django.db import models

# Create your models here.

from django.utils.translation import gettext as _
from django.utils.text import slugify

class Destination(models.Model):
    name = models.CharField(_("name"), max_length=50)
    desc = models.TextField(_("description") , max_length=150)
    image = models.ImageField(_("image"), upload_to='images')
    price = models.DecimalField(_("price"), max_digits=5, decimal_places=2)
    offer = models.BooleanField(_("offer") , default=False)
    slug = models.SlugField(max_length=255, unique=True  , blank=True, null=True)

    

    class Meta:
        verbose_name = _("Destination")
        verbose_name_plural = _("Destinations")

    def __str__(self):
        return self.name

        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Destination, self).save(*args, **kwargs)


    
    
