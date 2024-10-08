from flask import Flask
from flask_restful import Api
from app.routes import ItemResource, ItemListResource

def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(ItemListResource, '/items')
    api.add_resource(ItemResource, '/items/<int:item_id>')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5001)
