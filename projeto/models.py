from django.db import models

# Para realizar o cadastro de cliente será necessário email e senha. O email deve ser único.
# Email e senha tem um tamanho máximo de 254 e 128 caracteres respectivamente. O email não pode ser nulo e a senha também não pode ser nula.
# A função __str__ retorna o email do cliente, de modo que no banco de dados, o email do cliente será exibido como representação do objeto Cliente.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True, blank=True, null=True)
    senha = models.CharField(max_length=128, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)

class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cor = models.CharField(max_length=50)
    tamanho = models.CharField(max_length=10)
    estoque = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.produto.nome} - {self.cor} - {self.tamanho}"