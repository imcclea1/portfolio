from django.db import models
#models.Model means will be saved in the database - sqlite3 is default
#beauty of django is can choose whatver database you want. 
class Job(models.Model):
    #you can go to documentation to see which fields you can have
    image = models.ImageField(upload_to='images/') #where will it be saved - we have put it in images folder
    summary = models.CharField(max_length=200) #want to put a cap on it