from django.db import models


class Menu(models.Model):
    nome = models.CharField(max_length=200, default="")
    visualizza = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    @property
    def items(self):
        return Item.objects.filter(visualizza=True, menu=self)


class Item(models.Model):
    DEFAULT_DESCRIPTION = """This is a wider card with supporting text below as a natural lead-in to
                            additional content. This content is a little bit longer."""

    menu = models.ForeignKey(Menu, blank=True, null=True,
                             on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=200)
    visualizza = models.BooleanField(default=False)
    prezzo = models.CharField(max_length=200)
    photo = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)
    snack = models.CharField(max_length=150)
    descrizione = models.TextField(blank=True, null=True, default=DEFAULT_DESCRIPTION)

    def __str__(self):
        return self.nome

    @property
    def allergeni(self):
        return Allergene.objects.filter(item=self)


class Allergene(models.Model):
    ALLERGENE_CHOICES = (
        ('Latticini', 'Latticini'),
        ('Glutine', 'Glutine'),
        ('Arachidi', 'Arachidi'),
        ('Uova', 'Uova'),
        ('Nichel', 'Nichel'),
    )

    tipo = models.CharField(choices=ALLERGENE_CHOICES, max_length=30,
                            blank=True, default="")
    item = models.ForeignKey(Item, blank=True, null=True,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo


class FeedBack(models.Model):
    nome = models.CharField(max_length=100, default="Guest")
    messaggio = models.TextField(max_length=200)
