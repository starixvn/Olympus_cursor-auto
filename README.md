# Chương trình tự động gõ chữ

Chương trình này giúp tự động gõ chữ vào Cursor AI hoặc bất kỳ cửa sổ nào khác.

## Cài đặt

1. Đảm bảo bạn đã cài đặt Python 3.x
2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

## Cách sử dụng

1. Chạy chương trình:
```bash
python auto_type.py
```

2. Sau khi chạy, bạn có 5 giây để chuyển sang cửa sổ Cursor hoặc cửa sổ nơi bạn muốn gõ chữ
3. Nhấn F2 để bắt đầu gõ chữ
4. Nhấn F3 để thoát chương trình

## Tùy chỉnh

Bạn có thể thay đổi văn bản cần gõ bằng cách sửa biến `text` trong hàm `main()` của file `auto_type.py`

## Lưu ý

- Đảm bảo cửa sổ đích đang được focus khi chương trình bắt đầu gõ
- Có thể điều chỉnh tốc độ gõ bằng cách thay đổi giá trị `time.sleep()` trong hàm `auto_type()` 