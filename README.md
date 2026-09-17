# VNSTOCK_CSDL

Hướng dẫn cài đặt môi trường để chạy `config.py` và `connector.ipynb`.

## 1. Yêu cầu

- Windows 10/11
- Python **3.12.x** (khuyến nghị Python 3.12.10)
- Visual Studio Code
- Extension VS Code:
  - Python
  - Jupyter
- Google Chrome nếu sử dụng Selenium để truy cập website

Cấu trúc thư mục nên có dạng:

```text
vnstock_csdl/
├── config.py
├── connector.ipynb
├── README.md
└── .venv/
```

## 2. Tạo virtual environment

Mở PowerShell/Terminal tại thư mục project:

```powershell
cd E:\MGI_Investment\vnstock_csdl
```

Tạo môi trường bằng Python 3.12:

```powershell
py -3.12 -m venv .venv
```

Kích hoạt môi trường:

```powershell
.\.venv\Scripts\Activate.ps1
```

Kiểm tra:

```powershell
python --version
```

Kết quả nên là:

```text
Python 3.12.x
```

## 3. Cài các thư viện

Sau khi đã kích hoạt `.venv`:

```powershell
python -m pip install --upgrade pip
```

Cài các package cần thiết:

```powershell
pip install vnstock pandas openpyxl selenium ipykernel
```

Nếu notebook sử dụng thêm package khác, cài package bị thiếu bằng:

```powershell
pip install <ten-package>
```

## 4. Chọn Python Kernel trong VS Code

Mở `connector.ipynb`.

Ở góc trên bên phải của notebook, chọn:

```text
Select Kernel
→ Python Environments
→ .venv
```

Kernel cần trỏ tới:

```text
E:\MGI_Investment\vnstock_csdl\.venv\Scripts\python.exe
```

Có thể kiểm tra trong notebook bằng:

```python
import sys
print(sys.executable)
```

## 5. Cấu hình `config.py`

Đặt `config.py` cùng thư mục với `connector.ipynb`.

Nếu file chứa API key, token hoặc thông tin riêng, không nên đưa các giá trị này lên GitHub public.

Trong notebook có thể import cấu hình bằng:

```python
import config
```

hoặc:

```python
from config import *
```

tùy theo cách các biến được khai báo trong `config.py`.

## 6. Chạy notebook

Sau khi chọn đúng kernel `.venv`, mở:

```text
connector.ipynb
```

và chạy lần lượt các cell từ trên xuống dưới.

Để kiểm tra nhanh môi trường:

```python
import pandas as pd
import vnstock
import selenium

print("Môi trường hoạt động bình thường.")
```

## 7. Một số lỗi thường gặp

### `ModuleNotFoundError`

Ví dụ:

```text
ModuleNotFoundError: No module named 'vnstock'
```

Kiểm tra notebook có đang dùng đúng `.venv` hay không, sau đó chạy:

```powershell
pip install vnstock
```

### Không xuất được Excel

Cài `openpyxl`:

```powershell
pip install openpyxl
```

### Selenium không chạy

Cập nhật Selenium:

```powershell
pip install --upgrade selenium
```

Đồng thời kiểm tra Google Chrome đã được cài đặt và cập nhật.

### Notebook dùng nhầm Python

Chạy:

```python
import sys
print(sys.executable)
```

Đường dẫn đúng nên chứa:

```text
vnstock_csdl\.venv\Scripts\python.exe
```

## 8. Khởi động lại project

Mỗi lần mở Terminal mới:

```powershell
cd E:\MGI_Investment\vnstock_csdl
.\.venv\Scripts\Activate.ps1
```

Sau đó mở `connector.ipynb` và chọn kernel `.venv`.

---

**Lưu ý:** Vnstock Community có giới hạn request API. Khi xử lý nhiều mã chứng khoán, nên có cơ chế delay, retry và checkpoint trong notebook để tránh mất tiến độ khi gặp rate limit.
