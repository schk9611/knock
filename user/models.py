from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from post.models import DevStack


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have an name")
        if not last_name:
            raise ValueError("Users must have an name")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"email: {self.email}"

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perm(self, app_label):
        return True


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dev_stack = models.ManyToManyField(DevStack, blank=True)
    nick_name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to="", blank=True)
    bio = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = "user_profile"
