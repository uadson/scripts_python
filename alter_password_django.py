from django.contrib.auth.models import User

print(User.objects.filter(is_superuser=True))

superuser = User.objects.filter(is_superuser=True)

user = User.objects.get(username=superuser)

nova_senha = input('Nova Senha: ').strip()

user.set_password(nova_senha)

user.save()