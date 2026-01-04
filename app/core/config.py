import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CLERK_SECRET_KEY=os.getenv("CLERK_SECRET_KEY")
    CLERK_PUBLISHABLE_KEY=os.getenv("CLERK_PUBLISHABLE_KEY")
    CLERK_WEBHOOK_SECRET=os.getenv("CLERK_WEBHOOK_SECRET")
    CLERK_JWKS_URL=os.getenv("CLERK_JWKS_URL")

    DATABASE_URL=os.getenv("DATABASE_URL")
    FRONTEND_URL=os.getenv("FRONTEND_URL")

    FREE_TIER_MEMBERSHIP_LIMIT : int =2
    pro_TIER_MEMBERSHIP_LIMIT : int =0

settings = Config()
