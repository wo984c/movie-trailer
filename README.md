# Movie Trailer Website

Website where users can see your favorite movies and watch the trailers.

## Quick Start

Clone the repo: git clone https://github.com/wo984c/movie-trailer.git

## Software Requirements

Python 2.7. You can download python from [here](https://www.python.org)

## What is included

Within the download you'll find the following files:

* fresh_tomatoes.py - generates the website
* entertainment_center.py - creates a list of movie objects
* media.py - movie class

## How to create the website

1. Run `python entertainment_center.py` module - it will call the open_movies_page() contained in fresh_tomatoes.py. This function will take the list of movies and generate the index.html file

2. Set up the web server from the movies directory by executing `python -m SimpleHTTPServer 8000`

3. Enter `http://127.0.0.1:8000` on your web browser to showcase the movies.
