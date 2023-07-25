import graphene

class TodoItem(graphene.ObjectType):
    title = graphene.String()
    description = graphene.String()
    time = graphene.DateTime()

class Query(graphene.ObjectType):
    todos = graphene.List(TodoItem)

    def resolve_todos(self, info):
        # Implement fetching todos from the database and return them
        pass

class AddTodoItem(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        description = graphene.String()
        time = graphene.DateTime()

    todo = graphene.Field(TodoItem)

    def mutate(self, info, title, description, time):
        # Implement adding a new todo to the database
        pass

class Mutation(graphene.ObjectType):
    add_todo = AddTodoItem.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
