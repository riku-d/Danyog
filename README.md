# Danyog

Danyog is a web-based platform designed to connect people who want to donate unused items with orphanages that can benefit from these donations. By facilitating this exchange, Danyog aims to bring smiles to those in need by repurposing items that would otherwise go unused. You can visit the live site [here](https://danyog.onrender.com/).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/riku-d/Danyog.git
   cd Danyog
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database (using SQLite3):
   ```bash
   python manage.py migrate
   ```

5. Run the application:
   ```bash
   python manage.py runserver
   ```

## Usage

- Visit the live site: [Danyog](https://danyog.onrender.com/).
- Users can log in to donate items they no longer need, such as clothing, books, toys, and more.
- Orphanages can log in to browse listed items and place orders for items they need.

## Features

- **User Login & Registration**: Allows both donors and orphanages to create accounts and log in.
- **Donation Listings**: Donors can list items for donation, including details and images.
- **Order Requests**: Orphanages can request items listed by donors.
- **SQLite3 Database**: The platform uses SQLite3 for efficient data storage and retrieval.

## Screenshots

![Danyog Screenshot](screenshots/danyog_main.png)
*Include screenshots to highlight donation listings, orphanage orders, and the user interface.*

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Created by [riku-d](https://github.com/riku-d). For questions, reach out via email at [rohitdutta2103@gmail.com](mailto:rohitdutta2103@gmail.com).
