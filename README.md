# DjangoMedStoreManager

## Overview

DjangoMedStoreManager is a Django-based application designed for efficiently managing a medical store. It includes both a user-friendly web interface and a RESTful API, providing seamless functionalities for handling medicine-related operations.

## Features

### Web Application

- **User Authentication:** Allows users to sign up and log in securely.
- **Medicine Management:**
  - Add, edit, and delete medicines.
  - List all available medicines.
  - Search for specific medicines.

### API

- **User Authentication:** Supports user signup and secure login.
- **Medicine Management (JSON Response):**
  - Add, edit, and delete medicines via API.
  - Retrieve a list of all medicines in JSON format.
  - Search for specific medicines via API.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KarunShaji/DjangoMedStoreManager.git
    ```
2. **Navigate to the project directory:**
   ```bash
   cd DjangoMedStoreManager
   ```
3. Install `virtualenv` (if not already installed):

    ```bash
    pip install virtualenv
    ```

4. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv env
    ```
    For Windows
    ```bash
     env\Scripts\activate
    ```
    For Linux
   ```bash
   env/bin/activate
   ```
   
5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Usage

1. Create a superuser account for initial access:

    ```bash
    python manage.py createsuperuser
    ```

2. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Access the Application:

- Open your web browser and go to [http://localhost:8000/](http://localhost:8000/) to use the web application.

## API Documentation:

For detailed API documentation, refer to the [API Documentation](http://localhost:8000/api/docs/) page. This includes information on available endpoints, request methods, and expected responses. You can also explore the API interactively using Swagger at [http://localhost:8000/api/swagger/](http://localhost:8000/api/swagger/).

## Testing with Postman:

You can use Postman to verify the functionality of the API:

1. **Install Postman:**
   - If you don't have Postman installed, you can download it [here](https://www.postman.com/downloads/).

2. **Import API Collection:**
   - Import the provided Postman collection located in the `postman` directory of this repository.

3. **Explore and Test Endpoints:**
   - The collection includes sample requests for various API endpoints.
   - Use these requests to interact with the API, send requests, and verify responses.

4. **Update Environment Variables (if needed):**
   - If your local server runs on a different port or if you have specific configurations, update the environment variables in Postman accordingly.

Feel free to experiment with different requests to ensure the API is working as expected.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
## Acknowledgements

- [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.
