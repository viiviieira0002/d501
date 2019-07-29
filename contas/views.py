from django.shortcuts import render
from .models import Pessoa

def mostrar_formulario_cadastro(request):
  contexto = {'msg': ''}
  if request.method == 'POST':
    pessoa = Pessoa()
    pessoa.nome = request.POST.get('nome')
    pessoa.cpf = request.POST.get('cpf')
    pessoa.email = request.POST.get('email')
    pessoa.telefone = request.POST.get('telefone')
    pessoa.genero = request.POST.get('genero')
    pessoa.save()
    contexto = {'msg': 'Aeee Parabéns :)'}
  return render(request, 'index.html', contexto)

def mostrar_pessoas(request):
  pessoas = Pessoa.objects.all()

  return render(request, 'pessoas.html', {'dados': pessoas})

def login(request):
  if request.method == 'POST':
    email_formulario = request.POST.get('email')
    pessoa_banco_dados = Pessoa.objects.filter(email=email_formulario).first()
    if pessoa_banco_dados is not None:
      return render(request, 'pessoa_filtrada.html', {'pessoa': pessoa_banco_dados})
    return render(request, 'login.html', {'msg': 'Ops, não encontramos'})
  
  return render(request, 'login.html', {'msg': 'ola'})

# - Página Login
# - Render da página login com campo email 
# e o btn consultar
# - Ao clicar no botão consultar
# - Enviar para uma outra página com todos os dados e 
# conta da pessoa
# - se a pessoa não for cadastrada, retornar para página
#  de login
# com uma mensagem: 'Ops, não encontramos essa pessoa'
