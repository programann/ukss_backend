import cloudinary.uploader

def upload_to_cloudinary(file):
    result = cloudinary.uploader.upload(file, folder="school_events")
    return result["secure_url"]
