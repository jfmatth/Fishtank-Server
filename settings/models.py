from django.db import models

class setting(models.Model):
    master  = models.BooleanField(blank=True, default=False)             

    name = models.CharField(max_length=20)
    value = models.TextField(blank=True)
    
    def __unicode__(self):
        return "%s:%s" % (self.name,self.value)

