'''from flask import Flask, jsonify, request

app = Flask(__name__)

users = []

@app.route('/api/users', methods=['GET'])
def list_users():
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def create_user():
    user = request.get_json()
    if 'name' not in user or 'email' not in user:
        return jsonify({'eror':'Name and email are required'}),400
    user['id'] = len(users)+1
    users.append(user)
    return jsonify(user),201

@app.route('/api/users/<int:user_id>',methods = ["PUT"])
def update_user():
    user = next((user for user in users if user['id'] == user_id),None)
    if user:
        data = request.get_json()
        user.update(data)
        return jsonify()
    return jsonify({'Error':'usernotfound'}),404

if __name__== '__main__':
    app.run(debug=True)'''

'''from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

@app.route('/api/tasks',methods = ['GET'])
def get_quests():
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    task = request.get_json()
    if 'Title' not in task:
        return jsonify({'eror':'Title are required'}),400
    task['id'] = len(tasks)+1
    tasks["completed"] = False
    tasks.append(task),201

@app.route('/api/quests/<int:task_id>',methods = ["PUT"])
def update_task():
    task = next((task for task in tasks if task['id'] == task_id),None)
    if task:
        data = request.get_json()
        task.update(data)
        return jsonify(task)
    return jsonify({'Error':'task not found'}),404

if __name__== '__main__':
    app.run(debug=True)'''

'''from flask import Flask, jsonify, request

app = Flask(__name__)

products = []

@app.route('/api/products',methods = ['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/products', methods=['POST'])
def add_product():
    product = request.get_json()
    if 'Title' not in product:
        return jsonify({'eror':'Title are required'}),400
    product['id'] = len(products)+1
    products["completed"] = False
    products.append(product),201

@app.route('/api/products/<int:product_id>',methods = ["PUT"])
def update_product():
    product = next((product for product in products if product['id'] == product_id),None)
    if product:
        data = request.get_json()
        product.update(data)
        return jsonify(product)
    return jsonify({'Error':'product not found'}),404

if __name__== '__main__':
    app.run(debug=True)'''

from flask import Flask, jsonify, request

app = Flask(__name__)

comments = []

@app.route('/api/comments',methods = ['GET'])
def get_comments():
    return jsonify(comments)

@app.route('/api/comments', methods=['POST'])
def add_comments():
    comment = request.get_json()
    if 'Comment' not in comments:
        return jsonify({'eror':'Comment are required'}),400
    comment['id'] = len(comments)+1
    comments["completed"] = False
    comments.append(comment),201

@app.route('/api/comments/<int:comments_id>',methods = ["PUT"])
def update_comments():
    comment = next((comment for comment in comments if comment['id'] == comment_id),None)
    if comment:
        data = request.get_json()
        comments.update(data)
        return jsonify(comment)
    return jsonify({'Error':'comment not found'}),404

if __name__== '__main__':
    app.run(debug=True)