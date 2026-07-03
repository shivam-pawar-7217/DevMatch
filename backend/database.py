import os
import time
import psycopg2
from psycopg2.extras import RealDictCursor

def get_db():
    """ Connect to postgres using env vars from docker """
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        port=os.environ.get("DB_PORT", "5432"),
        database=os.environ.get("DB_NAME", "devmatch_db"),
        user=os.environ.get("DB_USER", "devmatch_user"),
        password=os.environ.get("DB_PASSWORD", "devmatch_pass")
    )

def wait_for_db():
    """ Docker sometimes starts backend before postgres is fully up. We retry a few times. """
    print("Connecting to database...")
    for i in range(10):
        try:
            conn = get_db()
            conn.close()
            print("DB connected!")
            return
        except Exception as e:
            print(f"DB not ready yet... waiting 2 secs. Attempt {i+1}/10")
            time.sleep(2)
    
    # if we get here, things are broken
    raise Exception("Could not connect to DB. Is the docker container running?")
