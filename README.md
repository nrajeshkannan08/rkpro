# rkpro

A Python Flask-based web application for managing client requirements, company services, and candidate applications.

## Features
- **Client Requirements Form**: Dynamic inputs to gather clients' project specifications, technologies, budget, timeline, and document attachments.
- **Client List**: Panel to review submitted client requests.
- **Candidate Registration**: Portal for job candidates to apply, submit details, and upload resumes.
- **MySQL Integration**: Persistent backend database using `Flask-MySQLdb`.
- **Responsive Layout**: Modern, clean design templates.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/nrajeshkannan08/rkpro.git
   cd rkpro
   ```

2. **Set up Virtual Environment**:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/macOS
   source .venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Configuration**:
   - Ensure you have MySQL running locally.
   - Update the configuration values in `app.py` for database host, user, password, and database name.
   - Import/create the required schemas for `client_requirements`, `candidates`, etc.

5. **Run the Application**:
   ```bash
   python app.py
   ```
