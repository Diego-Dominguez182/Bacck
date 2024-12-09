from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Build
from .serializers import BuildSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password



@api_view(['POST'])
def register(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not email or not password:
        return Response({"error": "El email y la contraseña son requeridoss"}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=email).exists():
        return Response({"error": "El email  ya existe"}, status=status.HTTP_400_BAD_REQUEST)
    
    usuario = User.objects.create(
        username=email,
        password=make_password(password)  
    )
    
    token, creado = Token.objects.get_or_create(user=usuario)
    
    return Response({"token": token.key}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not email or not password:
        return Response({"error": "El email y la contraseña son requeridos"}, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=email, password=password)
    
    if user:
        token, created = Token.objects.get_or_create(user=user)
        print(token.key)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
        
    
    return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['GET'])
def getBuilds(request):
    queryset = Build.objects.all()
    serializer = BuildSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createBuild(request):
    serializer = BuildSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getBuildByName(request, name):
    builds = Build.objects.filter(champion_name=name)
    if builds.exists():
        serializer = BuildSerializer(builds, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def deletByID(request, idSearch):
    try:
        build = Build.objects.get(id=idSearch)
        build.delete()
        return Response({"Mensaje": "Build borrada exitosamente."}, status=status.HTTP_200_OK)
    except Build.DoesNotExist:
        return Response({"error": "Build no encontrada."}, status=status.HTTP_404_NOT_FOUND)