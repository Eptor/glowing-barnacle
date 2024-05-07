from supabase import create_client, Client

url: str = "https://xdsstcqwucixgufosfqj.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inhkc3N0Y3F3dWNpeGd1Zm9zZnFqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTI1MzgyNTksImV4cCI6MjAyODExNDI1OX0.SO_XPWALngeNQaAxjiZSwSH4_M9xuXpju6WeGMtVKWM"
supabase_client = create_client(url, key)