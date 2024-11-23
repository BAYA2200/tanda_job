import graphene
from orders.schema import Query as OrdersQuery, Mutation as OrdersMutation


class Query(OrdersQuery, graphene.ObjectType):
    pass


class Mutation(OrdersMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
