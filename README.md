# VNSTOCK_CSDL

Dự án thu thập dữ liệu cổ phiếu Việt Nam từ nguồn VCI qua thư viện `vnstock`, tính các chỉ tiêu theo dõi thị trường và xuất Excel. Luồng xử lý chính nằm trong `xuat_excel/connector.ipynb`, chạy thủ công bằng Jupyter trong VS Code.

**Dự án đang phát triển. Kết nối MySQL chỉ đang thử nghiệm; cơ sở dữ liệu chưa hoàn tất.** Hiện chưa có schema, migration hoặc luồng ghi dữ liệu từ notebook vào MySQL. Kết quả hiện được lưu bằng Excel và checkpoint trên máy.

## 1. Chức năng hiện có

- Lấy danh sách mã cổ phiếu, thông tin sàn và ngành ICB.
- Lấy bảng giá theo nhóm mã để tính vốn hóa.
- Tính khối lượng giao dịch trung bình 20 phiên.
- Tính giá trị giao dịch ước tính trung bình 20 và 60 phiên.
- Lưu checkpoint theo ngày dữ liệu, xử lý rate limit và thử lại các mã lỗi.
- Xuất Excel kết quả và danh sách mã cần kiểm tra.
- Thử nghiệm kiểm tra kết nối MySQL bằng `test_mysql.py`.

Danh sách mã được lấy trực tiếp từ VCI mỗi lượt chạy, không cố định số lượng. Output lưu trong notebook là kết quả các lần chạy trước, không đại diện cho dữ liệu hiện tại.

## 2. Cấu trúc dự án

| Đường dẫn | Vai trò |
| --- | --- |
| `xuat_excel/connector.ipynb` | Thu thập dữ liệu, tính chỉ tiêu và xuất Excel |
| `config.py` | Đăng ký người dùng Vnstock và import thư viện |
| `test_mysql.py` | Thử nghiệm kết nối MySQL |
| `csdl_mau/Bản test trước khi chuẩn hóa dữ liệu.xlsx` | Dữ liệu mẫu có sheet DSCP và Nháp để đối chiếu, chuẩn hóa |
| `csdl_mau/Processed.xlsx` | File giữ chỗ, chưa có bảng dữ liệu hoàn chỉnh |
| `database/` | Thư mục dự kiến, chưa có triển khai database |
| `cau_hinh_cai_dat.md` | Ghi chú môi trường và cấu trúc dự kiến |
| `AGENTS.md`, `xuat_excel/AGENTS.md` | Hướng dẫn cho AI agent |
| `.env` | Cấu hình riêng trên máy |
| `.venv/` | Môi trường Python cục bộ |

Các file cấu hình cục bộ và thư mục trống có thể không xuất hiện trong bản clone. Cấu trúc đề xuất trong `cau_hinh_cai_dat.md` chưa được triển khai đầy đủ.

## 3. Cài đặt môi trường

Môi trường đang sử dụng: Windows, Python 3.12.10, VS Code với extension Python và Jupyter. Chạy các lệnh dưới đây bằng PowerShell tại thư mục gốc dự án.

Nếu chưa có `.venv`:

```powershell
py -3.12 -m venv .venv
```

Kích hoạt môi trường và cài thư viện cho notebook:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install vnstock pandas openpyxl ipykernel tzdata
```

`tzdata` cung cấp dữ liệu múi giờ cho `ZoneInfo("Asia/Ho_Chi_Minh")` trên Windows. Các phiên bản đã ghi nhận trong môi trường làm việc: `vnstock 4.0.8`, `pandas 2.3.3`, `openpyxl 3.1.5`. Dự án chưa có file khóa phiên bản thư viện.

Cài thêm khi thử nghiệm MySQL:

```powershell
python -m pip install SQLAlchemy PyMySQL python-dotenv
```

Mở `xuat_excel/connector.ipynb`, chọn **Select Kernel > Python Environments > .venv**. Kiểm tra Python và thư mục làm việc trong một cell riêng:

```python
import sys
from pathlib import Path

