from __future__ import unicode_literals
from django.utils.datastructures import MultiValueDictKeyError

from django.db import models
import re
import bcrypt
from django import forms
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class UserManager(models.Manager):
	def registerVal(self, postData):
		print postData
		results = {'status': True, 'errors': [], 'user': None}
		if len(postData['first_name']) < 3 and len(postData['first_name']) > 50:
			results['status'] = False
			results['errors'].append('First Name Must be at Least 3 Characters.')
		if len(postData['last_name']) < 3 and len(postData['last_name']) > 50:
			results['status'] = False
			results['errors'].append('Last Name Must be at Least 3 Characters.')
		if len(postData['username']) < 3  and len(postData['username']) > 20:
			results['status'] = False
			results['errors'].append('Username Must be at Least 3 Characters.')
		if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
			results['status'] = False
			results['errors'].append('Please Enter a Valid Email.')
		if len(postData['password']) < 4 or postData['password'] != postData['confirm_password']:
			results['status'] = False
			results['errors'].append('Please Enter a Set of Matching Valid Password.')

		user = User.objects.filter(username=postData['username'])
		print user, '*****', len(user)
		if len(user) >= 1:
			results['status'] = False
			results['errors'].append(
			    'User Already Exists, Please Login or Use a Different Username.')
		return results

	def createUser(self, postData):
		p_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
		print postData['club']
		clubval = Club.objects.get(id = postData['club'])
		user = User.objects.create(
		    first_name=postData['first_name'], last_name=postData['last_name'], username = postData['username'], email=postData['email'], password=p_hash,)
		return user

	def loginVal(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		results['user'] = User.objects.filter(username=postData['username'])
		if len(results['user']) < 1:
			results['status'] = False
			results['errors'].append('Invalid Login Information')
		else:
			hashed = bcrypt.hashpw(postData['password'].encode(
			    ), results['user'][0].password.encode())
			if hashed != results['user'][0].password:
				results['status'] = False
				results['errors'].append('Invalid Login Information')
		return results

@python_2_unicode_compatible
class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	username = models.CharField(max_length=20)
	email = models.CharField(max_length=250)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

	def __str__(self):
		return self.first_name + " " + self.last_name
