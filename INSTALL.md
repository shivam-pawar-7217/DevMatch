# Installation & Setup Guide

This project is fully containerized with Docker, meaning you do not need to install Python, Node.js, or PostgreSQL on your local machine to run it.

## Prerequisites
1. **Git** (to clone the repository)
2. **Docker Desktop** (must be installed and running on your machine)

## How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/shivam-pawar-7217/DevMatch.git
   cd DevMatch
   ```

2. **Start the containers**
   Run the following command in the root directory. This will download the necessary base images, install all dependencies, initialize the database, and start the network.
   ```bash
   docker-compose up --build
   ```

3. **Access the Application**
   Once the terminal shows that both the backend and frontend servers are running, open your web browser:
   - **Frontend UI:** `http://localhost:3000`
   - **Backend API:** `http://localhost:8000`

---

## Stopping & Resetting

- **To gracefully stop the application:** 
  Press `Ctrl + C` in the terminal where Docker is running, or run:
  ```bash
  docker-compose down
  ```

- **To perform a full hard reset:**
  If you want to completely wipe the database and start from a completely clean slate (for example, to re-run the seed files), use the `-v` flag to destroy the volumes before rebuilding:
  ```bash
  docker-compose down -v
  docker-compose up --build
  ```

## Environment Variables
*Note: You do not need to manually create any `.env` files. All necessary development environment variables (like database credentials and ports) are safely handled and injected directly via the `docker-compose.yml` file.*
