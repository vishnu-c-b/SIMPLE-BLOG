
# Create your models here.


# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     publication_date = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_posts')

#     def __str__(self):
#         return self.title