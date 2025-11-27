# ChatGPT Desktop App

A lightweight, efficient desktop application for accessing ChatGPT. Built with Python and pywebview for a minimal, fast experience.

## Features

- 🚀 Lightweight and efficient (no Chromium overhead)
- 🎨 Clean, modern interface
- 🔒 Secure connection to ChatGPT
- 💻 Native desktop application
- ⚡ Fast startup and performance

## Requirements

- Python 3.8 or higher
- Windows 10/11 (or Linux/macOS)

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python main.py
```

The app will open a window connecting directly to ChatGPT. Simply log in and start chatting!

## Technical Details

This application uses `pywebview`, which utilizes your system's native webview component:
- **Windows**: Uses Edge WebView2 (if available) or falls back to IE
- **macOS**: Uses WKWebView (WebKit-based, not Chromium)
- **Linux**: Uses WebKitGTK (WebKit-based, not Chromium)

**Note on Windows**: Modern Windows systems use Edge WebView2, which is Chromium-based. However, this is the system's native webview and provides the best performance and compatibility. For a truly non-Chromium experience, consider using this app on macOS or Linux, which use WebKit-based webviews.

## License

MIT License - feel free to use and modify as needed.

