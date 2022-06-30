from django.db import models
import re
import bcrypt

class StudentManager(models.Manager):

    def registration_validator(self, postData):
        errors = {}
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['fname']) < 2:
            errors['fname'] = "The first name should be at least 2 character "
        if len(postData['lname']) < 2:
            errors['lname'] = "The last name should be at least 2 character "
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern
            errors['email'] = "Invalid email address!"
        else:
            try:
            # check the email does not exist in the database before creating
                email = Student.objects.get(email__iexact=postData['email'])
                errors['email'] = "The email is taken please try another one"
            except:
                pass
        if len(postData['password']) < 8:
            errors['password'] = "password should be at least 8 characters"
        if postData['password'] != postData['confirmPW']:
            errors['confirmPW'] = "password is not equal to the confirm password"
        return errors


    def login_validator(self, postData):
        errors= {}
        student = Student.objects.filter(email= postData['email'])
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']): # test whether a field matches the pattern
            errors['email'] = "Email is not valid"
        else:
            try:
                student = Student.objects.get(email__iexact=postData['email'])
                if not bcrypt.checkpw(postData['password'].encode(),student.password.encode()):
                    errors['login'] = "Email or Password is incorrect !"
            except:
                errors['login'] = "Email or Password is incorrect !"
        return errors




class Bootcamp(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField(upload_to='files/covers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # students
    # champions
    # instructors
    # bootcamp_comment


class Student(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    bootcamp= models.ForeignKey(Bootcamp, related_name='students' ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= StudentManager()
    # comment
    # projects


class Champion(models.Model):
    img=models.ImageField(upload_to='files/champion')
    bootcamp=models.ForeignKey(Bootcamp,related_name='champions' ,on_delete=models.CASCADE)


class Comment(models.Model):
    comment=models.CharField(max_length=255)
    student=models.ForeignKey(Student, related_name='comment' ,on_delete=models.CASCADE)
    bootcamp=models.ForeignKey(Bootcamp, related_name='bootcamp_comment' ,on_delete=models.CASCADE)



class Project(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField()
    url=models.URLField()
    img_project = models.ImageField(upload_to='files/covers')
    student=models.ForeignKey(Student,related_name='projects',on_delete=models.CASCADE)
    # champions



class instructor(models.Model):
    name = models.CharField(max_length=255)
    bootcamp=models.ForeignKey(Bootcamp, related_name='instructors',on_delete=models.CASCADE)
