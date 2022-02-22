import os
from pathlib import Path
from dotenv import load_dotenv

ENV = os.path.join(Path(__file__).resolve().parent.parent, 'config', '.env')
load_dotenv(ENV)
print(os.getenv('DATABASE_HOST'))
