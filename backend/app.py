import sys
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from cairo import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)