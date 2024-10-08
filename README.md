# Item Management Microservice

This is a simple microservice application for managing items. It provides basic CRUD operations through a RESTful API.

## Setup

1. Clone the repository:
   ```
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

2. Create and activate a virtual environment:
   ```
   pytho3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python src/app/main.py
   ```

The application will be available at `http://localhost:5000`.

## API Endpoints

- GET /items: Retrieve all items
- POST /items: Create a new item
- GET /items/<item_id>: Retrieve a specific item
- PUT /items/<item_id>: Update a specific item
- DELETE /items/<item_id>: Delete a specific item

## Docker

To build and run the Docker container:

1. Build the image:
   ```
   docker build -t flask-crud-app src/
   ```

2. Run the container:
   ```
   docker run -p 5000:5000 flask-crud-app
   ```

