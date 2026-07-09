import pymysql
from flask import Flask, render_template, request, redirect, flash, g
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)

app.secret_key = "ascopetech_secret_key"


app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', '')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'ascopetech')

class MySQL:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        @app.teardown_appcontext
        def teardown_db(exception):
            db = g.pop('mysql_db', None)
            if db is not None:
                try:
                    db.close()
                except Exception:
                    pass

    @property
    def connection(self):
        if 'mysql_db' not in g:
            g.mysql_db = pymysql.connect(
                host=self.app.config['MYSQL_HOST'],
                user=self.app.config['MYSQL_USER'],
                password=self.app.config['MYSQL_PASSWORD'],
                database=self.app.config['MYSQL_DB']
            )
        return g.mysql_db

mysql = MySQL(app)

# =========================
# FILE UPLOAD CONFIG
# =========================

UPLOAD_FOLDER = "static/uploads/client_requirements"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/client-form')
def client_form():
    return render_template('client_form.html')

@app.route('/client-submit', methods=['POST'])
def client_submit():

    try:

        client_name = request.form['client_name']
        company_name = request.form['company_name']
        email = request.form['email']
        mobile = request.form['mobile']
        address = request.form['address']

        project_name = request.form['project_name']
        project_type = request.form['project_type']
        project_description = request.form['project_description']
        target_audience = request.form['target_audience']
        technology = request.form['technology']

        required_features = request.form['required_features']
        pages_modules = request.form['pages_modules']
        hosting_required = request.form['hosting_required']

        budget = request.form['budget']
        deadline = request.form['deadline']

        reference_sites = request.form['reference_sites']
        additional_notes = request.form['additional_notes']

        # File Upload
        uploaded_file = ""

        file = request.files.get("requirement_file")

        if file and file.filename:

            uploaded_file = secure_filename(file.filename)

            file.save(
                os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    uploaded_file
                )
            )

        # Insert Into Database

        cur = mysql.connection.cursor()

        cur.execute("""
            INSERT INTO client_requirements(
                client_name,
                company_name,
                email,
                mobile,
                address,
                project_name,
                project_type,
                project_description,
                target_audience,
                technology,
                required_features,
                pages_modules,
                hosting_required,
                budget,
                deadline,
                uploaded_file,
                reference_sites,
                additional_notes
            )
            VALUES(
                %s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,
                %s,%s,%s
            )
        """, (

            client_name,
            company_name,
            email,
            mobile,
            address,

            project_name,
            project_type,
            project_description,
            target_audience,
            technology,

            required_features,
            pages_modules,
            hosting_required,

            budget,
            deadline,

            uploaded_file,
            reference_sites,
            additional_notes

        ))

        mysql.connection.commit()
        cur.close()

        flash(
            "Requirements submitted successfully!",
            "success"
        )

        return redirect('/client-form')

    except Exception as e:

        flash(f"Error: {str(e)}", "danger")

        return redirect('/client-form')
    
