from django.db import models

# Para realizar o cadastro de cliente será necessário email e senha. O email deve ser único.
# Email e senha tem um tamanho máximo de 254 e 128 caracteres respectivamente. O email não pode ser nulo e a senha também não pode ser nula.
# A função __str__ retorna o email do cliente, de modo que no banco de dados, o email do cliente será exibido como representação do objeto Cliente.

class Cliente(models.Model):
    email = models.EmailField(max_length=254, unique=True, blank=False)
    senha = models.CharField(max_length=128, blank=False)
    telefone = models.CharField(max_length=15, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return self.email