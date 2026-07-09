import os
import cssbeautifier

css_dir = "static/css"

for root, dirs, files in os.walk(css_dir):
    for file in files:
        if file.endswith(".css"):

            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:
                css = f.read()

            fixed = cssbeautifier.beautify(css)

            with open(path, "w", encoding="utf-8") as f:
                f.write(fixed)

            print(f"Fixed: {path}")

print("All CSS files optimized")