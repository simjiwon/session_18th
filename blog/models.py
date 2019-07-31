from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField("Date_published")
    body = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    parentClassObject = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="comments")
    comment_title = models.CharField(max_length=20)
    comment_pub_date = models.DateTimeField("Comment_date_published")
    comment_body = models.TextField()

    def __str__(self):
        return self.comment_title