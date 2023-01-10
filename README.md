# ESCOLA_API

Estou criando uma API com Django Rest API com fins de treinamento, 
nela estou me baseando em cursos feitos previamento, porem com diversas
 mudanças

----------------------------------------------------------------




## Criando o Ambiente Virtual

    python3 -m venv ./venv
    source venv/bin/activate


## Instalando As Dependencias

    pip3 install requirements.txt


## Help

Mostra os comandos do django:

    python3 manage.py help


## Criar Projeto

Criando um projeto, um projeto pode conter muitos apps e configurações.
    django-admin startproject nomeDoProjeto


## Subir servidor

    python3 manage.py runserver


## Criar Aplicativo

Cria um app, app é uma aplicação de um ou mais projetos. Cada app deve ser adicionado a seus respectivos projetos em INSTALLED_APPS de nomeDoProjetp/settings.py

    python3 manage.py startapp nomeDoApp

Criando urls.py no app, para adicionar as urls do aplicativo


## Rest Framework

Adicione em setup/settings.py:

    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    ...
]

## Crie Seus Modelos

    class ClasseDoModelo(models.Model):
        nome = models.CharField(max_length=50, blank=False, null=False)
        cpf = models.CharField(max_length=14, blank=False, null=False, unique=True)
        email = models.EmailField(blank=False, null=False, unique=True)
        celular = models.CharField(max_length=15, blank=False, null=False)
        data_nascimento = models.DateField(blank=False, null=False)

        def __str__(self) -> str:
            return self.nome


## Serializando os Modelos

    from rest_framework import serializers
    from nomeApp.models import ClasseModel


    class ClasseModelSerializer(serializers.ModelSerializer):

        class Meta:
            model = ClasseModel

        def create(self, validated_data):
            """
            Sobreescrevendo algum dos métodos padrão do django
            """

            user_data = validated_data.pop('user')
            original_user_data = self.initial_data.get('user')
            user_serializer = UserSerializer(data=original_user_data)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()
            validated_data['user'] = user

            return super(StudentSerializer, self).create(validated_data)


## Views para Serializers

    from rest_framework import viewsets
    from nomeApp.models import ClasseModel
    from nomeApp.serializer import ClasseModelSerializer


    class ClasseModelsViewSet(viewsets.ModelViewSet):
        """ Exibindo todos os ClasseModels """

        # Query do SQL, tambem é comum usar ClasseModel.objects.filter()
        queryset = ClasseModel.objects.all() 

        # Autenticação das classes serializer
        authentication_classes = [BasicAuthentication]

        # Trazendo permissão do Django Admin
        permission_classes = [IsAuthenticated, DjangoModelPermissions]

        # Trazendo Filtros para a API
        filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

        #Ordem dos Campos
        ordering_fields = ['nome', 'id']

        # Filtro dos Campos
        search_fields = ['nome', 'id']

        # Métodos HTTP permitidos
        http_method_names = ['get', 'post', 'put', 'delete']
        

        # versionamento do Serializer
        def get_serializer_class(self):
            if self.request.version == 'v2':
                return ClasseModelSerializerV2
            else:
                return ClasseModelSerializerV1



## Registrando urls 

Um mesmo projeto pode conter diversos apps, logo ele necessita 

    from rest_framework import routers
    from app.views import *

    router = routers.DefaultRouter()
    router.register('app', AppViewSet, basename='App')




    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include(router.urls)),
        ...,
        ]


## Adicionando Valores Default no Django Rest

O arquvo settings.py contem as informações padão que o dajngo utilizará, 
logo podemos definir vaores default para nossas classes e preferencias.

Em setup.settings.py:

    REST_FRAMEWORK = {
        'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.QueryParameterVersioning',
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
            'rest_framework.permissions.DjangoModelPermissions'
        ],
        'DEFAULT_AUTHENTICATION_CLASSES' : [
            'rest_framework.authentication.BasicAuthentication'
        ],

        'DEFAULT_THROTTLE_RATES': {
            'anon': '10/day',
            'user': '1000/day'
        }
    }


## CORS e HOSTs

CORS são basicamente os links ou portas que poderam receber e enviar dados 
para sua API. Podendo abastecer tanto um frontend, quanto mobile ou IOT

execute: 

    pip install django-cors-headers


