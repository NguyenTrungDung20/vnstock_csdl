# Chạy lệnh và nhập API key theo hướng dẫn
from vnstock import register_user
register_user('vnstock_4810571b41e9042d4a16bb11b0a6264f')
# hoặc nhập trực tiếp API key vào hàm register_user
# register_user('YOUR_API_KEY')


# Import các module của vnstock
from vnstock import Listing, Quote, Company, Finance, Trading

# Cách khác: Import từ nguồn dữ liệu cụ thể
# from vnstock.explorer.vci import Listing, Quote, Company, Finance, Trading
# from vnstock.explorer.tcbs import Quote, Company, Finance, Trading

print("✅ Tất cả modules đã được import thành công!")


