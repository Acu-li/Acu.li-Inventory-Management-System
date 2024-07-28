# Aculi Inventory Management System (Aculi IMS)

Aculi IMS is a web-based inventory management system designed to help you track and manage your devices efficiently. This system is built using Flask and Docker to ensure easy deployment and scalability.

## Features

- Add, view, and delete devices
- Store device information to keep track of all devices in your collection.
- ~~Persistent storage of device data using Docker volumes~~ (doesnt work idk what i did wrong, will get fixed in v2)
- Nice looking web interface
- All of that, contained in a single Docker container.

## Prerequisites

- Docker
- Docker Compose

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Acu-li/Acu.li-Inventory-Management-System.git
    cd Acu.li-Inventory-Management-System
    ```
    
2. **Build and run the application using Docker Compose:**

    ```bash
    docker-compose up -d
    ```

## Usage

- Open your web browser and go to `http://localhost:5000` to access the Aculi IMS interface.
- Use the "Add Device" form to input new device details. Click on the "Add Device" button to submit.
- View the list of devices on the main page.
- Click the delete button next to a device to remove it from the list.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or bug fixes.

## Acknowledgements

- Flask: A lightweight WSGI web application framework in Python.
- Docker: A platform for developing, shipping, and running applications in containers.

