# Django Blog Application

This Django application is a simple blog system that allows users to register, create blog posts, and view posts with various functionalities. Below are the features and setup instructions for using this application.

## Features

1. **User Authentication:**

   - Users can register, log in, and log out.

2. **Blog Post Management:**

   - Registered users can create, edit, and delete their own blog posts.
   - Each blog post has a title, content, publication date, and author.

3. **Blog Post Viewing:**

   - Visitors can view all blog posts sorted by publication date with pagination (10 posts per page).

4. **Search Functionality:**

   - Users can search for posts by title or content.

5. **RESTful APIs:**
   - Exposed APIs for CRUD operations on blog posts.
     - **List API:** Open to all users.
     - **Create, Read, Update, Delete APIs:** Require authentication.
     - **Authentication API:** Used for user registration, login, and logout.

## Setup Instructions

### Prerequisites

- Python (3.x recommended)
- Django (5.x)
- SQLite database or MySQL

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/vishnu-c-b/SIMPLE-BLOG

   ```

2. **Navigate to the project directory:**

   ```bash
   cd SIMPLE-BLOG
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Migrate database:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

6. **Access the admin interface:**
   - Navigate to `http://localhost:8000/admin/` and log in with the superuser account created earlier.
   - Here you can manage users, blog posts, and other site content.

## Usage

- **Register:** Visit `/api/blog/register/` to create a new user account.

- **Login:** Access `/api/blog/login/` to log in with your credentials.

- **Create Blog Post:** After logging in, visit `/api/blog/posts/create/` to create a new blog post.

- **View Blog Posts:** Navigate to `/api/blog/posts/` to see all published blog posts.

- **Search:** Use the search box on the homepage or visit `/api/blog/posts/?q=query` to search for posts by title or content.

## API Endpoints

- **List Blog Posts:** `GET /api/posts/`

- **Create Blog Post:** `POST /api/posts/`

- **Retrieve Blog Post:** `GET /api/blog/posts/<post_id>/`

- **Update Blog Post:** `PUT /api/blog/posts/<post_id>/update/`

- **Delete Blog Post:** `DELETE /api/blog/posts/<post_id>/delete/`

- **User Registration:** `POST /api/blog/register/`

- **User Login:** `POST /api/blog/login/`

- **User Logout:** `POST /api/blog/logout/`

## Access the API Endpoints in Postman:

## Accessing the API Endpoints in Postman

Follow these steps to interact with the API using Postman:

1. **Import the provided Postman collection:**

   - Click on the following button to view the Postman documentation:

     [![Postman](https://run.pstmn.io/button.svg)](https://documenter.getpostman.com/view/33931821/2sA3duGtgV)

2. **Set up the environment in Postman:**

   - After importing the collection, set up your environment variables, such as the base URL (`http://127.0.0.1:8000`).

3. **Obtain an authentication token:**

   - Use the provided credentials/use your own details to log in and obtain an authentication token.

4. **Authenticate requests:**

   - Set the obtained authentication token in the Authorization header of your requests to authenticate.
   - Example Authorization : Token (obtained token)

5. **Send requests using example data:**
   - Explore the endpoints documented in the collection and use the example data provided in the documentation as test inputs.

## Technical Requirements

- Django and Django REST Framework
- RESTful API design
- Django ORM for database interactions
- Token-based authentication
- Thorough documentation for each API endpoint
