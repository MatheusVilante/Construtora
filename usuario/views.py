from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST



class UsuarioAPIView(APIView):

    def post(self, request):
        usuario = authenticate(username=request.POST.get('username'),password=request.POST.get('password')) 
        if (request.POST.get('redirecionar')is None):
            response = request.POST 
            login(request, usuario)    
            return HttpResponseRedirect('/inicio')    
        if usuario:
            if (request.POST.get('redirecionar')is None):
                return HttpResponseRedirect('/inicio')
            token, created = Token.objects.get_or_create(user=usuario)
        else:
            return Response({"Login incorreto"})
        response = {
                "nome_usuario": usuario.get_full_name(),
                "token": token.key,
            }
        
        return Response(response) 

    def get(self, request): 
        if not request.user.is_authenticated:
            print('ók')
        return Response(request.user.id) 


    @require_POST
    def entrar(request):
        usuario_aux = User.objects.get(username=request.POST['username'])
        usuario = authenticate(username=usuario_aux.username,
        password=request.POST['password'])
        return usuario


    @login_required
    def sair(request):
        logout(request)
        return HttpResponseRedirect('/')
    


# class CadastrarUsuarioAPIView(APIView):
#     def post(self,request):
#         username = request.POST['username']
#         nome = request.POST['nome']
#         password = request.POST['password']
    
#         try:
#             usuario_aux = User.objects.filter(username=request.POST['username'])

#             if usuario_aux:
#                 return render(request, 'caminho para o index', {'msg': 'Erro! Já existe um usuário com o mesmo login'})

#         except User.DoesNotExist:
#             username = request.POST['username']
#             nome = request.POST['nome']
#             password = request.POST['password']

#         novoUsuario = User.objects.create_user(username=username, first_name=nome, password=password)
#         novoUsuario.save()
#         return Response({})


#     def put  (self, request):        
#         id = request.POST['id']
#         username = request.POST['username']
#         nome = request.POST['nome']
#         password = request.POST['password']
#         User.objects.filter(id=id).update(username=username, first_name=nome, password=password)
#         return Response('sucesso')

#     def delete(self, request, id=None):
#         id = request.GET['id']
#         usuario = User.objects.filter(id=id)
#         usuario.delete()
#         return Response('delete')


