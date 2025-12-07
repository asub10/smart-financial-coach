# GitHub Repository Setup Guide

## Option 1: Command Line (Recommended)

### Step 1: Create GitHub Repository
1. Go to github.com and log in
2. Click the "+" in top right → "New repository"
3. Name: `smart-financial-coach` or `panw-case-study`
4. Make it **Public** (unless they specify private)
5. DO NOT initialize with README (you already have one)
6. Click "Create repository"

### Step 2: Initialize Git Locally
```bash
# Navigate to your project folder
cd /path/to/your/project

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Smart Financial Coach - PANW Case Study"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/smart-financial-coach.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Verify
- Go to your GitHub repository URL
- Verify all files are visible
- Click on each file to make sure they display correctly
- Test the link in incognito mode to ensure it's public

---

## Option 2: GitHub Desktop (Easy)

### Step 1: Install GitHub Desktop
- Download from: https://desktop.github.com/

### Step 2: Create Repository
1. Open GitHub Desktop
2. File → New Repository
3. Name: `smart-financial-coach`
4. Local Path: Choose your project folder
5. Click "Create Repository"

### Step 3: Add Files
1. Copy all your files into the repository folder
2. GitHub Desktop will show all new files
3. Write commit message: "Initial commit: Smart Financial Coach"
4. Click "Commit to main"

### Step 4: Publish
1. Click "Publish repository" 
2. Uncheck "Keep this code private" (unless specified)
3. Click "Publish repository"

---

## Option 3: Upload via GitHub Web Interface (Backup)

### Step 1: Create Empty Repository
1. Go to github.com → New repository
2. Name: `smart-financial-coach`
3. Make it Public
4. DO initialize with README (we'll replace it)
5. Click "Create repository"

### Step 2: Upload Files
1. Click "Add file" → "Upload files"
2. Drag all your files into the browser:
   - app.py
   - transactions.csv
   - requirements.txt
   - README.md
   - DESIGN_DOCUMENTATION.md
   - PRESENTATION_SCRIPT.md
   - SUBMISSION_CHECKLIST.md
   - QUICK_START.md
3. Commit message: "Initial commit: Smart Financial Coach"
4. Click "Commit changes"

---

## What Your Repository Should Look Like

```
smart-financial-coach/
│
├── 📄 README.md                    ← Project overview (shows on homepage)
├── 📄 app.py                       ← Main application
├── 📄 transactions.csv             ← Demo data
├── 📄 requirements.txt             ← Dependencies
├── 📄 DESIGN_DOCUMENTATION.md      ← Technical documentation
├── 📄 PRESENTATION_SCRIPT.md       ← Video script
├── 📄 SUBMISSION_CHECKLIST.md      ← Submission guide
└── 📄 QUICK_START.md               ← Quick start guide
```

---

## Important: .gitignore

Create a `.gitignore` file to exclude unnecessary files:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/

# Streamlit
.streamlit/

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo
```

To add this:
```bash
# Create .gitignore file
cat > .gitignore << 'EOF'
__pycache__/
*.py[cod]
.streamlit/
.DS_Store
.vscode/
venv/
EOF

# Add to git
git add .gitignore
git commit -m "Add .gitignore"
git push
```

---

## Repository Settings to Check

### 1. Make Sure It's Public
- Go to repository Settings → Danger Zone
- Check visibility is "Public"

### 2. Enable Issues (Optional)
- Settings → Features → Check "Issues"
- Shows you're professional about tracking work

### 3. Add Topics (Optional but Nice)
- Click the ⚙️ next to "About"
- Add topics: `ai`, `fintech`, `python`, `streamlit`, `case-study`
- Makes your repo more discoverable

---

## Testing Your Repository

### Before Submitting
1. **Open in Incognito Mode**: Make sure anyone can view it
2. **Check All Files Load**: Click through each file
3. **Verify README Renders**: Should look nice with proper formatting
4. **Test Clone Command**: 
   ```bash
   git clone https://github.com/YOUR_USERNAME/smart-financial-coach.git test-clone
   cd test-clone
   streamlit run app.py
   ```
5. **Screenshot for Submission**: Take a screenshot of your repo homepage

---

## Common Issues & Fixes

### Issue: "Permission denied (publickey)"
**Fix**: Use HTTPS instead of SSH
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/smart-financial-coach.git
```

### Issue: "Repository not found"
**Fix**: Check the URL is correct, ensure repository is public

### Issue: Files not showing up
**Fix**: 
```bash
git status  # Check what's being tracked
git add .   # Add all files
git commit -m "Add missing files"
git push
```

### Issue: Large files rejected
**Fix**: Our files are tiny, but if you added screenshots:
- Keep images under 5MB
- Use PNG or JPG format
- Compress if needed

---

## Best Practices

### Commit Messages
Good:
- ✅ "Initial commit: Smart Financial Coach"
- ✅ "Update README with demo instructions"
- ✅ "Fix subscription detection algorithm"

Bad:
- ❌ "fix"
- ❌ "asdf"
- ❌ "updates"

### Repository Description
Add a short description at the top:
> "AI-powered subscription detector that helps users save money on forgotten recurring charges. Built for Palo Alto Networks Product SWE Case Study."

### README First Impression
Make sure your README.md:
- Has a clear title
- Explains what the project does
- Shows how to run it
- Looks professional

---

## Final Checklist Before Submission

- [ ] Repository is public
- [ ] All 8 files are present
- [ ] README renders correctly
- [ ] No sensitive data (API keys, passwords)
- [ ] Repository has a description
- [ ] Works when cloned to a new location
- [ ] Tested in incognito mode

---

## Your Repository URL Format

```
https://github.com/YOUR_USERNAME/smart-financial-coach
```

**This is what you'll submit in the Google Form!**

---

## After Pushing to GitHub

### Add a Nice README Badge (Optional)
Add this to the top of your README.md:
```markdown
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.29.0-FF4B4B.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
```

### Pin the Repository (Optional)
1. Go to your GitHub profile
2. Click "Customize your pins"
3. Select this repository
4. Makes it prominent on your profile

---

## Need Help?

### Git Resources
- GitHub Guides: https://guides.github.com/
- Git Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf

### If Really Stuck
Use the web interface method (Option 3) - it's foolproof!

---

## Remember

⏰ **Push by December 7th, 2:00 PM PST** (3 hours before deadline)

📝 **Double-check the URL** before submitting

🔒 **DO NOT edit after 5:00 PM PST** or you'll be disqualified

Good luck! 🚀
