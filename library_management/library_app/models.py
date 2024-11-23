from django.db import models


# Create your models here.
class Collection(models.Model):
    collection_id = models.IntegerField(primary_key=True)
    collection_name = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.collection_name


class Category(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=100)
    sub_cat_name = models.CharField(max_length=100, blank=True, null=True)

    # def __str__(self):
    #     return self.cat_name


class Member(models.Model):
    mem_id = models.IntegerField(primary_key=True)
    mem_name = models.CharField(max_length=100)
    mem_phone = models.CharField(max_length=15)
    mem_email = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.mem_name


class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=255)
    book_cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE)
    book_launch_date = models.DateField()
    book_publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name


class Membership(models.Model):
    membership_id = models.IntegerField(primary_key=True)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    status = models.CharField(max_length=40)


class Issuance(models.Model):
    issuance_id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    issuance_date = models.DateTimeField()
    issuance_member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issued_by = models.CharField(max_length=100)
    target_return_date = models.DateTimeField()
    issuance_status = models.CharField(max_length=40)

    # def __str__(self):
    #     return self.issuance_member

# Create your models here.
