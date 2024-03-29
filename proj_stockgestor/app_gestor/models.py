from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    groups = models.ManyToManyField(
        Group,
        verbose_name=('grupos'),
        blank=True,
        help_text=(
            'Os grupos aos quais este usuário pertence. Um usuário terá todas as permissões '
            'concedidas a cada um de seus grupos.'
        ),
        related_name="custom_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('permissões do usuário'),
        blank=True,
        help_text=('Permissões específicas para este usuário.'),
        related_name="custom_user_set",  
        related_query_name="user",
    )

    def __str__(self) -> str:
        return self.username