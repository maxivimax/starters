import os
import json
from supabase import create_client, Client
from config import SUPABASE_KEY, SUPABASE_URL

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def getData():
    response = supabase.table("data").select("*").execute().data
    return response
