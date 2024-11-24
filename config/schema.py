import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType

from orders.schema import Query as OrdersQuery, Mutation as OrdersMutation
import graphql_jwt

from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
from orders.schema import Query as OrdersQuery, Mutation as OrdersMutation
import graphql_jwt
from graphql_jwt.shortcuts import get_token, create_refresh_token
class Query(OrdersQuery, graphene.ObjectType):
    pass


class Mutation(OrdersMutation, graphene.ObjectType):
    pass

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class Query(graphene.ObjectType):
    me = graphene.Field(UserType)

    def resolve_me(root, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Not authenticated!")
        return user


class Mutation(graphene.ObjectType):
    # Мутация для логина
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # Мутация для обновления токена
    refresh_token = graphql_jwt.Refresh.Field()
    # Мутация для выхода (удаление refresh токена)
    revoke_token = graphql_jwt.Revoke.Field()

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, email, password):
        user = User.objects.create_user(username=username, email=email, password=password)
        token = get_token(user)
        refresh_token = create_refresh_token(user)
        return CreateUser(user=user, token=token, refresh_token=refresh_token)

schema = graphene.Schema(query=Query, mutation=Mutation)

