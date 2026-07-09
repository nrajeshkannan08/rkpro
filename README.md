# RK Software Services - Static Frontend Website

This repository is set up to build and deploy as a **pure static frontend website** on Vercel or any other static hosting platform. 

It compiles dynamic Flask / Jinja2 templates into standard static HTML, CSS, and JS files, which are hosted on a fast Global CDN without requiring a running Python/MySQL backend server.

---

## 🚀 Deployment Process to Vercel

To deploy this project to Vercel as a frontend-only static site, follow these steps:

### 1. Push to GitHub
Make sure your latest code is pushed to your GitHub repository:
```bash
git add .
git commit -m "Configure static build system for frontend deployment"
git push origin main
```

### 2. Import into Vercel
1. Go to your **[Vercel Dashboard](https://vercel.com/dashboard)**.
2. Click **Add New** > **Project**.
3. Import the repository: **`nrajeshkannan08/rkpro`**.

### 3. Configure Build Settings
During the configuration step in Vercel:
1. Expand the **Build and Development Settings** section.
2. Toggle the switches to customize the commands:
   - **Build Command**: `python build_static.py`
   - **Output Directory**: `dist`
3. Click **Deploy**.

Vercel will install Python, run the build script to compile the templates, and deploy the resulting static files in `dist/`.

---

## 🛠️ How the Build System Works

We use a Python builder script (`build_static.py`) to compile the Jinja2 templates into static HTML:
1. **Mock Rendering**: It uses Flask's test client to load and render all templates (such as `index.html`, `about.html`, etc.) in memory without requiring a database connection.
2. **Relative Paths**: It post-processes all URLs and assets:
   - Converts absolute paths like `/static/css/style.css` to relative paths (`static/css/style.css`).
   - Converts navigation routes like `/about` to local HTML pages (`about.html`).
3. **Asset Bundling**: It copies the `static/` directory containing all CSS, JS, and image assets to the build output directory (`dist/`).

### Local Development & Verification
To test the static build locally on your machine:
```bash
# Run the build script
python build_static.py
```
This will create a `dist/` folder containing the compiled website. You can open `dist/index.html` directly in your browser or serve it using any simple local server (like Live Server in VS Code).

---

## 📝 Important Note on Forms

Since the site is hosted as a **pure static frontend website**:
- **Information Pages**: All pages like Home, About, Services, Technologies, Process, and Contact work perfectly.
- **Forms**: The Client Registration, Candidate Application, and Project Details forms will render and display correctly in the browser.
- **Submissions**: Standard form submissions (`POST` actions to local backend endpoints) will fail on a static host. 
  - To make the forms functional, you can modify the `action` attribute in the HTML files inside `templates/` to point to a static form handling service (e.g., [Formspree](https://formspree.io/), [Web3Forms](https://web3forms.com/), or [Getform](https://getform.io/)), or point them to an externally hosted API backend.
