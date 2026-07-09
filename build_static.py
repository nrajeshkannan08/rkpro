import os
import shutil
from app import app

# Set testing mode
app.config['TESTING'] = True

# List of routes to render and their static filename outputs
routes = [
    ('/', 'index.html'),
    ('/about', 'about.html'),
    ('/services', 'services.html'),
    ('/technologies', 'technologies.html'),
    ('/process', 'process.html'),
    ('/industries', 'industries.html'),
    ('/contact', 'contact.html'),
    ('/client-form', 'client-form.html'),
    ('/candidate-form', 'candidate-form.html'),
    ('/clientcompletedetailsform', 'clientcompletedetailsform.html'),
    ('/clientrequirementform', 'clientrequirementform.html'),
]

# Create output directory
output_dir = 'dist'
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

# Copy static assets (CSS, JS, Images) to dist
if os.path.exists('static'):
    shutil.copytree('static', os.path.join(output_dir, 'static'))

# Render pages using Flask's test client
with app.test_client() as client:
    for route, filename in routes:
        print(f"Rendering {route}...")
        response = client.get(route)
        if response.status_code == 200:
            html = response.get_data(as_text=True)
            
            # Post-process links to make them static-friendly
            # Replace absolute static URL paths with relative paths
            html = html.replace('"/static/', '"static/')
            html = html.replace("'/static/", "'static/")
            
            # Replace navigation links with local file links
            html = html.replace('href="/"', 'href="index.html"')
            html = html.replace('href="/about"', 'href="about.html"')
            html = html.replace('href="/services"', 'href="services.html"')
            html = html.replace('href="/technologies"', 'href="technologies.html"')
            html = html.replace('href="/process"', 'href="process.html"')
            html = html.replace('href="/industries"', 'href="industries.html"')
            html = html.replace('href="/contact"', 'href="contact.html"')
            html = html.replace('href="/client-form"', 'href="client-form.html"')
            html = html.replace('href="/candidate-form"', 'href="candidate-form.html"')
            html = html.replace('href="/clientcompletedetailsform"', 'href="clientcompletedetailsform.html"')
            html = html.replace('href="/clientrequirementform"', 'href="clientrequirementform.html"')
            
            # Save the static HTML page
            with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
                f.write(html)
        else:
            print(f"Failed to render {route}: {response.status_code}")

print("Static build completed successfully in 'dist/' directory!")
