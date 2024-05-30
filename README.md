# swiss-watches-microservices

Django Microservices

## Getting Started

Follow these steps to build and run the Docker containers for the frontend and backend microservices:

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/swiss-watches-backend.git
   ```

2. Navigate to frontend:

   ```bash
   cd frontend
   ```

2. Build the Docker image for the frontend:

   ```bash
   docker build -t frontend .
   ```

3. Run the Docker container for the frontend:

   ```bash
   docker run -p 5173:5173 frontend
   ```

4. Navigate to the backend directory:

   ```bash
   cd ../backend
   ```

5. For each app (user_management, product_management, cart), navigate to the respective directory and run the following commands:

   ```bash
   cd user_management
   docker-compose down
   docker-compose up --build
   ```

   ```bash
   cd ../product_management
   docker-compose down
   docker-compose up --build
   ```

   ```bash
   cd ../cart
   docker-compose down
   docker-compose up --build
   ```

6. Open your web browser and visit `http://localhost:5173` to see the app running.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Please replace `your-username` with your actual GitHub username in the clone command.
