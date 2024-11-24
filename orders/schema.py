import graphene
from graphene_django.types import DjangoObjectType
from .models import Order


class OrderType(DjangoObjectType):
    """Represents an Order with its details."""
    class Meta:
        model = Order
        fields = "__all__"


class Query(graphene.ObjectType):
    """API endpoints for querying orders."""

    orders = graphene.List(OrderType,  description="Retrieve a list of all orders.")

    def resolve_orders(root, info):
        """Resolver for fetching all orders."""
        return Order.objects.all()


class CreateOrder(graphene.Mutation):
    """Mutation for creating a new order."""

    class Arguments:
        title = graphene.String(required=True, description="The title of the order.")
        description = graphene.String(required=False , description="A short description of the order.")

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


