# Olivia's Bachelorette Extravaganza Setup Guide

## Files Created:
1. `olivias-bachelorette.html` - The web page with big yellow letters and lavender button
2. `generate_qr.py` - Python script to generate the QR code
3. `olivias_bachelorette_qr.png` - The QR code image (currently points to placeholder URL)

## Setup Steps:

### 1. Update the Venmo Link
Edit `olivias-bachelorette.html` and replace `YOUR-VENMO-USERNAME` with the actual Venmo username:
```html
<a href="https://venmo.com/u/actual-venmo-username" class="buy-drink-btn" target="_blank">
```

### 2. Host the HTML File
You have several free options:

#### Option A: GitHub Pages (Recommended)
1. Create a GitHub repository
2. Upload `olivias-bachelorette.html`
3. Go to Settings → Pages
4. Enable GitHub Pages
5. Your URL will be: `https://username.github.io/repository-name/olivias-bachelorette.html`

#### Option B: Netlify
1. Go to [netlify.com](https://netlify.com)
2. Drag and drop the HTML file
3. Get your URL (something like: `https://random-name.netlify.app/olivias-bachelorette.html`)

#### Option C: Vercel
1. Go to [vercel.com](https://vercel.com)
2. Upload your HTML file
3. Deploy and get your URL

### 3. Update QR Code with Real URL
1. Edit `generate_qr.py` 
2. Replace `https://your-hosting-service.com/olivias-bachelorette.html` with your actual hosted URL
3. Run: `python3 generate_qr.py`

### 4. Print the QR Code
The QR code is saved as `olivias_bachelorette_qr.png` - you can print this and put it on tables, cards, etc.

## Features:
- ✨ Big yellow "Welcome to Olivia's Bachelorette Extravaganza" text
- 💜 Lavender "Buy the Bride a Drink!" button
- 🎉 Sparkle animations for fun
- 📱 Mobile-responsive design
- 🔗 Direct link to Venmo for easy payments

## Quick Test:
You can open `olivias-bachelorette.html` directly in your browser to see how it looks before hosting it online.
