
# Scrapy Trip.com Project

## Description

This project scrapes hotel information from Trip.com and stores it in a PostgreSQL database.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/scrapy_trip_project.git
   cd scrapy_trip_project
Create a Virtual Environment

bash
Copy code
python -m venv env
source env/bin/activate
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Configure PostgreSQL Database

Ensure PostgreSQL is installed and running. Update DATABASE settings in scrapy_trip_project/settings.py.

Run the Spider

bash
Copy code
python run_spider.py
Access the Data

Data is stored in the trip table of the configured PostgreSQL database. Images are stored in the images directory.

Acceptance Criteria
Uses Scrapy Spider.
Data is stored in PostgreSQL using SQLAlchemy.
Table and image directory are created automatically.
Image references are stored in the database.
GitHub repo is public with a README.md containing setup instructions.
Deadline
12th August 2024, Monday 11:30 AM.

csharp
Copy code

### Step 8: Finalize and Push to GitHub

1. **Initialize a Git Repository**

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
Create a Repository on GitHub

Create a new repository on GitHub and follow the instructions to push your local repository to GitHub.

Push to GitHub

bash
Copy code
git remote add origin https://github.com/yourusername/scrapy_trip_project.git
git push -u origin master
