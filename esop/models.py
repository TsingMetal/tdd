from django.db import models


class Department(models.Model):
    
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Line(models.Model):

    department = models.ForeignKey(Department)
    line_no = models.CharField(max_length=10)

    def __str__(self):
        return self.line_no


class Station(models.Model):

    line = models.ForeignKey(Line)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
