Mô tả chi tiết:
assets/: Lưu hình ảnh, âm thanh, phông chữ để game chuyên nghiệp hơn.
src/: Chứa toàn bộ code của trò chơi.
main.py: Xử lý menu chính và điều hướng giữa các màn hình.
game.py: Điều khiển rắn, xử lý va chạm, ăn mồi, cập nhật điểm.
menu.py: Giao diện menu chính với các nút Play, Help, About, Quit.
settings.py: Lưu cấu hình trò chơi (ví dụ: tốc độ rắn, danh sách màn chơi).
game_over.py: Hiển thị điểm, cho phép chọn Chơi lại hoặc Quay về menu.
highscore.py: Ghi và đọc điểm số cao nhất từ data/highscore.json.
utils.py: Hàm hỗ trợ như tải ảnh, âm thanh.
maps/: Lưu dữ liệu bản đồ, có thể thêm nhiều màn chơi.
data/: Lưu thông tin người chơi như điểm cao nhất.
README.md: Hướng dẫn cách chơi và cài đặt game.
requirements.txt: Danh sách thư viện cần thiết (pygame, json,...).
💡 Ưu điểm của cấu trúc này:
✔ Dễ mở rộng với các màn chơi khác nhau.
✔ Hỗ trợ nhiều loại mồi, bản đồ, tốc độ.
✔ Quản lý tài nguyên (hình ảnh, âm thanh) tốt hơn.
✔ Lưu dữ liệu người chơi (điểm cao nhất).