import os
from dotenv import load_dotenv

# Set enviromental variables
load_dotenv()

# Check the environment type, i.e. stage (DEV/TEST/PROD)
env = os.getenv("STAGE")

# Define DB path and credentials from enviromental variables depending on the stage
match env:
    case "DEV":
        db_config = {
            "type": "sqlite",
            "username": None,
            "pass": None,
            "host": None,
            "db": "project-tc.db",
        }
    case "TEST":
        db_config = {
            "type": "mysql+mysqldb",
            "username": os.getenv("USERNAME"),
            "pass": os.getenv("PASS"),
            "host": os.getenv("HOST"),
            "db": "project-tc",
        }
    case "PROD":
        db_config = {
            "type": "mysql+mysqldb",
            "username": os.getenv("USERNAME"),
            "pass": os.getenv("PASS"),
            "host": os.getenv("HOST"),
            "db": "project-tc",
        }
    # If no ENV variable has been detected, exit with an error message
    case _:
        print ("Error: .env file is missing or ENV not set")
        exit(1)

