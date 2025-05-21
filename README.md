# Web Services and Applications Project

Author: Irene Kilgannon

Student ID: G00220627

This is my repository for the Big Project for the semester three module, _Web Services and Applications_ for a [Higher Diploma in Science in Computing in Data Analytics](https://www.atu.ie/courses/higher-diploma-in-science-data-analytics) at [Atlantic Technological University](https://www.atu.ie/). 

This project is worth 60% of the overall marks. Deadline 26th May 2025.

__Project Brief__

Write a program that demonstrates that you understand creating and consuming RESTful APIs. 

Create a Web application in Flask that has a RESTful API, the application should link to one or more database tables.
You should also create the web pages that can consume the API i.e. performs CRUD operations on the data. 

[Full project description on GitHub.](https://github.com/andrewbeattycourseware/WSAA-Courseware/blob/main/labs/WSAA%20Project%20Description.pdf)

__Project Overview__

My hobby is dressmaking and I have an extensive collection of sewing patterns. I also have four relatives who sew, and a common question in our group chat is "Does anyone have pattern X?". 

The aim of this project is to create a MySQL database of sewing patterns that makes it easy to search and manage our combined collection. The database has two tables, users and patterns. 

The project uses a MySQL database to store patterns and user data. The backend is built with Python Flask, which provides a RESTful API for interacting with the database. The frontend uses HTML, JavaScript and Ajax to create the interface that allows the users to interact with the database. 

Users can register to receive a unique UserID. Once registered, they can add, update and delete patterns in the database. All users can view the complete collection and use various filters to search by patternID, brand, fabric type, category, format, description or userID. 

Each column can be sorted alphabetically by clicking on the column header - click again to reverse the sorting order!

The project can be run locally and it is also deployed at [irenekilgannon2.eu.pythonanywhere.com](https://irenekilgannon2.eu.pythonanywhere.com/). The gitHub repository for the deployed project is available [here](https://github.com/IreneKilgannon/deploytopythonanywhere).


__Project Structure__

    ├── static/                 # CSS file and png images for the project.
    ├── templates/              # HTML templates.
    ├── .gitignore              # Files that github ignores.
    ├── .config.py              # A hidden file with credentials required access the database.
    ├── .venv                   # Hidden virtual environment.
    ├── config_template.py      # Template of the config file.
    ├── create_db.py            # Python file to create the sewing_patterns database.
    ├── create_tables.py        # Python file to create users and patterns table for the sewing_patterns database.
    ├── db.sql                  # SQL file with create table commands for the users and patterns tables.
    ├── PatternDAO.py           # Module with the functions required to query the patterns table. 
    ├── README.md               # Main repository overview (this file).
    ├── requirements.txt        # Packages required to run the project.
    ├── server.py               # The main project file.
    ├── testPatterDAO.py        # Python file to test the functions in PatternDAO.py.
    └── UserDAO.py              # Module with the functions required to query the users table.


__Getting Started__

Download and install the following:

* [Anaconda](https://www.anaconda.com/download)

* [WAMPServer](https://www.wampserver.com/en/)

* [Cmder](https://cmder.app/)

* [Visual Studio Code](https://code.visualstudio.com/)

In Cmder or the terminal of VS code, clone the project from GitHub on your machine:

    git clone https://github.com/IreneKilgannon/wsaa-project.git


__Usage__

Note: the commands are for a Windows machine.

In Cmder, navigate to the project directory and create a virtual environment:

    python -m venv .venv

Activate the virtual environment:

    .venv\Scripts\activate

Install requirements.txt:

    pip install -r requirements.txt

Open WAMP and start MySQL console.

Create the file, `config.py` using `config_template.py`. Add your user and password to access WAMP server. Ensure that there is no database name in the database row i.e.  ``'database':""`` 

Add ``config.py`` to the .gitignore so that it does not get pushed to GitHub. 

In Cmder, run the script, `create_db.py` to create the database, sewing_patterns:

    python create_db.py

Alternatively in MySQL console, run:

    CREATE DATABASE sewing_patterns;

Update `config.py` with the database name, ``sewing_patterns``.

In Cmder, run the script, ``create_tables.py`` to create the the tables, users and patterns. 

Alternatively, in the MySQL console, create the tables, users and patterns. The file, `db.sql` contains the MySQL commands to create the tables. Copy and paste the each table separately into the MySQL console. Confirm the tables exist with the command `describe tables;` 

Run the python script:

    python server.py

The project should now be available to view in your browser, http://127.0.0.1:5000.

Upon completion, deactivate the virtual environment with the command:

    deactivate


__Known Issues__

Users can update other users profile information. 

If a user wants to update their profile, they must also update their password. 

__Future Improvements__

Login/logout functionality.

Users can only update their own information

Despite declarations of _"I'm not buying any more fabric"_, every sewist has an extensive fabric collection. A similar project to keep track of the ever-growing fabric collection would be very useful! The table for this would most definitely not include how much was spent on each piece!



__References__

https://github.com/andrewbeattycourseware/deploytopythonanywhere

https://github.com/andrewbeattycourseware/WSAA-Courseware

https://stackoverflow.com/questions/15735450/images-as-links-in-mysql-database

Render templates Flask for beginners 2 (how to render HTML templates) https://www.youtube.com/watch?v=LuuSFH-RuBU

YouTube Tech with Tim Flask Tutorial #2 - HTML Template https://www.youtube.com/watch?app=desktop&v=xIgPMguqyws&t=286s

HTML & CSS Full Course for free, Bro Code, YouTube

Modern Responsive Table Using DataTable, Step by step guide devRasen https://www.youtube.com/watch?v=1CPli6lkKCY

How to use MySQL Database with Flask, Codemy.com https://www.youtube.com/watch?v=hQl2wyJvK5k

W3 Schools How to - Sort a Table https://www.w3schools.com/howto/howto_js_sort_table.asp

https://fontawesome.com/icons

https://www.w3schools.com/bootstrap5/index.php

W3 Schools How To Filter/Search Table https://www.w3schools.com/howto/howto_js_filter_table.asp

ChatGPT: Create a basic python flask api with javascript and ajax and explain how it works.

ChatGPT: How do I render different templates for Python Flask API?

How do hash passwords in python, uses bcrypt https://www.youtube.com/watch?v=yePHM2Ks07c

YouTube, Hashing passwords with Werkzeug https://www.youtube.com/watch?v=8ebIEefhBpM

YouTube Password Hashing in Flask Using Werkzeug, Pretty Printed https://www.youtube.com/watch?v=jJ4awOToB6k

Navbar Bootstrap5 Bootstrap Navbar Tutorial, Adrian Twarog, https://www.youtube.com/watch?v=qNifU_aQRio

ChatGPT How can I check form validity in HTML? 

https://www.tutorialspoint.com/how-to-submit-a-form-on-enter-button-using-jquery?


https://getbootstrap.com/docs/5.3/components/alerts/

https://www.w3schools.com/bootstrap5/bootstrap_alerts.php?

https://www.geeksforgeeks.org/how-to-create-dismissible-alerts-in-bootstrap

[Stackoverflow, preventing negative input numbers](https://stackoverflow.com/questions/7372067/is-there-any-way-to-prevent-input-type-number-getting-negative-values)

https://stackoverflow.com/questions/9139075/how-to-show-a-confirm-message-before-delete

https://codedamn.com/news/frontend/how-to-put-image-and-text-side-by-side-in-html


bootstrap modal https://www.sitepoint.com/understanding-bootstrap-modals/

https://getbootstrap.com/docs/5.0/components/modal/

https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_delete_modal