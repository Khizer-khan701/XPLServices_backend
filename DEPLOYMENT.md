# Railway Deployment Guide

## Prerequisites
- Railway account (railway.app)
- GitHub repository with this code
- Git installed on your machine

## Deployment Steps

### 1. Push Code to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 2. Connect to Railway
1. Go to [railway.app](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Authorize Railway to access your GitHub
5. Select your repository
6. Click "Deploy"

### 3. Configure Environment Variables
In Railway Dashboard:
1. Go to your project
2. Click the service
3. Go to "Variables" tab
4. Add all variables from your `.env` file:
   - `OPENAI_API_KEY`
   - `GEMINI_API_KEY`
   - `OPENROUTER_API_KEY`
   - `ELEVENLABS_API_KEY`
   - `DATABASE_URL`

### 4. Verify Deployment
- Check the "Deployments" tab
- View logs to ensure no errors
- Click the generated URL to test your API
- Test endpoints: `https://your-railway-url/` and `https://your-railway-url/docs`

## Important Notes
⚠️ **Security**: Never commit `.env` file to GitHub. The `.gitignore` file is configured to exclude it.

## Support
- Railway Docs: https://docs.railway.app
- FastAPI: https://fastapi.tiangolo.com
- Uvicorn: https://www.uvicorn.org
