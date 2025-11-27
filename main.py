"""
ChatGPT Desktop App
A lightweight, efficient desktop application for accessing ChatGPT.
"""

import sys
from pathlib import Path

# Create user data directory for persistent storage
user_data_dir = Path.home() / '.chatgpt-desktop'
user_data_dir.mkdir(exist_ok=True)

import webview


class ChatGPTApp:
    def __init__(self):
        self.window = None
        self.chatgpt_url = "https://chat.openai.com"
        self.storage_path = str(user_data_dir)
        
    def create_window(self):
        """Create the main application window"""
        # Window configuration with modern defaults
        window_config = {
            'title': 'ChatGPT',
            'url': self.chatgpt_url,
            'width': 1200,
            'height': 800,
            'min_size': (800, 600),
            'resizable': True,
            'fullscreen': False,
            'on_top': False,
            'background_color': '#FFFFFF',
            'frameless': False,
            'shadow': True,
        }
        
        # Create the webview window
        self.window = webview.create_window(**window_config)
        
        # Inject custom CSS after page loads
        def on_loaded():
            try:
                css = """
                    html, body {
                        margin: 0;
                        padding: 0;
                        height: 100%;
                        overflow: hidden;
                    }
                    * {
                        scroll-behavior: smooth;
                    }
                """
                css_escaped = css.replace('\\', '\\\\').replace('`', '\\`').replace('$', '\\$')
                js_code = f"""
                    (function() {{
                        var style = document.createElement('style');
                        style.textContent = `{css_escaped}`;
                        document.head.appendChild(style);
                    }})();
                """
                self.window.evaluate_js(js_code)
            except Exception:
                pass
        
        # Set up event handlers
        if hasattr(self.window, 'loaded'):
            self.window.loaded += on_loaded
        
    def run(self):
        """Start the application"""
        try:
            self.create_window()
            # Start webview with persistent storage
            # private_mode=False allows cookies/localStorage to persist
            # storage_path sets where the data is stored
            webview.start(
                debug=False,
                private_mode=False,
                storage_path=self.storage_path
            )
        except KeyboardInterrupt:
            print("\nApplication closed by user.")
            sys.exit(0)
        except Exception as e:
            print(f"Error starting application: {e}")
            sys.exit(1)


def main():
    """Main entry point"""
    try:
        app = ChatGPTApp()
        app.run()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

