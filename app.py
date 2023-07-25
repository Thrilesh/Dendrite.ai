from flask import Flask, request, jsonify
from flask_graphql import GraphQLView
from database import init_db
from keycloak import keycloak_required
from graphql.schema import schema

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the To-Do List App!'

# Initialize database and other configurations
init_db()

app.add_url_rule(
    '/graphql',
    view_func=keycloak_required(GraphQLView.as_view('graphql', schema=schema, graphiql=True))
)

if __name__ == '__main__':
    app.run(debug=True)
