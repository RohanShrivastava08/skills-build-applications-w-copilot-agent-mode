from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    duration = models.IntegerField()  # Duration in minutes
    date = models.DateField()

    def __str__(self):
        return f"{self.type} by {self.user.name}"

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.team.name}: {self.score}"

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()  # Duration in minutes

    def __str__(self):
        return self.name
