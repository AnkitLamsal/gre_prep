from django.db import models

connotation_choices = [
    ('positive', 'Positive'),
    ('negative', 'Negative'),
    ('neutral', 'Neutral')
]

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=100)
    meaning = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Word(models.Model):
    name = models.CharField(max_length=100)
    connotation = models.CharField(max_length=100, choices=connotation_choices)
    definition = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return self.name

class WordFamily(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

    def _str__(self) -> str:
        return f'{self.family.name} - {self.word.name}'
