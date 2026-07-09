import os

os.makedirs("templates", exist_ok=True)

base_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>rk software services </title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">

<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
<div class="container">
<a class="navbar-brand" href="/">rk software services</a>

# <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#nav">
<button id="topBtn" class="btn btn-primary">
<span class="navbar-toggler-icon"></span>
</button>

<div class="collapse navbar-collapse" id="nav">
<ul class="navbar-nav ms-auto">

<li class="nav-item"><a class="nav-link" href="/">Home</a></li>
<li class="nav-item"><a class="nav-link" href="/about">About</a></li>
<li class="nav-item"><a class="nav-link" href="/services">Services</a></li>
<li class="nav-item"><a class="nav-link" href="/technologies">Technologies</a></li>
<li class="nav-item"><a class="nav-link" href="/process">Process</a></li>
<li class="nav-item"><a class="nav-link" href="/industries">Industries</a></li>
<li class="nav-item"><a class="nav-link" href="/contact">Contact</a></li>

</ul>
</div>
</div>
</nav>

{% block content %}
{% endblock %}

<footer class="bg-dark text-white text-center py-4 mt-5">
<div class="container">
<h5>rk software services </h5>
<p>Software Development & Technology Solutions Division</p>
<p>© 2026 All Rights Reserved.</p>
</div>
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="{{ url_for('static', filename='js/client-form.js') }}"></script>

</body>
</html>
"""

pages = {
"index.html": """
{% extends 'base.html' %}
{% block content %}
<section class="py-5 bg-light text-center">
<div class="container">
<h1>rk software services </h1>
<p>Software Development & Technology Solutions Division</p>
<a href="/services" class="btn btn-primary">Explore Services</a>
</div>
</section>
{% endblock %}
""",

"about.html": """
{% extends 'base.html' %}
{% block content %}
<div class="container py-5">
<h2>About Us</h2>

<h4>Mission</h4>
<p>To provide innovative, secure, and scalable software solutions that help businesses embrace digital transformation and achieve sustainable growth.</p>

<h4>Vision</h4>
<p>To become a trusted global technology partner recognized for excellence in software development, innovation, and customer success.</p>
</div>
{% endblock %}
""",

"services.html": """
{% extends 'base.html' %}
{% block content %}
<div class="container py-5">
<h2>Our Services</h2>

<ul class="list-group">
<li class="list-group-item">Custom Software Development</li>
<li class="list-group-item">Web Application Development</li>
<li class="list-group-item">Website Development</li>
<li class="list-group-item">Mobile Application Development</li>
<li class="list-group-item">UI/UX Design</li>
<li class="list-group-item">API Development & Integration</li>
<li class="list-group-item">Database Design & Management</li>
</ul>
</div>
{% endblock %}
""",

"technologies.html": """
{% extends 'base.html' %}
{% block content %}
<div class="container py-5">
<h2>Technologies We Use</h2>

<h4>Frontend</h4>
<p>HTML5, CSS3, JavaScript, TypeScript, React.js, Next.js, Tailwind CSS</p>

<h4>Backend</h4>
<p>Node.js, Express.js, Java, Spring Boot, Python, PHP</p>

<h4>Database</h4>
<p>MySQL, PostgreSQL, MongoDB</p>

<h4>Cloud & DevOps</h4>
<p>AWS, Docker, GitHub, CI/CD Pipelines, Linux Servers</p>
</div>
{% endblock %}
""",

"process.html": """
{% extends 'base.html' %}
{% block content %}
<div class="container py-5">
<h2>Development Process</h2>

<ol>
<li>Requirement Analysis</li>
<li>Planning & Strategy</li>
<li>UI/UX Design</li>
<li>Development</li>
<li>Testing & Quality Assurance</li>
<li>Deployment</li>
<li>Maintenance & Support</li>
</ol>
</div>
{% endblock %}
""",

"industries.html": """
{% extends 'base.html' %}
{% block content %}
<div class="container py-5">
<h2>Industries We Serve</h2>

<div class="row">

<div class="col-md-3 mb-3"><div class="card"><div class="card-body">Education</div></div></div>

<div class="col-md-3 mb-3"><div class="card"><div class="card-body">Healthcare</div></div></div>

<div class="col-md-3 mb-3"><div class="card"><div class="card-body">Manufacturing</div></div></div>

<div class="col-md-3 mb-3"><div class="card"><div class="card-body">Retail</div></div></div>

<div class="col-md-3 mb-3"><div class="card"><div class="card-body">E-Commerce</div></div></div>

<div class="col-md-3 mb-3"><div class="card"><div class="card-body">Logistics</div></div></div>

<div class="col-md-3 mb-3"><div class="card"><div class="card-body">Real Estate</div></div></div>

<div class="col-md-3 mb-3"><div class="card"><div class="card-body">Hospitality</div></div></div>

</div>
</div>
{% endblock %}
""",

"contact.html": """
{% extends 'base.html' %}
{% block content %}
<div class="container py-5">

<h2>Contact Us</h2>

<p><strong>rk software services </strong></p>

<p>
5th Floor, SBRR Square,<br>
Anna Nagar,<br>
Tiruchirappalli – 620017,<br>
Tamil Nadu, India
</p>

<p>Phone: +91 7418240526</p>

<p>Email: rksoftwareservices@gmail.com</p>

<p>Website: www.rksoftwareservices.in</p>

</div>
{% endblock %}
"""
}

with open("templates/base.html", "w", encoding="utf-8") as f:
    f.write(base_html)

for filename, content in pages.items():
    with open(f"templates/{filename}", "w", encoding="utf-8") as f:
        f.write(content)

print("All HTML files generated successfully.")