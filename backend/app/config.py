from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:1234@localhost/demo')

# # config.py
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()

# # Retrieve the database URL from the environment variables
# DATABASE_URL = os.getenv('DATABASE_URL')
