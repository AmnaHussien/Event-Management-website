# Event Management Website

## Overview
The **Event Management Website** is a platform designed to simplify the process of organizing and managing events. It provides users with features to create, update, and manage events seamlessly. Built with Flask, the application employs a modular architecture using Blueprints, ensuring scalability and maintainability.

### Key Features:
- User Authentication (Sign Up, Login, Logout)
- CRUD Operations for Event Management
- Responsive Design using HTML and CSS
- Database Integration with MySQL using SQLAlchemy


## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Database**: MySQL (via Flask-SQLAlchemy)
- **Architecture**: Modular Flask Blueprints



## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- MySQL installed and configured
- A virtual environment tool (e.g., `venv`)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AmnaHussien/Event-Management-website.git
   cd event-management-website
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   - Create a MySQL database named `event_management`.
   - Update the database configuration in `__init__.py`:
     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/event-management-website'
     ```

5. **Run Database Migrations**:
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

6. **Run the Application**:
   ```bash
   flask run
   ```
   Open your browser and navigate to `http://127.0.0.1:5000`.

---

## Usage Guidelines

### Navigating the Website
- **Home Page**: Displays a list of all events.
- **Authentication**:
  - Sign Up for a new account.
  - Log In to access event management features.
- **Event Management**:
  - Add a New Event: Fill in event name, date added automatically.
  - Edit an Event: Update the details of an existing event.
  - Delete an Event: Remove events no longer needed.

### Form Validations
- Event titles should not exceed 50 characters.
- Event tiles should not be less than 1 character.


## Project Architecture

The project follows the **Model-View-Controller (MVC)** pattern:

1. **Model**:
   - Handled by SQLAlchemy ORM.
   - Represents database tables for users and events.

2. **View**:
   - HTML templates are rendered using Jinja2.
   - CSS provides responsive and aesthetic styling.

3. **Controller**:
   - Routes are defined using Flask.
   - Modularized using Blueprints (`auth` and `views`).

### Directory Structure:
```
├── website
│   ├── __init__.py         # Initializes the Flask app
│   ├── auth.py             # Handles authentication routes
│   ├── views.py            # Handles main application routes
│   ├── models.py           # Defines database models
│   ├── templates           # Contains HTML files
│   │   └── base.html       # Base template
|   |   |__home.html        # home template
|   |   |__about.html       # about template
|   |   |__contact.html     # contact template
|   |   |__landing.html     # landing template
|   |   |__login.html       # login template
|   |   |__signup.html      # signup template
|   |   |__update.html      # update template
|   |  
│   ├── static              # Contains CSS and assets
│       └── base.css        # Styling for the website
├── app.py                  # Entry point to run the Flask app
```

---

## Lessons Learned and Next Steps

### Successes:
- Successfully implemented user authentication and CRUD operations.
- Learned and applied modular Flask architecture with Blueprints.

### Challenges:
- Managing database relationships effectively.
- Ensuring consistent styling across devices.

### Future Improvements:
- Add calendar-based event visualization.
- Enhance user interface with advanced CSS frameworks.
- Implement email notifications for event reminders.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.
