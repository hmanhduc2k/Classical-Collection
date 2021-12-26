# Classical-Collection

Classical Collection is a web database and web MP3 player specific to Western classical music. It aims to document notable composers of classical music, their works,
and serve as a platform to play their works. Kind of like Spotify, but with a more narrowed scope.


This project is my submission for the course CS50 Web Programming in Python and JavaScript offered by Harvard.

## Distinctiveness and Complexity
Classical Collection has some of its minor concepts inspired from the previous projects, but the overarching concepts are completely unique. It is somewhat a crossover of
YouTube and Spotify for music playing and documentation of classical music. It is not an e-commerce website and utilize no relevant concepts to e-commerce except for commenting functions. Similarly, this is not a social network media website except for the commenting and upvoting function which is similar but slightly more complex.
In addition, Classical Collection is notably more complex than all of my previous 5 projects. The following are the evidence for this claim:


1. The Application has 8 different models. This includes:
    - User (for authentication purpose)
    - Composer (representing a composer of classical music)
    - Piece (representing a classical music composition)
    - Favorite (representing a list of user's favorite composer and pieces)
    - Period (representing the classical music era the works are written in)
    - Difficulty (if applicable for piano, representing how difficult the composition is)
    - Comment (representing a comment on each musical piece)
    - Upvote (representing likes for comment)
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
    - Unit testing and Integration Testing
    - Documentation (through README.md)
6. Utilize various advanced and new concepts of Python and Computer Science, such as:
    - Regex matching
    - Similarity ratio

## Files

## How to run the application

## Additional Information

## Comprehensive list of features:
1. Authentication (including password strength check)
2. Uploading or View a Composer
3. Uploading or View a Piece
4. Play the MP3 file and controls them by various means (volume, timestamp, downloading, muting...)
5. Write, update, and delete comments on each pieces of music
6. Upvoting comments
7. Sort comments by upvote count and/or time posted
8. Sort pieces by period of composition
9. Sort pieces by level of difficulties
10. Filter search a composer or a piece

## Plan for future extension (Post-CS50W grading):
1. Adding CI/CD pipeline and utilizing GitHub Actions
2. Add GUI Web Testing
3. Deployment using Heroku/Netlify or other web-hosting services
4. Incorporating Cloud database for media uploading
5. More extension features and possible usage of AI/ML
