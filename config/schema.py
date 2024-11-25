import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
import graphql_jwt
from graphql_jwt.shortcuts import get_token, create_refresh_token
from orders.schema import Query as OrdersQuery, Mutation as OrdersMutation


# Тип пользователя
class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "email")


# Запросы
class Query(OrdersQuery, graphene.ObjectType):
    me = graphene.Field(UserType)

    def resolve_me(root, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Not authenticated!")
        return user


# Мутация для создания пользователя
class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    token = graphene.String()
    refresh_token = graphene.String(name="refreshToken")

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, email, password):
        if User.objects.filter(username=username).exists():
            raise Exception("Username already exists.")
        if User.objects.filter(email=email).exists():
            raise Exception("Email already exists.")

        user = User.objects.create_user(username=username, email=email, password=password)
        token = get_token(user)
        refresh_token = create_refresh_token(user)
        return CreateUser(user=user, token=token, refresh_token=refresh_token)


# Кастомная мутация для получения токенов
# Кастомная мутация для получения токенов
# Кастомная мутация для получения токенов
class CustomObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(UserType)
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, username, password, **kwargs):
        # Проверка учетных данных пользователя
        user = User.objects.filter(username=username).first()
        if not user or not user.check_password(password):
            raise Exception("Invalid credentials.")

        # Генерация токенов
        token = get_token(user)
        refresh_token = create_refresh_token(user)

        # Возврат экземпляра класса с заполненными полями
        return cls(user=user, token=token, refresh_token=refresh_token)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        # Здесь resolve должен просто вернуть результат без изменений
        return root



# Мутации
class Mutation(OrdersMutation, graphene.ObjectType):
    token_auth = CustomObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()
    create_user = CreateUser.Field()


# Схема
schema = graphene.Schema(query=Query, mutation=Mutation)
