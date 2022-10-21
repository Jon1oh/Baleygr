# Baleygr

### Prerequisites

- [Python](https://www.python.org/)
<!-- - [Docker](https://www.docker.com/) -->

### Installation

1. Clone the repo
   ```sh
    git clone https://github.com/Jon1oh/Baleygr.git
   ```
2. Create and use virtual environment
   ```sh
    python -m venv .venv
    source ./.venv/bin/activate
   ```
3. Install Python packages
   ```sh
    pip install -r requirements.txt
   ```

### Usage

1. Run server
   ```sh
    python manage.py runserver
   ```
2. Edit database
   ```sh
    python manage.py makemigrations
    python manage.py migrate
   ```
