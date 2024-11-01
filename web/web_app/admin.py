from django.contrib import admin
# from web_app.models import StatusModel, GeeksModel, Album, Song, Author, Book
from web_app.models import StatusModel, Album, Song, Author, Book, Vihicle, Car

admin.site.register(StatusModel)
# admin.site.register(GeeksModel)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Vihicle)
admin.site.register(Car)
