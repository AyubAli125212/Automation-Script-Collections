import subprocess
import os

def create_vite_project():
     subprocess.run(["npm", "create", "vite@latest", "./react", "--", "--template", "react"], check=True)
# ./react Change to your project directory

def install_dependencies():
    subprocess.run(["npm", "install", "-D", "tailwindcss", "postcss", "autoprefixer"], check=True)

def initialize_tailwind():
    subprocess.run(["npx", "tailwindcss", "init", "-p"], check=True)

def modify_tailwind_config():
    with open("tailwind.config.js", "w") as f:
        f.write("""module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
                
  plugins: [],
};""")

def update_index_css():
    with open("src/index.css", "w") as f:
        f.write("@tailwind base;\n@tailwind components;\n@tailwind utilities;")

def create_components_folder():
    os.makedirs("src/components", exist_ok=True)

def setup_project():
    create_vite_project()
    os.chdir("./react")  # Change to your project directory
    install_dependencies()
    initialize_tailwind()
    modify_tailwind_config()
    update_index_css()
    create_components_folder()

if __name__ == "__main__":
    setup_project()
