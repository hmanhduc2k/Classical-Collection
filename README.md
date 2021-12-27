# Classical-Collection

Classical Collection is a web database and web MP3 player specific to Western classical music. It aims to document notable composers of classical music, their works,
and serve as a platform to play their works. Kind of like Spotify, but with a more narrowed scope.


This project is my submission for the course CS50 Web Programming in Python and JavaScript offered by Harvard.

## Distinctiveness and Complexity
Classical Collection has some of its minor concepts inspired from the previous projects, but the overarching concepts are completely unique. It is somewhat a crossover of
YouTube and Spotify for music playing and documentation of classical music. It is not an e-commerce website and utilize no relevant concepts to e-commerce except for commenting functions. Similarly, this is not a social network media website except for the commenting and upvoting function which is similar but slightly more complex.
In addition, Classical Collection is notably more complex than all of my previous 5 projects. The following are the evidence for this claim:


1. The Application has 8 different models. This includes:
    - User (entity, for authentication purpose)
    - Composer (entity, representing a composer of classical music)
    - Piece (entity, representing a classical music composition)
    - Favorite (relation, representing a list of user's favorite composer and pieces)
    - Period (entity, representing the classical music era the works are written in)
    - Difficulty (entity, if applicable for piano, representing how difficult the composition is)
    - Comment (relation, representing a comment on each musical piece)
    - Upvote (relation, representing likes for comment)
2. The application uses HTML, CSS, and JavaScript for front-end user interaction. For the back-end, it uses Django, Python, and SQLite3 database.
3. Users can post a classical music composer and post a work of the composer themselves, including a MP3 file for the piece they are uploading which will be controlled
and used by the web application to play the music. Users can also choose to add the composers and pieces to their personal favorite or remove them. In each pieces, users
have the option to write a comment, read others' comments, edit their comment, or delete their comments (basic CRUD functionalities). In addition, users can filter search
a composer or a piece of work, and they can sort the comment by time and upvote for their convenience.
4. Good practice of User Interfaces are implemented - with application of the Single-Page-Application principle and usage of Pagination to limit the number of entries shown.
5. Utilize good practices of software engineering. This includes:
    - Package restructure and organization
    - Some adherence to OOP principle and design pattern of SWE
    - Code quality
    - Some Unit Testings
    - Documentation (through README.md)
6. Utilize various advanced and new concepts of Python and Computer Science, such as:
    - Regular expression matching
    - Similarity ratio

## How to run the application
0. Prerequisites:
    - Have a web browser that supports MP3 reading/loading/playing
    - Is connected to the Internet
    - Have installed Django and Python to the computer. The application is developed using Python 3.9.5 and Django 3.2.6 and can work on any version higher on that
1. Access the inner files of Classical-Collections, run `python manage.py makemigrations`, then run `python manage.py migrate`
2. Run `python manage.py runserver`, and access the local host `http://127.0.0.1:8000` to use the web application

Should there be any problems running the files, please make sure that Django and Python are installed to the system. Alternatively, you can run `python3` instead of `python` if you are using Linux/Ubuntu.

## Comprehensive list of features:
1. Authentication (including password strength check for registration)
    * Rule: Password must have at least 8 characters, must not be >90% similar to username, and must contain at least an alphanumeric character and a special character
2. Uploading or View a Composer
3. Uploading or View a Piece
4. Play the MP3 file and controls them by various means (volume, timestamp, downloading, muting...)
5. Write, update, and delete comments on each pieces of music
6. Upvoting comments
7. Filter search a work by period of composition, difficulty, or query
8. Filter search a composer or a piece by query
9. View, save, or remove favorite composers/pieces from personal list
10. View description of difficulty or periods of composition

## Plan for future extension (Post-CS50W grading):
1. Adding CI/CD pipeline and utilizing GitHub Actions
2. Add GUI Web Testing
3. Deployment using Heroku/Netlify or other web-hosting services
4. Incorporating Cloud database for media uploading
5. More extension features and possible usage of AI/ML

## File structure

### Python files:
1. `models.py`: Create the models for Django entities and relations
2. `urls.py`: Create the urls for the view of the web application
3. View files, set on a subdirectory of ClassColl:
    - `Attributes.py`: Deal with the model `Period` and `Difficulty` and their related views
    - `Authentication.py`: Deal with user login, logout, and registration of account
    - `Composers.py`: Deal with the composer pages (all composers, single composers,...)
    - `Discussion.py`: Deal with user interaction activities like Comments and Upvote
    - `Index.py`: Deal with the landing page (home page)
    - `Pieces.py`: Deal with the musical work page (list all works and list a single work)
    - `UserFavorite.py`: Deal with the favorite works and composers of a user
4. Utility files, set on a subdirectory of ClassColl:
    - `ComposerSearch.py`: Search for a composer with the nearest similarity to the user input
    - `PasswordStrength.py`: Assert the minimal strength of a password that user is registering for
5. Test files (to be added later on...)

### HTML files:
1. All available HTML files:
    - `all_composers.html`: list all composers on the page (with pagination)
    - `all_pieces.html`: list all musical works on the page (with pagination)
    - `composer.html`: list the details of a composer and his related works
    - `difficulty.html`: list the difficulty of a musical work by the dropdown select button
    - `error.html`: if user search for an invalid query related to composer or piece
    - `favorite.html`: list the user favorite pieces and composers
    - `index.html`: redirect the landing page with the randomized and about content
    - `layout.html`: the root structure of the HTML content, including a top nav-bar
    - `login.html`: redirect users to a login page to signin the web application
    - `period.html`: list the period of a musical work by the dropdown select button
    - `piece.html`: list the details of a piece of music and its comments/upvotes
    - `register.html`: redirect users to a registration page to create a new account
    - `pagination.html`: serves as a common template for pagination purposes

### JavaScript files:
1. All available JavaScript files:
    - `all_composers.js`: interact with the all_composers page to hide and show the views when buttons are clicked
    - `all_pieces.js`: interact with the all_pieces page to hide and show the views when buttons are clicked
    - `composer.js`: interact with the button to add favorite, hide and show content as requested
    - `favorite.js`: interact to show the favorite composers or pieces
    - `piece.js`: interact to show the piece, comment, edit comment, delete comment, or upvote a comment as requested...

## Acknowledgements: