from django.db import models

class StatusModel(models.Model) :
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class JobTitle(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.ForeignKey(StatusModel,
                               related_name = 'status_status_model',
                               blank = True, null = True,
                               on_delete= models.SET_NULL)



class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete= models.CASCADE)

    def __str__(self):
        return self.title
    

class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    authors = models.ManyToManyField(Author, related_name= 'book_author')

    def __str__(self):
        return self.title
    
class Vihicle(models.Model):
    reg_no = models.IntegerField()
    owner = models.CharField(max_length=100)

    def __str__(self):
        return str(self.reg_no)
    
class Car(models.Model):
    vihicle = models.OneToOneField(Vihicle, on_delete=models.CASCADE, primary_key= True)
    car_model = models.CharField(max_length=100)

    def __str__(self):
        return str(self.vihicle)