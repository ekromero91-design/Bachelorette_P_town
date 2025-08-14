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
- 🍸 Multiple drink price options ($5 Shot, $10 Cocktail, $15 Wine, $25 Champagne)
- 🎉 Interactive animations and sound effects
- 💕 Cross-device message board for guests to leave messages for Olivia
- 🔄 Real-time message syncing across all devices (5-second polling)
- 🛡️ Built-in profanity filter to keep messages appropriate
- 🔧 Admin mode for message moderation (password: olivia2024)
- 📱 Mobile-responsive design
- 🔗 Direct Venmo integration for easy payments

## Message Board Features:

### For Guests:
- Leave sweet messages for Olivia using the "Messages for Olivia" section
- Messages are limited to 150 characters and names to 20 characters
- All inappropriate content is automatically filtered
- Messages sync across all devices within 5 seconds

### For Admins:
- Click the small 🔧 icon in the top-right of the message board
- Enter password: `olivia2024`
- Delete inappropriate messages by clicking the × button
- Click 🚪 to logout of admin mode

### Technical Details:
- Messages are stored in browser localStorage with cross-device sync
- No external database required - works entirely client-side
- Automatic profanity filtering blocks inappropriate content
- Polling every 5 seconds keeps all devices synchronized

## Quick Test:
You can open `olivias-bachelorette.html` directly in your browser to see how it looks before hosting it online.
