# Flask PostgreSQL Docker Demo

A simple Flask application with PostgreSQL database running in Docker containers.

## Prerequisites
- Docker
- Docker Compose

## Setup
1. Clone this repository
2. Create `.env` file (optional) with your preferred credentials:
   ```
   POSTGRES_USER=youruser
   POSTGRES_PASSWORD=yourpassword
   POSTGRES_DB=yourdb
   ```

## Running the Application
```bash
docker-compose up -d
```

The application will be available at: http://localhost:5000

## Stopping the Application
```bash
docker-compose down
```

## Database Persistence
Data is persisted in a Docker volume named `postgres_data`.

## Initial Database Setup
You may want to connect to the database and create the `books` table:
```sql
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL
);

INSERT INTO books (title, author) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald'),
('1984', 'George Orwell');
```
Everything done here is explained in details on my mediums account
https://medium.com/@divyln20/containerize-a-web-app-using-docker-compose-5a8b40cc706d