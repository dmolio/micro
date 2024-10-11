from flask import request
from flask_restful import Resource
from app.models import Item

class ItemListResource(Resource):
    def get(self):
        return {'items': Item.get_all()}

    def post(self):
        data = request.get_json()
        item = Item(data['name'], data['description'])
        item.save()
        return item.to_dict(), 201

class ItemResource(Resource):
    def get(self, item_id):
        item = Item.get(item_id)
        if item:
            return item
        return {'message': 'Item not found'}, 404

    def put(self, item_id):
        item_data = Item.get(item_id)
        if item_data:
            data = request.get_json()
            item = Item(data['name'], data['description'])
            item.id = item_id
            item.save()
            return item.to_dict()
        return {'message': 'Item not found'}, 404

    def delete(self, item_id):
        if Item.get(item_id):
            Item.delete(item_id)
            return '', 204
        return {'message': 'Item not found'}, 404
