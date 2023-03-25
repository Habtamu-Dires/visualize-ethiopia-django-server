import os
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Element
from .forms import ElementForm
import cloudinary

#remove the group
admin.site.unregister(Group)

#local image path
local_path = "Ethiopia/templates/Ethiopia"

class ElementAdmin(admin.ModelAdmin):
    fieldsets =(
        ('Element', {
            'fields': ('title', 'description', 'source_name', 'source_url', 'file_type',),
            'classes': ('predefined',)
        }),
        (None, {
            'fields': (('html',)),
             'classes': ('abcdefg',)
        }),(None,{
            'fields':(('image',)),
            'classes': ('uvwxyz',)
        })
    )
    form = ElementForm

    class Media:
        js = ('static_jquery/js/jquery.js', 'Ethiopia/image_html_selection.js', )

    def save_model(self, request, obj, form, chnage):

        # during upate get ride of old files.
        if obj.file_type == 'html':
            filename = "%s.%s" % (obj.id, 'html')
            old_file = local_path + '/' + filename
            if(obj.html != old_file):  #that means it is new
                try:
                    os.remove(os.path.join(local_path, filename))
                except:
                    print('error')    
        elif obj.file_type == 'image':
            #no need to delete since they have the dame public_id 
            #cloudinary will replace it.
            pass

        super().save_model(request, obj, form, chnage)
    

    def delete_model(self, request, obj):
        if (obj.file_type == 'html'):
            filename = "%s.%s" % (obj.id, 'html')
            os.remove(os.path.join(local_path, filename))
            obj.delete()
        elif (obj.file_type == 'image'):
            public_id = str(obj.image.public_id)
            print(public_id)
            result = cloudinary.uploader.destroy(public_id)
            print(result)
            obj.delete()
                    
    def delete_queryset(self, request, queryset):
       for obj in queryset:
           if (obj.file_type == 'html'):
                filename = "%s.%s" % (obj.id, 'html')
                os.remove(os.path.join(local_path, filename))
                obj.delete()
           elif (obj.file_type == 'image'):
                print("we are on image delet")
                public_id = obj.image.public_id 
                result = cloudinary.uploader.destroy(public_id)
                print(result)
                obj.delete()
    

# Register your models here.
admin.site.register(Element, ElementAdmin)



