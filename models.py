from django.db import models

# Create your models here.

class Horario(models.Model):
    numero=models.IntegerField()

    def __str__(self):
        return f"Horario{self.numero}"


class Aula(models.Model):
    materia=models.CharField(max_length=64)
    vagas=models.IntegerField()
    horario=models.ForeignKey(Horario,on_delete=models.CASCADE,related_name="aulas",null=True,blank=True)

    def __str__(self):
        return f"{self.materia}"

class Aluno(models.Model):
    first=models.CharField(max_length=64)
    last=models.CharField(max_length=64)
    aulas=models.ManyToManyField(Aula,blank=True,related_name="alunos")

    def __str__(self):
        return f"{self.first} {self.last}"


class Sala(models.Model):
    localizacao=models.IntegerField()
    aulas=models.ManyToManyField(Aula,blank=True,related_name="localizacao")

    def __str__(self):
        return f"Sala {self.localizacao}"