@app.route('/client-list')
def client_list():

    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT *
        FROM client_requirements
        ORDER BY id DESC
    """)

    clients = cur.fetchall()

    cur.close()

    return render_template(
        'client_list.html',
        clients=clients
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/technologies')
def technologies():
    return render_template('technologies.html')

@app.route('/process')
def process():
    return render_template('process.html')

@app.route('/industries')
def industries():
    return render_template('industries.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/candidate-form')
def candidate_form():
    return render_template('candidate_form.html')


@app.route('/candidate-submit', methods=['POST'])
def candidate_submit():

    resume = request.files['resume']

    filename = secure_filename(resume.filename)

    resume.save(
        os.path.join(
            app.config['UPLOAD_FOLDER'],
            filename
        )
    )

    cursor = mysql.connection.cursor()

    cursor.execute("""
        INSERT INTO candidates(
            first_name,last_name,email,mobile,dob,
            gender,address,tenth_percentage,
            twelfth_percentage,diploma_percentage,
            ug_degree,ug_cgpa,pg_degree,pg_cgpa,
            skills,experience,projects,resume
        )
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
               %s,%s,%s,%s,%s,%s,%s,%s)
    """, (

        request.form['first_name'],
        request.form['last_name'],
        request.form['email'],
        request.form['mobile'],
        request.form['dob'],
        request.form['gender'],
        request.form['address'],

        request.form['tenth_percentage'],
        request.form['twelfth_percentage'],
        request.form['diploma_percentage'],

        request.form['ug_degree'],
        request.form['ug_cgpa'],

        request.form['pg_degree'],
        request.form['pg_cgpa'],

        request.form['skills'],
        request.form['experience'],
        request.form['projects'],

        filename

    ))

    mysql.connection.commit()
    cursor.close()

    return redirect('/candidate-form')

@app.route('/clientcompletedetailsform')
def client_complete_details_form():
    return render_template('clientcompletedetailsform.html')

@app.route('/submit', methods=['POST'])
def submit():

    project_complete_details = request.files['project_complete_details']

    filename = secure_filename(project_complete_details.filename)

    project_complete_details.save(
        os.path.join(
            app.config['UPLOAD_FOLDER'],
            filename
        )
    )

    cursor = mysql.connection.cursor()
    

    cursor.execute("""
        INSERT INTO clientcompletedetailsform(
            client_name,company_name,email,mobile,alternate_mobile,website,
            address,city,state,pincode,project_name,project_type,
            project_description,budget,delivery_date,notes,project_complete_details
        )
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
               %s,%s,%s,%s,%s,%s,%s)
    """, ( 
          
          
        request.form['client_name'],
        request.form['company_name'],
        request.form['email'],
        request.form['mobile'],
        request.form['alternate_mobile'],
        request.form['website'],
        request.form['address'],
        request.form['city'],
        request.form['state'],
        request.form['pincode'],
        request.form['project_name'],
        request.form['project_type'],
        request.form['project_description'],
        request.form['budget'],
        request.form['delivery_date'],
        request.form['notes'],
       
       filename
    ))

    mysql.connection.commit()
    cursor.close()

    return redirect('/clientcompletedetailsform')

# Form Submission
# @app.route('/submit', methods=['POST'])
# def submit():

#     client_data = {
#         "client_name": request.form.get("client_name"),
#         "company_name": request.form.get("company_name"),
#         "email": request.form.get("email"),
#         "mobile": request.form.get("mobile"),
#         "alternate_mobile": request.form.get("alternate_mobile"),
#         "website": request.form.get("website"),
#         "address": request.form.get("address"),
#         "city": request.form.get("city"),
#         "state": request.form.get("state"),
#         "pincode": request.form.get("pincode"),
#         "project_name": request.form.get("project_name"),
#         "project_type": request.form.get("project_type"),
#         "project_description": request.form.get("project_description"),
#         "budget": request.form.get("budget"),
#         "delivery_date": request.form.get("delivery_date"),
#         "notes": request.form.get("notes")
#     }

#     print("\n===== CLIENT DETAILS =====")
#     for key, value in client_data.items():
#         print(f"{key}: {value}")

#     return """

#     <h2>Client Details Saved Successfully!</h2>
#     <a href="/">Add Another Client</a>
#     """



# # Open the form page
# @app.route('/client-form')
# def client_form():
#     return render_template('client_form.html')


# # Handle form submission
# @app.route('/client-submit', methods=['POST'])
# def client_submit():
#     client_data = {
#         "client_name": request.form.get("client_name"),
#         "company_name": request.form.get("company_name"),
#         "email": request.form.get("email"),
#         "mobile": request.form.get("mobile"),
#         "alternate_mobile": request.form.get("alternate_mobile"),
#         "website": request.form.get("website"),
#         "address": request.form.get("address"),
#         "city": request.form.get("city"),
#         "state": request.form.get("state"),
#         "pincode": request.form.get("pincode"),
#         "project_name": request.form.get("project_name"),
#         "project_type": request.form.get("project_type"),
#         "project_description": request.form.get("project_description"),
#         "budget": request.form.get("budget"),
#         "delivery_date": request.form.get("delivery_date"),
#         "notes": request.form.get("notes"),
#         "project_complete_details": request.files.get("project_complete_details")
#     }

