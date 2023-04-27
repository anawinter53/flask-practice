from application import app, db
from application.models import Movie
from application.forms import MovieForm
from flask import request, jsonify, render_template, redirect, url_for


@app.route('/')
def hello():
    return "Hey!"

@app.route('/createForm', methods=['GET','POST'])
def create_movie():
    form = MovieForm()

    if form.validate_on_submit():
        movie = Movie(title=form.title.data, description=form.description.data, date_of_release=form.date_of_release.data)
        db.session.add(movie)
        db.session.commit()

        return redirect(url_for('get_movies'))

    return render_template('create.html', form=form)

def format_movie(movie):
    return {
        "id": movie.id,
        "title": movie.title,
        "description": movie.description,
        "date_of_release": movie.date_of_release
    }

@app.route('/movies')
def get_movies():
    movies = Movie.query.all()
    movies_list = []
    for movie in movies:
        movies_list.append(format_movie(movie))
    return render_template('movies.html', movies=movies_list, title='Movies')

@app.route('/movies/<id>')
def get_movie(id):
    movie = Movie.query.filter_by(id=id).one()
    return render_template('movie.html', movie=format_movie(movie))
    # return jsonify(id=movie.id, title=movie.title, description=movie.description, date_of_release=movie.date_of_release)

@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.filter_by(id=id).one()

    db.session.delete(movie)
    db.session.commit()

    return "Movie deleted!"

@app.route('/movies/<id>', methods=['PATCH'])
def update_movie(id):
    movie = Movie.query.filter_by(id=id)

    title = request.json['title']
    description = request.json['description']
    date_of_release = request.json['date_of_release']

    movie.update(dict(title=title, description=description, date_of_release=date_of_release))

    db.session.commit()

    updatedMovie = movie.one()
    return jsonify(id=updatedMovie.id, title=updatedMovie.title, description=updatedMovie.description, date_of_release=updatedMovie.date_of_release)
