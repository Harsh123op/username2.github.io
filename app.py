from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb+srv://harshmanjhi1801:waifu201@cluster0.xxwc4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['gaming_create']
collection = db['gaming_anime_characters']

# Route to get characters by page
@app.route('/characters/<int:page>', methods=['GET'])
def get_characters(page):
    characters_per_page = 9
    skip = (page - 1) * characters_per_page
    characters = list(collection.find({}, {'_id': 0, 'name': 1, 'img_url': 1}).skip(skip).limit(characters_per_page))

    return jsonify({
        'characters': characters,
        'current_page': page,
        'total_characters': collection.count_documents({})
    })

if __name__ == '__main__':
    app.run(debug=True)