em setup.settings.py:

    INSTALLED_APPS = [
        ...,
        "corsheaders",
        ...,
    ]

    MIDDLEWARE = [
        ...,
        "corsheaders.middleware.CorsMiddleware",
        "django.middleware.common.CommonMiddleware",
        ...,
    ]

    CORS_ALLOWED_ORIGINS = [
        "https://example.com",
        "https://sub.example.com",
        "http://localhost:8080",
        "http://127.0.0.1:9000",
    ]


Os ALLOWED_HOSTS são basicamente as portas locais que poderam ser usadas para testes 
no localhost.

em settings.py: 

    ALLOWED_HOSTS = [
        'localhost', '127.0.0.1', 'www.mysite.com'
    ]

# Arquivos Estaticos e Pillow


Pillow é uma biblioteca para organização de arquivos estaticos com o django.
Por pdadrão o Django apenas o path da foto, assim é necessário configurar onde 
ficaram os arquivos estaticos e suas urls.


    pip install pillow


em settings.py: 

    STATIC_URL = 'static/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')
    MEDIA_URL = '/media/'

em urls.py:

    ...
    from django.conf import settings
    from django.conf.urls.static import static

    ...

    urlpatterns = [
        ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Caching

Caching é basicamente uma cópia de parte dos dados, ou seja, de quanto em qaunto
 tempo um recurso será atuaizado.


# Caching e Redis

Redis é um banco de dados muito utilizado para caching, ele basicamente funciona com 
chave e valor, ele pode ser baixado no link: https://redis.io/download/
Instale com make, na pasta extraida do link acima:

    make
    make test

Para ligar o redis:

    src/redis-server


# Conectando Redis ao Django

Primeiro é necessário instalar um modulo para conecta-los:

    pip install django-redis
    


Em settings.py:

    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/1",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    }

    SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
    SESSION_CACHE_ALIAS = "default"

# Internacionalização

Para alterar a linguagem da resposta de erro da nossa API, em settings.py:


    MIDDLEWARE = [
        ...
        'django.middleware.locale.LocaleMiddleware'
    ]

# Alterando as Mensagens Padrão do Django

Em settings.py:

    LOCALE_PATHS = (
        (os.path.join(BASE_DIR, 'locale/'))
    )

E execute:

    manage.py makemessages -l pt_BR


# Respondendo com JSON, XML e YAML

Instale as bibliotecas 
    pip install djangorestframework-xml
    pip install djangorestframework-yaml

em views.py, em suas views adicione:

    class AppViewsSet(viewset.ModelViewsSet):
        ...
        renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)

Ou direto por padrão em settings.py:

    REST_FRAMEWORK = {
        ...
        'DEFAULT_PARSER_CLASSES': [
            'rest_framework.renderers.BrowsableAPIRenderer',
            'rest_framework.parsers.JSONParser',
            'rest_framework_xml.parsers.XMLParser',
            'rest_framework_yaml.parsers.YAMLParser',
        ],
        'DEFAULT_RENDERER_CLASSES': [
            'rest_framework.renderers.BrowsableAPIRenderer',
            'rest_framework.renderers.JSONRenderer',
            'rest_framework_xml.renderers.XMLRenderer',
            'rest_framework_yaml.renderers.YAMLRenderer',
        ],

    }


# Honey Pot

É uma biblioteca para registrar dados de todos que tentam acessar /admin em nossa 
aplicação, podendo conseguir informação de possíveis hackers.

execute: 

    pip install django-admin-honeypot

adicione em settings.py:

    INSTALLED_APPS = [
        ...
        'admin_honeypot',
    ]

Agora é só escolher a url para o pote de mél:


# Testes

Bom, testes são assenciais para toda e qualquer aplicação, um código sem testes vai falhar 
é apenas uma questão de tempo. Nesta aplicação, foram feitos alguns testes de unidade e de 
requisições no app de Cursos.


# Swagger

Swagger elimita o trabalho manual de documentação de uma API com seus clientes. Mostrando 
de uma melhor forma, quais urls são válidas para utilizarem nossa API, ele tem uma 
interface amigável e de fácil entendimento.

execute:

    pip install -U drf-yasg


em settings.py: 

    INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',  # required for serving swagger ui's css/js files
    'drf_yasg',
    ...
    ]


em urls.py:

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]