# 🚀 Heroku Deployment Guide

This guide covers deploying your Text Summarization NLP application to Heroku.

## 🟣 Heroku Deployment

### Prerequisites:
- Heroku account (free tier available at [heroku.com](https://heroku.com))
- Heroku CLI installed on your computer

### Step 1: Install Heroku CLI
1. **Download Heroku CLI**: Go to [devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)
2. **Install for your OS**: Follow the installation instructions for Windows/Mac/Linux
3. **Verify installation**: Open terminal and run `heroku --version`

### Step 2: Login to Heroku
```bash
heroku login
```
This will open your browser to login to Heroku.

### Step 3: Create Heroku App
```bash
cd "c:\Users\aksha\Projects\Text-Summarization-NLP-main"
heroku create your-app-name-here
```
Replace `your-app-name-here` with a unique name for your app.

### Step 4: Deploy to Heroku
```bash
git add .
git commit -m "Add Heroku deployment configuration"
git push heroku main
```

### Step 5: Open Your Live App
```bash
heroku open
```
This will open your deployed app in the browser!

---

## 🛠️ Configuration Files Explained:

### `Procfile`
Tells Heroku how to start your application:
- `web: gunicorn wsgi:app` - Uses Gunicorn to serve your Flask app

### `runtime.txt`
Specifies the Python version:
- `python-3.12.4` - Ensures Heroku uses the same Python version

### `wsgi.py`
Production entry point that:
- Downloads required NLTK data on startup
- Imports your Flask app for production serving

### `requirements.txt`
Lists all Python dependencies including:
- Flask and NLP libraries
- Gunicorn for production serving

---

## 🎯 Why Heroku?

- **Beginner-Friendly**: Most documented platform for beginners
- **Free Tier**: Good for learning and small projects
- **Git-Based**: Deploy with simple `git push`
- **Add-ons**: Easy to add databases, monitoring, etc.
- **Popular**: Large community and lots of tutorials

---

## 🚨 Important Notes:

### Heroku Free Tier Limitations:
- **Dyno Sleep**: App sleeps after 30 minutes of inactivity
- **Hours Limit**: 550 free hours per month (1000 with credit card)
- **Cold Start**: First request after sleep takes longer

### After Deployment:
1. **Test all features**: Text summarization, sentiment analysis, word cloud
2. **Check logs**: Use `heroku logs --tail` to monitor your app
3. **Scale if needed**: `heroku ps:scale web=1` to ensure one dyno is running
4. **Add domain**: Optionally add your custom domain

---

## 🛠️ Useful Heroku Commands:

```bash
# View app logs
heroku logs --tail

# Check app status
heroku ps

# Open app in browser
heroku open

# Run commands on Heroku
heroku run python

# Restart app
heroku restart
```

---

## 🎉 Success!

Your Text Summarization NLP app will be live at:
`https://your-app-name.herokuapp.com`

The app will automatically:
- ✅ Install all dependencies
- ✅ Download NLTK data
- ✅ Start with Gunicorn
- ✅ Handle web traffic

Your app is now accessible worldwide! 🌍✨