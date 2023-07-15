import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("TOKEN")
ADMIN_API_TOKEN = os.getenv("ADMIN_TOKEN")

admin_id = os.getenv("ADMIN_ID")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")