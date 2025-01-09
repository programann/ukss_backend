import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "8321ce6cc7de4184bf491894345e73b0")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///school.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CLOUDINARY_URL = os.getenv("CLOUDINARY_URL", "cloudinary://API_KEY:API_SECRET@CLOUD_NAME")
    
    # JWT Configuration
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "8321ce6cc7de4184bf491894345e73b0")
    JWT_ACCESS_TOKEN_EXPIRES = False 