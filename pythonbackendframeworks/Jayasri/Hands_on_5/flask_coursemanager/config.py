class Config:
    SECRET_KEY = "mysecretkey"

    SQLALCHEMY_DATABASE_URI = "sqlite:///course.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True