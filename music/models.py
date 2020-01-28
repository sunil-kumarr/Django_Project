from django.db import models

'''
 Django Database API :
 >>> python manage.py shell
 >>> from music.models import Album,Song
 >>> Album.objects.all() => []
  >>>a = Album(artist="taylor swift" ,album_title="Red",genre="Country" ,album_logo="https://random.com")
  >>> a.save()
  >>>a.artist  =>'Taylor swift'
  >>> a.pk => 1
  >>> a.id  => 1
  >>> b = Album()
  >>> b.artist="Myth" >>> b.album_title="high school" >>> b.genre="punk" >>>b.album_logo ="https://"
  >>> b.save() 
  >>> Album.objects.filter(id=1)
  >>> Album.objects.filter(artist__startswith='Taylor')
'''
# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)
    def __str__(self):
        return self.album_title+' -'+self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
