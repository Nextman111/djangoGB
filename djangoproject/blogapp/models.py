from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField(max_length=500)
    birthday = models.DateField()

    def fullname(self):
        return f'{self.name} {self.fullname()}'

    def __str__(self):
        return f'{self.pk}: {self.name} {self.fullname()}'


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    published_date = models.DateField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk}: Author {self.author.name}. Title - {self.title}'
