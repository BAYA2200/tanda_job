import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType

from orders.schema import Query as OrdersQuery, Mutation as OrdersMutation
import graphql_jwt

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


schema = graphene.Schema(query=Query, mutation=Mutation)

