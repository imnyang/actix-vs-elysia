# My Actix Web App

This is a simple web application built using Actix Web framework in Rust. The application demonstrates basic routing, handling GET and POST requests, and working with JSON data.

## Project Structure

```
my-actix-web-app
├── src
│   ├── main.rs         # Entry point of the application
│   ├── handlers        # Contains handler functions for routes
│   ├── routes          # Sets up routing for the application
│   └── models          # Defines data structures and models
├── Cargo.toml          # Project configuration and dependencies
└── README.md           # Documentation for the project
```

## Getting Started

### Prerequisites

- Rust and Cargo installed on your machine. You can install them from [rustup.rs](https://rustup.rs/).

### Running the Application

1. Clone the repository or download the project files.
2. Navigate to the project directory:
   ```
   cd my-actix-web-app
   ```
3. Build and run the application:
   ```
   cargo run
   ```
4. Open your web browser and go to `http://localhost:3000` to see the application in action.

## Functionality

- The application listens on port 3000.
- It handles GET and POST requests.
- Supports JSON request bodies and parameters.

## License

This project is licensed under the MIT License.