
## Overview
This document provides documentation for the URL shortening service project discussed in the chat conversation.

## Project Description
The URL shortening service allows users to generate shortened URLs for long URLs. It provides endpoints for creating shortened URLs, retrieving original URLs from shortened ones, and tracking analytics data such as total clicks and referral sources.

## Components
### 1. `main.py`
This file contains the main FastAPI application instance and runs the ASGI server.

### 2. `routers.py`
Contains the API routers and endpoints for handling URL shortening operations.

### 3. `crud.py`
Provides CRUD (Create, Read, Update, Delete) operations for interacting with the database.

### 4. `models.py`
Defines SQLAlchemy models for database tables, including `ShortenedURL`, `URL`, and `Analytics`.

### 5. `keygen.py`
Generates short URL keys using a specified algorithm.

### 6. `database.py`
Configures the database connection using SQLAlchemy and databases library.

### 7. `schemas.py`
Contains Pydantic models for request and response validation.

### 8. `utils.py`
Utility functions used across the project.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   - Configure the database connection in `database.py`.
   - Run migrations using Alembic or SQLAlchemy to create database tables.

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

5. Access the application:
   Open a web browser and go to `http://localhost:8000` to access the application.

