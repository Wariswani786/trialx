from django.db import models
from django.contrib.auth.models import User

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    condition = models.TextField()
    medications = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s Profile"

class ClinicalTrial(models.Model):
    title = models.CharField(max_length=255)
    inclusion_criteria = models.TextField()
    exclusion_criteria = models.TextField()  # ✅ Add default
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title



class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    trial = models.ForeignKey(ClinicalTrial, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'trial')  # prevents duplicate bookmarks

    def __str__(self):
        return f"{self.user.username} bookmarked {self.trial.title}"
