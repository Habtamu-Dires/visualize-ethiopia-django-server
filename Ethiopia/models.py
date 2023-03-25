from django.db import models
from cloudinary.models import CloudinaryField
import os
import uuid
from django.core.exceptions import ValidationError


#local image path
local_path = "Ethiopia/templates/Ethiopia"

# Create your models here.
def content_file_name(instance, filename):
    path = local_path
    ext = str(filename).split('.')[-1]
    #if(ext != 'html'):
    #    raise ValidationError('Shouold be html file')
    filename = "%s.%s" % (instance.id, ext)
    return os.path.join(path, filename)

def set_public_id(instance):
    return str(instance.id)


class Element(models.Model):
    file_choice = [
        ('image', 'Image'),
        ('html', 'HTML')
    ] 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    source_name = models.CharField(max_length=100)
    source_url = models.CharField(max_length=300, blank=True)  
    file_type = models.CharField(max_length=9, choices=file_choice, default='image')
    html = models.FileField(upload_to=content_file_name, blank=True, null=True)
    image = CloudinaryField('image', folder = "visualize-ethiopia",public_id=set_public_id, blank=True, null=True)
    
    #validation
    def clean(self):    
        if(self.file_type == 'image'):
            if(self.image == None):
                raise ValidationError({
                    'image': ValidationError('No file selected', code='required')
                })
            
            valid_img_types = ['png', 'jpg', 'jpeg', 'gif', 'svg', 'webp', 'bmp','pdf']
            ext = str(self.image).split('.')[-1]
            if(ext.lower() not in valid_img_types):
                raise ValidationError({
                    'image': ValidationError('Image format not supported',code='invalid')
                })
        
        if(self.file_type=='html'):
            if(self.html == None):
               raise ValidationError({
                    'html': ValidationError('No file selected', code='required')
                }) 
            
            ext = str(self.html).split('.')[-1]
            if(ext != 'html'):
                raise ValidationError({
                    'html': ValidationError('Not html file', code='invalid')
                })
        return super().clean()    


    def __str__(self):
        return self.title
    
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "source_name": self.source_name,
            "source_url": self.source_url,
            "file_type": self.file_type,
        } 


           
        




            
           





   
    
