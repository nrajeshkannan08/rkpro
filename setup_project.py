import os

folders = [
    "templates",
    "static",
    "static/css",
    "static/js",
    "static/images"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

files = [
    "app.py",
    "templates/base.html",
    "templates/index.html",
    "templates/about.html",
    "templates/services.html",
    "templates/technologies.html",
    "templates/process.html",
    "templates/industries.html",
    "templates/contact.html",
    "static/css/style.css",
    "static/js/main.js"
]

for file in files:
    open(file, "w").close()

print("rk software services Project Created Successfully")