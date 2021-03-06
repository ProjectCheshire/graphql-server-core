from graphql.type.definition import (
    GraphQLArgument,
    GraphQLField,
    GraphQLNonNull,
    GraphQLObjectType,
)
from graphql.type.scalars import GraphQLString
from graphql.type.schema import GraphQLSchema


def resolve_raises(*_):
    raise Exception("Throws!")


QueryRootType = GraphQLObjectType(
    name="QueryRoot",
    fields={
        "thrower": GraphQLField(GraphQLNonNull(GraphQLString), resolver=resolve_raises),
        "request": GraphQLField(
            GraphQLNonNull(GraphQLString),
            resolver=lambda obj, info: context.args.get("q"),
        ),  # noqa: F821
        "context": GraphQLField(
            GraphQLNonNull(GraphQLString), resolver=lambda obj, info: context
        ),  # noqa
        "test": GraphQLField(
            type=GraphQLString,
            args={"who": GraphQLArgument(GraphQLString)},
            resolver=lambda obj, info, who="World": "Hello %s" % who,
        ),
    },
)

MutationRootType = GraphQLObjectType(
    name="MutationRoot",
    fields={
        "writeTest": GraphQLField(type=QueryRootType, resolver=lambda *_: QueryRootType)
    },
)

schema = GraphQLSchema(QueryRootType, MutationRootType)
