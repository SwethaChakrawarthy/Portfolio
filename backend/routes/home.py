from flask import Blueprint, render_template, request
# from flask_login import login_required

home_bp = Blueprint('home', __name__)

movies = [
    {
        "id": 1,
        "title": "EDUCATION",
        "poster": "EDUCATION.png",
        "description": "A group of kids uncover supernatural forces and secret experiments.",
        "genre": "Sci-Fi, Drama",
        "rating": "8.7"
    },
    {
        "id": 2,
        "title": "SKILLS",
        "poster": "SKILLS.jpg",
        "description": "A chemistry teacher turns to making meth to provide for his family.",
        "genre": "Crime, Drama",
        "rating": "9.5"
    },
    # Add more as needed...
    {
        "id": 3,
        "title": "EXPERIENCE",
        "poster": "EXPERIENCE.png",
        "description": "A chemistry teacher turns to making meth to provide for his family.",
        "genre": "Crime, Drama",
        "rating": "9.5"
    },
    {
        "id": 4,
        "title": "PROJECTS",
        "poster": "EXPERIENCE.png",
        "description": "A chemistry teacher turns to making meth to provide for his family.",
        "genre": "Crime, Drama",
        "rating": "9.5"
    },
    

]

@home_bp.route('/')
# @login_required
def home():
    query = request.args.get('q')
    if query:
        filtered_movies = [m for m in movies if query.lower() in m['title'].lower()]
    else:
        filtered_movies = movies
    return render_template('index.html', movies=filtered_movies, query=query)
@home_bp.route('/movie/<int:movie_id>', endpoint='movie_detail')
# @login_required
def show_movie(movie_id):
    selected_movie = next((m for m in movies if m["id"] == movie_id), None)
    if not selected_movie:
        return "Movie not found", 404
    return render_template('movie_detail.html', movie=selected_movie)

@home_bp.route('/education')
# @login_required
def education():
    return render_template('education.html')

@home_bp.route('/skills')
# @login_required
def skills():
    return render_template('skills.html')

@home_bp.route('/experience')
# @login_required
def experience():
    return render_template('experience.html')

@home_bp.route('/projects')
# @login_required
def projects():
    return render_template('projects.html')
