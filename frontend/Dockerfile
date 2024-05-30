# Use an official Node.js runtime as the base image
FROM node:16-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock if you're using Yarn)
COPY package*.json ./

# Install dependencies
RUN npm install
RUN npm install -g vite


# Copy the rest of your app's source code
COPY . .

# Copy the Vite configuration file
COPY vite.config.js .

# Build the app
RUN npm run build

# Expose port 5173 for the app to be accessible
EXPOSE 5173

# Start the app
CMD ["npm", "run", "dev"]
