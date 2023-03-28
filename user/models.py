from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    
    name = models.CharField(max_length=80, null=False)
    cpf = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True, editable=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Verifica se o objeto foi atualizado antes de salvar
        if self.id:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)