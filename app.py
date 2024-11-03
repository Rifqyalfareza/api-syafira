from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Sample aquarium equipment data with 15 items
equipment_list = [
    {"id": 1, "name": "Air Pump", "description": "Provides oxygen to the aquarium", "price": 20, "stock": 50},
    {"id": 2, "name": "Water Heater", "description": "Maintains water temperature in tropical aquariums", "price": 35, "stock": 30},
    {"id": 3, "name": "Filter", "description": "Removes impurities from water, keeps it clean", "price": 40, "stock": 20},
    {"id": 4, "name": "Aquarium Light", "description": "LED light for plant growth and fish visibility", "price": 25, "stock": 45},
    {"id": 5, "name": "Gravel Cleaner", "description": "Removes debris and waste from gravel", "price": 15, "stock": 60},
    {"id": 6, "name": "Aquarium Thermometer", "description": "Monitors water temperature accurately", "price": 8, "stock": 75},
    {"id": 7, "name": "Fish Net", "description": "Helps to catch or transfer fish safely", "price": 5, "stock": 100},
    {"id": 8, "name": "Algae Scraper", "description": "Removes algae buildup on aquarium walls", "price": 10, "stock": 40},
    {"id": 9, "name": "Fish Food", "description": "Nutritionally balanced food for freshwater fish", "price": 12, "stock": 150},
    {"id": 10, "name": "CO2 Diffuser", "description": "Increases CO2 levels for plant growth", "price": 18, "stock": 25},
    {"id": 11, "name": "Decorative Plants", "description": "Artificial plants to beautify the aquarium", "price": 9, "stock": 80},
    {"id": 12, "name": "Aquarium Stand", "description": "Sturdy stand for supporting large aquariums", "price": 100, "stock": 15},
    {"id": 13, "name": "Water Conditioner", "description": "Neutralizes chlorine and chloramines", "price": 7, "stock": 65},
    {"id": 14, "name": "PH Meter", "description": "Accurately measures the water's pH level", "price": 22, "stock": 30},
    {"id": 15, "name": "Aquarium Background", "description": "Scenic background to enhance aquarium aesthetics", "price": 14, "stock": 55},
]

# Helper function to find an item by ID
def find_equipment(equipment_id):
    return next((item for item in equipment_list if item["id"] == equipment_id), None)

class EquipmentList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "success",
            "count": len(equipment_list),
            "equipment": equipment_list
        }

class EquipmentDetail(Resource):
    def get(self, equipment_id):
        equipment = find_equipment(equipment_id)
        if equipment:
            return {"error": False, "message": "success", "equipment": equipment}
        return {"error": True, "message": "Equipment not found"}, 404

class AddEquipment(Resource):
    def post(self):
        data = request.get_json()
        new_equipment = {
            "id": data.get("id"),
            "name": data.get("name"),
            "description": data.get("description"),
            "price": data.get("price"),
            "stock": data.get("stock")
        }
        equipment_list.append(new_equipment)
        return {"error": False, "message": "Equipment added successfully", "equipment": new_equipment}, 201

class UpdateEquipment(Resource):
    def put(self, equipment_id):
        data = request.get_json()
        equipment = find_equipment(equipment_id)
        if equipment:
            equipment.update({
                "name": data.get("name", equipment["name"]),
                "description": data.get("description", equipment["description"]),
                "price": data.get("price", equipment["price"]),
                "stock": data.get("stock", equipment["stock"])
            })
            return {"error": False, "message": "Equipment updated successfully", "equipment": equipment}
        return {"error": True, "message": "Equipment not found"}, 404

class DeleteEquipment(Resource):
    def delete(self, equipment_id):
        equipment = find_equipment(equipment_id)
        if equipment:
            equipment_list.remove(equipment)
            return {"error": False, "message": "Equipment deleted successfully"}
        return {"error": True, "message": "Equipment not found"}, 404

api.add_resource(EquipmentList, '/equipment')
api.add_resource(EquipmentDetail, '/equipment/<int:equipment_id>')
api.add_resource(AddEquipment, '/equipment/add')
api.add_resource(UpdateEquipment, '/equipment/update/<int:equipment_id>')
api.add_resource(DeleteEquipment, '/equipment/delete/<int:equipment_id>')

if __name__ == '__main__':
    app.run(debug=True)
