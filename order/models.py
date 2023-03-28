from django.db import models
from user.models import User
from django.utils import timezone
# Create your models here.

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_description = models.CharField(max_length=80)
    item_quantity = models.PositiveIntegerField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_value = models.DecimalField(max_digits=12, decimal_places=2, editable=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        # Calcula o valor total antes de salvar
        self.total_value = self.item_quantity * self.item_price
        # Verifica se o objeto foi atualizado antes de salvar
        if self.id:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)