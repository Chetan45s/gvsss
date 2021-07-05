import sys
from django.db import models
from django.utils.timezone import now
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from datetime import date

from django.conf import settings

User = settings.AUTH_USER_MODEL

class_choices = (
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
)

class about(models.Model):
    intro = models.TextField(default="", null=True, blank=True)
    images = models.ImageField(upload_to='media', default="", null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.images = self.compressImage(self.images)
        super(about, self).save(*args, **kwargs)

    def compressImage(self,images):
        imageTemproary = Image.open(images)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        images = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % images.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return images

    def __str__(self):
        return self.intro

class director(models.Model):
    name = models.CharField(max_length=500,default="")
    text = models.TextField(default="")
    designation = models.CharField(max_length=500,default="")
    images = models.ImageField(upload_to='media', default="")

    def save(self, *args, **kwargs):
        if not self.id:
            self.images = self.compressImage(self.images)
        super(director, self).save(*args, **kwargs)

    def compressImage(self,images):
        imageTemproary = Image.open(images)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        images = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % images.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return images

class img_slider(models.Model):
    images = models.ImageField(upload_to='gallery', default="")
    caption = models.CharField(max_length=500,default="", null=True, blank=True)
    pub_date = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.images = self.compressImage(self.images)
        super(img_slider, self).save(*args, **kwargs)

    def compressImage(self,images):
        imageTemproary = Image.open(images)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        imageTemproary.save(outputIoStream , format='JPEG', quality=70)
        outputIoStream.seek(0)
        images = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % images.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return images

    class Meta:
        ordering = ['-pub_date',]

class staff(models.Model):
    name = models.CharField(max_length=500,default="")
    designation = models.CharField(max_length=1000,default="")
    contact = models.CharField(max_length=1500,default="", null=True, blank=True)

    def __str__(self):
        return self.name

class faq(models.Model):
    question = models.TextField(default="")
    answer = models.TextField(default="")

    def __str__(self):
        return self.question

class feedback(models.Model):
    name = models.CharField(max_length=500,default="")
    email = models.CharField(max_length=1000,default="")
    subject = models.CharField(max_length=1500,default="")
    message = models.TextField(default="")
    posting_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class guideline(models.Model):
    text = models.TextField(default="")

    def __str__(self):
        return self.text

class announcement(models.Model):
    text = models.TextField(default="")
    image = models.ImageField(upload_to='media', default="", null=True, blank=True)
    file = models.FileField(upload_to='files', default="", null=True, blank=True)
    pub_date = models.DateField(default=now)
    time = models.TimeField(default=now)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-pub_date','-time']

class gallery(models.Model):
    images = models.ImageField(upload_to='gallery', default="")
    caption = models.CharField(max_length=500,default="", null=True, blank=True)
    pub_date = models.DateTimeField(default=now)

    class Meta:
        ordering = ['-pub_date',]

    def save(self, *args, **kwargs):
        if not self.id:
            self.images = self.compressImage(self.images)
        super(gallery, self).save(*args, **kwargs)

    def compressImage(self,images):
        imageTemproary = Image.open(images)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        imageTemproary.save(outputIoStream , format='JPEG', quality=50)
        outputIoStream.seek(0)
        images = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % images.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return images

class event(models.Model):
    title = models.CharField(max_length=1500,default="")
    description = models.TextField(default="",null=True, blank=True)
    venue = models.CharField(max_length=5000,default="")
    eventdate = models.DateField()
    time = models.TimeField( default="", null=True, blank=True)

    def __str__(self):
        return self.title

    def month(self):
        return self.eventdate.strftime('%b')

    def year(self):
        return self.eventdate.strftime('%Y')

    def dateday(self):
        return self.eventdate.strftime("%d")

    class Meta:
        ordering = ['-eventdate','time']

class Student(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=500,null=True,blank=True)
    last_name = models.CharField(max_length=500,null=True,blank=True)
    roll_no = models.CharField(max_length=500,null=True,blank=True)
    gender = models.CharField(max_length=500,null=True,blank=True)
    date_of_birth = models.CharField(max_length=500,null=True,blank=True)
    phone = models.CharField(max_length=500,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    father_name = models.CharField(max_length=500,null=True,blank=True)
    mother_name = models.CharField(max_length=500,null=True,blank=True)
    class_name = models.CharField(max_length=500,choices=class_choices,null=True,blank=True)
    profile_pic = models.ImageField(upload_to="student_profile_pics",null=True,blank=True)
    bio = models.CharField(max_length=500,null=True,blank=True)

    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    def __str__(self):
        return f"{self.user}"

class Teacher(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=500,null=True,blank=True)
    last_name = models.CharField(max_length=500,null=True,blank=True)
    gender = models.CharField(max_length=500,null=True,blank=True)
    phone = models.CharField(max_length=500,null=True,blank=True)
    class_name = models.CharField(max_length=500,choices=class_choices,null=True,blank=True)

    def __str__(self):
        return f"{self.user}"

class ClassLink(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_and_time = models.CharField(max_length=500,null=True,blank=True)
    topic = models.CharField(max_length=500,null=True,blank=True)
    link = models.CharField(max_length=500,null=True,blank=True)
    class_name = models.CharField(max_length=500,choices=class_choices,null=True,blank=True)
    subject =  models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return f"{self.user}"
    
    