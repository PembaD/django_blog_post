from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    #one to one relationship, CASCADE: delete the profile if user is deleted BUT not vice-versa
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    #upload_to is the directory the images get uploaded to when profile image is uploaded
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{ self.user.username } Profile'
    
    # *args = positional arguments
    # **kwargs = keyword arguments 
    def save(self): #Corey added * args and **kwargs here but mine does not work with those included
        super().save() #
        
        #resizing images for profile picture
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path) 