print(sys.executable)
print(Path.cwd())
```

Notebook dùng đường dẫn tương đối. Excel và checkpoint được lưu tại thư mục làm việc của kernel, có thể khác thư mục chứa notebook. Giữ cùng thư mục làm việc giữa các lần chạy để tìm đúng checkpoint.

## 4. Cấu hình Vnstock

`config.py` hiện gọi `register_user` và import các lớp Vnstock; file này không cấu hình MySQL. Notebook hiện không tự import `config.py`.

API key và mật khẩu là thông tin riêng, không đưa giá trị thật vào README, output notebook hoặc commit. Khi chuyển cấu hình Vnstock sang biến môi trường, có thể dùng `VNSTOCK_API_KEY` trong `.env`; code hiện tại chưa tự đọc biến này.

## 5. Chạy và cập nhật dữ liệu

Lần chạy đầy đủ, chạy các cell từ trên xuống dưới. Tải toàn thị trường có thể mất nhiều thời gian; kiểm tra thông báo và sheet lỗi sau khi hoàn tất.

| Cell theo thứ tự | Nội dung | File kết quả |
| --- | --- | --- |
| 1–2 | Khởi tạo Listing và lấy danh sách mã | `all_symbols.xlsx` |
| 3 | Thông tin mã theo sàn | `by_exchange.xlsx` |
| 4 | Thông tin ngành ICB | `by_industry.xlsx` |
| 5–9 | Lấy bảng giá, tính và xuất vốn hóa | `market_cap_vci.xlsx` |
| 10 | Khối lượng giao dịch trung bình 20 phiên | `KLDG_20_VCI.xlsx` |
| 11 | Giá trị giao dịch ước tính trung bình 20 phiên | `GTGD_20_VCI.xlsx` |
| 12 | Giá trị giao dịch ước tính trung bình 60 phiên | `GTGD_60_VCI.xlsx` |

Tên `KLDG` trong code và file hiện tại dùng cho chỉ tiêu KLGD. Có thể chạy riêng cell 10, 11 hoặc 12 để cập nhật chỉ tiêu lịch sử vì mỗi cell tự import thư viện và lấy danh sách mã.

### Ngày kết thúc dữ liệu

Ba cell lịch sử xác định `end_date` theo múi giờ Việt Nam:

- Trước 15:15: lấy đến ngày hôm qua.
- Từ 15:15: cho phép lấy đến hôm nay.
- Cuối tuần hoặc ngày nghỉ: kết quả phụ thuộc các phiên có dữ liệu mà VCI trả về.

Mốc này là ngày yêu cầu dữ liệu, không xác nhận nguồn đã cập nhật xong phiên. Kiểm tra `Den_ngay` của từng mã để biết phiên cuối thực tế. Mỗi cell xác định ngày riêng khi bắt đầu; lưu ý khi chạy qua mốc 15:15 hoặc qua ngày mới.

### Checkpoint theo ngày

Checkpoint được tách theo chỉ tiêu và ngày kết thúc dữ liệu, ví dụ:

```text
KLDG_20_VCI_checkpoint_2026-09-17.xlsx
GTGD_20_VCI_checkpoint_2026-09-17.xlsx
GTGD_60_VCI_checkpoint_2026-09-17.csv
```

Giữ `FORCE_REFRESH = False` trong cell để dùng chế độ mặc định:

- Cùng ngày dữ liệu: tiếp tục checkpoint, bỏ qua mã đã xử lý xong và thử lại mã lỗi.
- Ngày dữ liệu mới: dùng checkpoint mới và tính lại toàn bộ mã.
- Checkpoint cũ không có ngày trong tên không được dùng bởi luồng mới.

Muốn lấy lại toàn bộ dữ liệu trong cùng ngày, sửa cấu hình ngay trong cell cần cập nhật rồi chạy cell đó:

```python
FORCE_REFRESH = True
```

Sau khi hoàn tất, đổi lại `False` để có thể tiếp tục checkpoint ở lượt sau. Nếu giữ `True`, mỗi lần chạy lại cell đều bắt đầu từ đầu.

Các trạng thái `OK`, `THIEU_20_PHIEN` hoặc `THIEU_60_PHIEN`, và `KHONG_CO_DU_LIEU` được xem là đã xử lý trong cùng ngày. Muốn truy vấn lại các mã này cần bật `FORCE_REFRESH`.

Checkpoint được lưu sau mỗi 10 mã ở KLGD 20 và GTGD 20, mỗi 50 mã ở GTGD 60, khi xử lý rate limit và khi kết thúc. Dừng thủ công giữa hai lần lưu có thể khiến một số mã vừa xử lý phải chạy lại. Sang ngày dữ liệu mới, chương trình bắt đầu lượt mới thay vì tiếp tục lượt ngày cũ.

### Vốn hóa và file kết quả

Vốn hóa không dùng checkpoint. Chạy lại toàn bộ cell 5–9 để lấy bảng giá mới, tạo lại bảng vốn hóa và xuất file. Chỉ chạy cell xuất Excel sẽ ghi lại dữ liệu đang giữ trong bộ nhớ.

File kết quả cuối giữ nguyên tên và được ghi đè khi chạy đến bước xuất thành công. Nếu dừng trước bước xuất, file cuối có thể vẫn chứa dữ liệu cũ. Sao lưu hoặc đổi tên file trước khi cập nhật nếu cần giữ lịch sử; checkpoint theo ngày không thay thế kho lưu trữ lịch sử.

## 6. Công thức và kiểm tra dữ liệu

| Chỉ tiêu | Cách tính trong notebook | Đơn vị |
| --- | --- | --- |
| KLGD 20 | Trung bình `volume` của 20 phiên, làm tròn số nguyên | Cổ phiếu/phiên |
| GTGD 20 | Trung bình `close × volume / 1_000_000` của 20 phiên | Tỷ đồng/phiên |
| GTGD 60 | Trung bình `close × volume / 1_000_000` của 60 phiên | Tỷ đồng/phiên |
| Vốn hóa | `Giá khớp × SLCP niêm yết`, chia `1_000_000_000` để ra tỷ đồng | VND hoặc tỷ đồng |

GTGD là giá trị **ước tính từ giá đóng cửa nhân khối lượng**, không phải tổng giá trị khớp lệnh thực tế trong phiên. Công thức GTGD giả định `close` có đơn vị nghìn đồng/cổ phiếu. Công thức vốn hóa hiện giả định giá khớp từ bảng giá là VND/cổ phiếu và sử dụng số cổ phiếu niêm yết; cần đối chiếu đơn vị nguồn khi thay phiên bản thư viện hoặc nguồn dữ liệu.

Chỉ tiêu lịch sử chỉ có giá trị khi đủ 20 hoặc 60 phiên hợp lệ. Mã thiếu phiên hoặc không có dữ liệu được để trống chỉ tiêu. Mỗi file lịch sử có sheet kết quả (`KLDG_20`, `GTGD_20`, `GTGD_60`) và sheet `Kiem_tra` chứa các mã có trạng thái khác `OK`.

Dùng `So_phien`, `Tu_ngay`, `Den_ngay`, `Trang_thai` để đối chiếu cửa sổ tính. Trạng thái bắt đầu bằng `LOI_CAN_THU_LAI` được thử lại khi tiếp tục checkpoint. Lỗi không có dữ liệu do API ném exception cũng có thể được ghi dưới trạng thái này.

## 7. MySQL: đang thử nghiệm

**Database chưa hoàn tất và chưa tích hợp với notebook.** `test_mysql.py` chỉ kiểm tra kết nối và đọc tên database, phiên bản MySQL, charset, collation. Kết nối thành công không có nghĩa là bảng đã được tạo hoặc dữ liệu đã được nhập.

Để thử nghiệm, chuẩn bị một MySQL server và database riêng rồi khai báo trong `.env` tại thư mục gốc:

```dotenv
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=your_test_user
MYSQL_PASSWORD=your_test_password
MYSQL_DATABASE=your_test_database
```

Chạy từ thư mục gốc sau khi kích hoạt `.venv`:

```powershell
python test_mysql.py
```

Script dùng SQLAlchemy với driver PyMySQL và charset `utf8mb4`. Script không tự tạo database, bảng hoặc nhập Excel. Có thể chạy notebook xuất Excel độc lập mà không chạy thử nghiệm MySQL.

## 8. Các vấn đề thường gặp

| Hiện tượng | Cách xử lý |
| --- | --- |
| `ModuleNotFoundError` | Kiểm tra kernel và cài thư viện bằng Python của `.venv`. |
| `ZoneInfoNotFoundError` | Cài `tzdata` trong `.venv`, sau đó khởi động lại kernel. |
| Rate limit | Để cell chờ và thử lại; tránh chạy nhiều lượt tải đồng thời. Delay hiện tại không đảm bảo mọi lượt gọi đều tránh được giới hạn. |
| Excel báo `PermissionError` | Đóng file Excel kết quả hoặc checkpoint đang mở rồi chạy lại. |
| Không còn mã cần xử lý khi chạy lại | Checkpoint cùng ngày đã hoàn thành; bật `FORCE_REFRESH = True` khi cần tải lại. |
| Không tìm thấy checkpoint | Kiểm tra `Path.cwd()`, ngày dữ liệu và tên file. |
| MySQL không kết nối | Kiểm tra server, quyền tài khoản, database thử nghiệm và `.env`; `MYSQL_PORT` phải là số nguyên hợp lệ. |

## 9. Phần chưa hoàn tất

- Chuẩn hóa bảng dữ liệu tổng hợp và hoàn thiện `Processed.xlsx`.
- Thiết kế schema, khóa dữ liệu và cách lưu lịch sử trong MySQL.
- Xây dựng luồng nhập dữ liệu, kiểm tra chất lượng và cập nhật database.
- Tách notebook thành các module có thể chạy theo lịch.
- Hoàn thiện quản lý cấu hình, phiên bản thư viện và thông tin xác thực.

Đây là các công việc dự kiến, chưa phải chức năng đã triển khai.
