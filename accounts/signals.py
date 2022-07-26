from django.db.models.signals import post_save, pre_delete

from django.dispatch import receiver

from student.models import CGPA, Course, Result
from .models import Department, Profile,College,User

@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        college = College.objects.create(name='no college')
        department = Department.objects.create(name='no department',college=college)
        Profile.objects.create(user=instance, department=department)
        
   
@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs):
        instance.profile.save()