cd C:\Users\21653\PycharmProjects\pythonProject4

# Step 1: Set identity (if not done yet)
git config --global user.name "nada22-creator"
git config --global user.email "chaouachinadda3@gmail.com"

# Step 2: Initialize Git
git init

# Step 3: Stage all files
git add .

# Step 4: Commit files
git commit -m "Initial commit"

# Step 5: Rename branch to main
git branch -M main

# Step 6: Add GitHub remote
git remote add origin https://github.com/nada22-creator/Mini-projects.git

# Step 7: Push to GitHub
git push -u origin main
