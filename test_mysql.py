import os

from dotenv import load_dotenv
from sqlalchemy import URL, create_engine, text


# ============================================================
# 1. Load biến môi trường từ file .env
# ============================================================

load_dotenv()


# ============================================================
# 2. Tạo URL kết nối MySQL
# ============================================================

url = URL.create(
    drivername="mysql+pymysql",
    username=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
    database=os.getenv("MYSQL_DATABASE"),
    query={"charset": "utf8mb4"},
)


# ============================================================
# 3. Tạo SQLAlchemy Engine
# ============================================================

engine = create_engine(
    url,
    pool_pre_ping=True
)


# ============================================================
# 4. Kiểm tra kết nối
# ============================================================

try:
    with engine.connect() as conn:

        result = conn.execute(
            text("""
                SELECT
                    DATABASE() AS database_name,
                    @@version AS mysql_version,
                    @@character_set_connection AS charset,
                    @@collation_connection AS collation
            """)
        )

        row = result.fetchone()

        print("=" * 50)
        print("MYSQL CONNECTION TEST")
        print("=" * 50)

        print("Database      :", row.database_name)
        print("MySQL Version :", row.mysql_version)
        print("Charset       :", row.charset)
        print("Collation     :", row.collation)

        print("=" * 50)
        print("KẾT NỐI MYSQL THÀNH CÔNG!")

except Exception as e:

    print("=" * 50)
    print("KẾT NỐI MYSQL THẤT BẠI!")
    print("=" * 50)
    print(type(e).__name__)
    print(e)
    