#     print("Received client submission:", client_data)

#     # return "Client Details Saved Successfully!"
#     return render_template('client_form.html')

@app.route('/clientrequirementform')
def client_requirement_form():
    return render_template('clientrequirementform.html')


app.secret_key = "ascopetech_secret_key"

# Upload Folder
UPLOAD_FOLDER = "static/uploads/client_requirements"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create folder automatically
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ========================================
# HOME PAGE
# ========================================




# ========================================
# CLIENT REQUIREMENTS FORM PAGE
# ========================================

# @app.route("/client-form")
# def client_form():
#     return render_template("client_form.html")


# ========================================
# CLIENT FORM SUBMIT
# ========================================

# @app.route("/client-submit", methods=["POST"])
# def client_submit():

#     try:

#         # Client Information
#         client_name = request.form.get("client_name")
#         company_name = request.form.get("company_name")
#         email = request.form.get("email")
#         mobile = request.form.get("mobile")
#         address = request.form.get("address")

#         # Project Details
#         project_name = request.form.get("project_name")
#         project_type = request.form.get("project_type")
#         project_description = request.form.get("project_description")
#         target_audience = request.form.get("target_audience")
#         technology = request.form.get("technology")

#         # Features
#         required_features = request.form.get("required_features")
#         pages_modules = request.form.get("pages_modules")
#         hosting_required = request.form.get("hosting_required")

#         # Budget & Timeline
#         budget = request.form.get("budget")
#         deadline = request.form.get("deadline")

#         # References
#         reference_sites = request.form.get("reference_sites")
#         additional_notes = request.form.get("additional_notes")

#         # ====================================
#         # FILE UPLOAD
#         # ====================================

#         uploaded_filename = ""

#         requirement_file = request.files.get("requirement_file")

#         if requirement_file and requirement_file.filename != "":

#             uploaded_filename = secure_filename(
#                 requirement_file.filename
#             )

#             requirement_file.save(
#                 os.path.join(
#                     app.config["UPLOAD_FOLDER"],
#                     uploaded_filename
#                 )
#             )

#         # ====================================
#         # SAVE DATA TO TEXT FILE
#         # ====================================

#         with open(
#             "client_requirements.txt",
#             "a",
#             encoding="utf-8"
#         ) as file:

#             file.write("\n")
#             file.write("=" * 80 + "\n")

#             file.write(f"Client Name : {client_name}\n")
#             file.write(f"Company Name : {company_name}\n")
#             file.write(f"Email : {email}\n")
#             file.write(f"Mobile : {mobile}\n")
#             file.write(f"Address : {address}\n\n")

#             file.write(f"Project Name : {project_name}\n")
#             file.write(f"Project Type : {project_type}\n")
#             file.write(f"Project Description : {project_description}\n")
#             file.write(f"Target Audience : {target_audience}\n")
#             file.write(f"Technology : {technology}\n\n")

#             file.write(f"Required Features : {required_features}\n")
#             file.write(f"Pages/Modules : {pages_modules}\n")
#             file.write(f"Hosting Required : {hosting_required}\n\n")

#             file.write(f"Budget : {budget}\n")
#             file.write(f"Deadline : {deadline}\n\n")

#             file.write(f"Reference Sites : {reference_sites}\n")
#             file.write(f"Uploaded File : {uploaded_filename}\n")
#             file.write(f"Additional Notes : {additional_notes}\n")

#             file.write("=" * 80 + "\n")

#         flash(
#             "Client Requirements Submitted Successfully!",
#             "success"
#         )

#         return redirect("/")

#     except Exception as e:

#         flash(f"Error : {str(e)}", "danger")

#         return redirect("/")




if __name__ == '__main__':
    app.run(debug=True)