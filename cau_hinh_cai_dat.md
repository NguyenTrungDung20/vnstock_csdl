(.venv) PS E:\MGI_Investment\vnstock_csdl> python -m pip list
Package            Version
------------------ ------------
annotated-types    0.8.0
beautifulsoup4     4.15.0
certifi            2026.7.22
cffi               2.1.1
charset-normalizer 3.5.1
contourpy          1.4.0
cycler             0.12.1
et_xmlfile         2.0.0
fonttools          4.65.0
idna               3.19
importlib_metadata 9.0.1
kiwisolver         1.5.1
matplotlib         3.11.2
mplfinance         0.12.10b0
numpy              2.2.6
openpyxl           3.1.5
packaging          26.3
pandas             2.3.3
pillow             12.3.0
pip                26.2.1
psutil             7.2.2
pycparser          3.0
pydantic           2.13.5
pydantic_core      2.46.5
pyparsing          3.3.2
python-dateutil    2.9.0.post0
pytz               2026.3.post1
requests           2.34.2
seaborn            0.13.2
setuptools         84.0.0
six                1.17.0
soupsieve          2.9.2
tenacity           9.1.4
typing_extensions  4.16.0
typing-inspection  0.4.4
tzdata             2026.4
urllib3            2.8.0
vnai               2.6.0
vnstock            4.0.8
vnstock_ezchart    1.0.2
wheel              0.48.0
zipp               4.1.0






vnstock_csdl/
│
├── .venv/                         # Virtual environment Python 3.12
│
├── .env                           # Thông tin kết nối DB, token... KHÔNG commit
├── .env.example                   # Mẫu biến môi trường
├── .gitignore
├── README.md
├── requirements.txt
│
├── data/
│   │
│   ├── raw/                       # Dữ liệu gốc - KHÔNG chỉnh sửa
│   │   ├── master/
│   │   │   └── danh_sach_co_phieu_goc.xlsx
│   │   │
│   │   └── vnstock/               # Payload/file lấy trực tiếp từ Vnstock nếu cần
│   │
│   ├── staging/                   # Dữ liệu trung gian đang chuẩn hóa
│   │
│   ├── processed/                 # Dữ liệu đã clean/validate
│   │
│   └── exports/                   # File xuất ra Excel/CSV phục vụ sử dụng
│
├── config/
│   ├── settings.py                # Cấu hình chung
│   └── mappings.py                # Mapping HOSE/HSX, ngành nghề, tên cột...
│
├── src/
│   └── vnstock_csdl/
│       │
│       ├── __init__.py
│       │
│       ├── connectors/
│       │   └── vnstock/
│       │       ├── __init__.py
│       │       ├── company.py
│       │       ├── market.py
│       │       └── financial.py
│       │
│       ├── ingestion/
│       │   ├── master_list.py
│       │   ├── market_data.py
│       │   ├── company_data.py
│       │   └── financial_data.py
│       │
│       ├── cleaning/
│       │   ├── securities.py
│       │   ├── market_data.py
│       │   └── financial_data.py
│       │
│       ├── validation/
│       │   ├── securities.py
│       │   ├── market_data.py
│       │   └── financial_data.py
│       │
│       ├── database/
│       │   ├── connection.py
│       │   ├── insert.py
│       │   └── upsert.py
│       │
│       ├── metrics/
│       │   ├── liquidity.py
│       │   ├── market.py
│       │   └── financial.py
│       │
│       └── utils/
│           ├── dates.py
│           ├── logging.py
│           └── text.py
│
├── sql/
│   ├── migrations/
│   │   ├── 001_create_schemas.sql
│   │   ├── 002_create_reference_tables.sql
│   │   ├── 003_create_market_tables.sql
│   │   └── 004_create_financial_tables.sql
│   │
│   └── queries/
│       ├── securities.sql
│       ├── market_metrics.sql
│       └── financial_metrics.sql
│
├── scripts/
│   ├── 01_clean_master_list.py
│   ├── 02_test_vnstock.py
│   ├── 03_init_database.py
│   ├── 04_load_master_data.py
│   ├── 05_update_market_data.py
│   └── 06_update_financial_data.py
│
├── tests/
│   ├── test_cleaning.py
│   ├── test_validation.py
│   └── test_vnstock_connector.py
│
├── logs/                           # Log ingestion/update/error
│
└── docs/
    └── notes/
        └── cau_hinh_cai_dat.md     # File nháp hiện tại của bạn