from django.db.models.signals import pre_save, pre_delete, post_delete, post_save
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum


def car_inventory_update():
    cars_count = Car.objects.all().count()
    #Calcula o valor de todos os carros presentes no banco de dados
    cars_value = Car.objects.aggregate(
       total_value = Sum('value')
    )['total_value']
    #Essa lista faz com que a funcão aggregate retorne somente o valor
    CarInventory.objects.create(
       cars_count = cars_count,
       cars_value = cars_value
    )
    #Após calcular tudo, eu crio uma nova tabela com os novos valores
   

'''@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.description:
        ai_description = get_car_ai_description(
            instance.model, instance.brand, instance.model_year
        )
        instance.description = ai_description'''




@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()



@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()