from django.db import models

def tester():
    return "This is a test"

class movie(models.Model):

    moviename=models.CharField(max_length=10)
    movie_id=models.IntegerField()
    response_list=['Star Wars', 'The Empire Strikes Back', "The Fugitive"]
    test = tester()

    def __str__(self):
        return self.moviename
