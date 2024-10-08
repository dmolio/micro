from flask import request
from flask_restful import Resource
from app.models import Item, items

class ItemListResource(Resource):
    def get(self):
        return {'items': [item.to_dict() for item in items]}

    def post(self):
        data = request.get_json()
        item = Item(data['name'], data['description'])
        items.append(item)
        return item.to_dict(), 201

class ItemResource(Resource):
    def get(self, item_id):
        item = next((item for item in items if item.id == item_id), None)
        if item:
            return item.to_dict()
        return {'message': 'Item not found'}, 404

    def put(self, item_id):
        item = next((item for item in items if item.id == item_id), None)
        if item:
            data = request.get_json()
            item.name = data['name']
            item.description = data['description']
            return item.to_dict()
        return {'message': 'Item not found'}, 404

    def delete(self, item_id):
        global items
        items = [item for item in items if item.id != item_id]
        return '', 204
