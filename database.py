from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Local testing ke liye SQLite use kar rahe hain
SQLALCHEMY_DATABASE_URL = "sqlite:///./taskmanager.db"

# Engine create karna (connect_args sirf SQLite ke liye zaroori hai)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal database se temporary connection banayega
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Is Base class se hum apne saare database tables banayenge
Base = declarative_base()

# Database session get karne ka function (Dependency)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()