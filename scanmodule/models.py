from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
	        raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(
			email=self.normalize_email(email),
			username=username,
		)
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, unique=False)
    family_name = models.CharField(max_length=50, unique=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='images/users', default='images/usersdef_user.png')
    teams_link = models.URLField(blank = True, max_length=200)
    mobile_phone = models.CharField(max_length=16, blank=True)
    user_location = models.CharField(max_length=80, blank=True)
    


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True




class ScanTemplate(models.Model):
    template_name = models.CharField(max_length=250)
    scan_options = models.CharField(max_length=250)
    scan_script = models.CharField(max_length=250)

    NMAP_OUTPUT_CHOICES = [
    ('XM', 'XML'),
    ('LS', 'LOGSTASH'),
    
    ]
    output_format = models.CharField(max_length=2,choices=NMAP_OUTPUT_CHOICES,default='XML')

    def __str__(self):
        return self.template_name

class ScanSet(models.Model):
    scanset_name = models.CharField(max_length=250)
    scan_template = models.ForeignKey(ScanTemplate, on_delete=models.RESTRICT)
    scan_every_min = models.IntegerField()
    scan_every_days = models.IntegerField()


    def __str__(self):
        return self.scanset_name


class SiteAssest(models.Model):
    site_name = models.CharField(max_length=250,blank=False)
    location_name = models.CharField(max_length=250,blank=False)
    # Geo location
    lon = models.FloatField()
    lat = models.FloatField()
    site_ip_range1 = models.CharField(max_length=250,blank=True)
    site_ip_range2 = models.CharField(max_length=250,blank=True)
    site_ip_range3 = models.CharField(max_length=250,blank=True)
    last_scaned = models.DateField(auto_now_add=False)
    TASK_STATUS_CHOICES = [
    ('ID', 'IDLE'),
    ('RU', 'RUNNING'),
    
    ]
    current_status = models.CharField(max_length=2,choices=TASK_STATUS_CHOICES,default='IDLE')

    site_rank = models.IntegerField()

    scan = models.ForeignKey(ScanSet, on_delete=models.RESTRICT)
    scan_count = models.IntegerField(default=0)


    def __str__(self):
        return self.site_name