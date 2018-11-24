from flask import Flask,request,jsonify
app = Flask(__name__)

books=[
{'title':'api intro','id':1,'author':'bana','ISBN':97}
]

@app.route('/')
def landing():
    return 'Hello, World!'

@app.route('/api/v1/books/<int:bookId>')
def get_book(bookId):
	for book in books:
		if book['id']==bookId:
			return jsonify({'book':book,'message':'Success'}), 200

	return jsonify({'message':'Sorry! There no books found'}), 200


@app.route('/api/v1/books', methods=['GET'])
def get_books():
	if len(books)<1:
		return jsonify({
			{'message':'Sorry! There no books found'}
			}), 200

	return jsonify({
		'books':books,
		'message':'Success'
		})


@app.route('/api/v1/books', methods=['POST'])
def add_book():
	data=request.get_json()
	title=data.get('title')
	author=data.get('author')
	issbn=data.get('ISBN')
	id=len(books)+1

	if not title or title.isspace():
		return jsonify({'message':'title is required'}), 400

	book=dict(id=id,title=title,ISBN=issbn, author=author)


	books.append(book)
	return jsonify({'message':'Success'})

# books.remove
	


if __name__ == '__main__':
	app.run(debug=True)

	# if len(bookId)<1:
	# 	return jsonify({'message':'Sorry! There no books found'}), 200
