import graphene
from graphene_django.types import DjangoObjectType
from .models import Order


class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = "__all__"


class Query(graphene.ObjectType):
    orders = graphene.List(OrderType)

    def resolve_orders(root, info):
        return Order.objects.all()


class CreateOrder(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=False)

    order = graphene.Field(OrderType)

    def mutate(self, info, title, description=None):
        order = Order.objects.create(title=title, description=description)
        return CreateOrder(order=order)


class UpdateOrderStatus(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        status = graphene.String(required=True)

    order = graphene.Field(OrderType)

    def mutate(self, info, id, status):
        order = Order.objects.get(pk=id)
        if status not in dict(Order.STATUS_CHOICES):
            raise Exception("Invalid status.")
        order.status = status
        order.save()
        return UpdateOrderStatus(order=order)


class Mutation(graphene.ObjectType):
    create_order = CreateOrder.Field()
    update_order_status = UpdateOrderStatus.Field()


