from django.db import models

# Create your models here.


class discente(models.Model):
    nome = models.CharField(primary_key=True, max_length=120)
    periodo = models.CharField(
        max_length=8, choices=[
            ('Primeiro', '1ª'),
            ('Segundo', '2ª'),
            ('Terceiro', '3ª'),
            ('Quarto', '4ª'),
            ('Quinto', '5ª'),
            ('Sexto', '6ª'),
            ('Sétimo', '7ª'),
            ('Oitavo', '8ª'),
            ('Nono', '9ª'),
        ], default='Primeiro')
    turno = models.CharField(
        max_length=10, choices=[
            ('Manhã', 'M'),
            ('Tarde', 'T'),
            ('Noite', 'N')
        ], default='Manhã')

    class Meta:
        verbose_name = 'Discente'
        verbose_name_plural = 'Discentes'

    def __str__(self):
        return self.nome


class emprestimo(models.Model):
    data = models.DateField(auto_now=True)
    discente = models.ForeignKey(
        discente, on_delete=models.CASCADE, related_name='emprestimos_discentes')
    quantidade = models.PositiveIntegerField(default=15)

    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'

    def __str__(self):
        return f'{self.data}'
