from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
	def registerVal(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		if len(postData['first_name']) < 3:
			results['status'] = False
			results['errors'].append('First Name must be at least 3 chars.')
		if len(postData['last_name']) < 3:
			results['status'] = False
			results['errors'].append('Last Name must be at least 3 chars.')
		if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
			results['status'] = False
			results['errors'].append('Please enter a valid email.')
		if len(postData['password']) < 4  or  postData['password'] != postData['c_password']:
			results['status'] = False
			results['errors'].append('Please enter a valid password.')

		user = User.objects.filter(email = postData['email'])
		print user, '*****', len(user)
		if len(user) >= 1:
			results['status'] = False
			results['errors'].append('User already exists')



		#check to see if user is not in db

		return results
	def createUser(self, postData):
		p_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
		user = User.objects.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = p_hash,)
		return user
	def loginVal(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		results['user'] = User.objects.filter(email = postData['email'])
		if len(results['user'] ) <1:
			results['status'] = False
			results['errors'].append('Something went wrong')
		else:
			hashed = bcrypt.hashpw(postData['password'].encode(), results['user'][0].password.encode())
			if hashed  != results['user'][0].password:
				results['status'] = False
				results['errors'].append('Something went wrong')
		return results




class User(models.Model):
	first_name = models.CharField(max_length = 400)
	last_name = models.CharField(max_length = 400)
	email = models.CharField(max_length = 400)
	password = models.CharField(max_length = 400)

	satoshi = models.FloatField(default=0)
	section_1_level = models.IntegerField(default=1)
	section_2_level = models.IntegerField(default=0)
	section_3_level = models.IntegerField(default=0)
	section_4_level = models.IntegerField(default=0)
	section_5_level = models.IntegerField(default=0)
	section_6_level = models.IntegerField(default=0)
	section_7_level = models.IntegerField(default=0)
	section_8_level = models.IntegerField(default=0)
	section_9_level = models.IntegerField(default=0)
	section_10_level = models.IntegerField(default=0)
	section_11_level = models.IntegerField(default=0)
	section_12_level = models.IntegerField(default=0)


	objects = UserManager()

	def __str__(self):
		return self.first_name + " " + self.last_name
