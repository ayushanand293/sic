from flask import Flask, jsonify, request
from person_flask_dao import Db_operations, Person

persons = Db_operations()

persons.create_table()

app = Flask(__name__)

@app.route('/persons',methods=['POST'])
def persons_create():
    body = request.get_json()
    dob = body['dob'] if body['dob'] else None  # Handle empty string for dob
    new_person = Person(body['name'], body['gender'], dob, body['location'])
    id = persons.insert_row(new_person)
    person = persons.search_row(id)
    person_dict = {'id': person[0], 'name': person[1], 'gender': person[2], 'dob': person[3], 'location': person[4]}
    return jsonify(person_dict)
    
@app.route('/new_persons/<id>',methods=['GET'])
def persons_read_by_id(id):
    person = persons.search_row(id)
    print(person)
    print(type(person))
    if person == None:
        return jsonify("person not found")
    person_dict = {'id':person.id, 'name':person.name,'gender':person.gender, 'location': person.location, 'dob':person.dob}
    return jsonify(person_dict)

@app.route('/persons',methods=['GET'])
def persons_read_all():
    persons_list = persons.list_all_rows()
    persons_dict = []
    for person in persons_list:
        persons_dict.append({'id':person[0], 'name':person[1], 'gender':person[2], 'dob':person[3], 'location': person[4]})
    return jsonify(persons_dict)

@app.route('/persons/<id>',methods=['PUT'])
def persons_update(id):
    body = request.get_json()
    old_person_obj = persons.search_row(id)
    if not old_person_obj:
        return jsonify({'message': 'Person not found'})
    new_person_obj = []
    new_person_obj.append(body['name'])
    new_person_obj.append(body['gender'])
    new_person_obj.append(body['location'])
    new_person_obj.append(body['dob'])
    new_person_obj.append(id)
    new_person_obj = tuple(new_person_obj)
    persons.update_row(new_person_obj)

    person = persons.search_row(id)
    person_dict = {'id':person[0], 'name':person[1], 'gender':person[2], 'dob':person[3], 'location': person[4]}
    return jsonify(person_dict)

@app.route('/persons/<id>',methods=['DELETE'])
def persons_delete(id):
    old_person_obj = persons.search_row(id)
    if not old_person_obj:
        return jsonify({'message': 'person not found', 'is_error': 1})
    persons.delete_row(id)
    return jsonify({'message': 'person is deleted', 'is_error': 0})

app.run(debug=True)