                 Coal or Candy ?
                          Group 6
Thành Viên:
Nguyễn Công Thành
Trần Thiên Ân
Ca Ngọc Tân
Nguyễn Tuấn Anh
Trần Phát

I. Nội dung game
1. Giới thiệu tổng quan
Tên game: Coal or Candy? (Quà xấu hay quà tốt).
•	Ý tưởng:
Dựa trên không khí lễ Giáng sinh, chúng em muốn tạo ra một trò chơi thú vị, nhẹ nhàng với thông điệp khuyến khích hành động tốt. Trò chơi mang lại niềm vui cho người chơi thông qua cơ chế đơn giản, đồ họa thân thiện, và những thử thách hài hước.
2. Thành phần trong game
•	Nhân vật chính:
Một cậu bé/cô bé cùng chiếc giỏ dùng để hứng quà từ ông già Noel.
•	Vật thể rơi:
o	Quà tốt (Candy): Dành cho trẻ ngoan, tăng điểm hoặc tăng thời gian chơi.
o	Quà xấu (Coal): Dành cho trẻ hư, giảm điểm, giảm thời gian hoặc kết thúc game.
•	Bối cảnh:
Một không gian ấm cúng, như phòng khách với bếp lửa, cây thông, và đèn trang trí.
3. Cơ chế chính của game
•	Di chuyển giỏ:
Sử dụng các phím mũi tên để điều khiển giỏ, đón những món quà rơi xuống.
•	Vật thể rơi ngẫu nhiên:
Quà và vật thể xuất hiện ngẫu nhiên từ trên xuống, tăng dần tốc độ qua thời gian.
•	Tính điểm:
o	Nhận quà tốt: +1 điểm (hoặc thêm thời gian).
o	Nhận quà xấu: -1 điểm, giảm thời gian, hoặc kết thúc game.
•	Kết thúc game:
Hiển thị "Game Over" khi người chơi:
o	Hết thời gian.
o	Hứng phải quà xấu khiến trò chơi dừng.
4. Cơ chế bổ sung sáng tạo
•	Thời gian giới hạn:
Người chơi phải thu thập quà trong thời gian nhất định, với cơ chế:
o	Quà tốt: Tăng thời gian.
o	Quà xấu: Giảm thời gian.
•	Tăng độ khó:
o	Quà rơi ngày càng nhanh.
o	Hiệu ứng "gió bay" khiến quà lệch vị trí.
•	Hiệu ứng đặc biệt:
o	Quà đặc biệt:
	+5 điểm.
	Tăng x2 điểm trong 10s.
	Làm chậm tốc độ rơi quà trong vài giây.
	Xóa hết quà xấu trên màn hình.
o	Quà bẫy:
	Làm nhân vật bị đóng băng trong 5s.
•	Chướng ngại vật:
Thỉnh thoảng, các vật thể khác như cục tuyết, gậy kẹo sẽ rơi xuống, khiến người chơi phải né tránh.
•	Chế độ 2 người chơi:
Hai người chơi có thể thi đấu bằng cách điều khiển hai giỏ quà riêng biệt, xem ai ghi được nhiều điểm hơn trong thời gian giới hạn.
•	Màn chơi đa dạng:
Các thành phố lớn như Tokyo, New York, Paris… với nền, âm thanh, và đồ họa khác biệt tạo sự mới lạ.
________________________________________
II. Quy trình thiết kế game trên Python
1. Phân chia công việc
1.	Thiên Ân - Thiết kế nhân vật và vật thể
o	Tạo hình nhân vật (cậu bé/cô bé) và giỏ.
o	Thiết kế các vật thể như quà tốt (xe đồ chơi, quần áo mới, máy nghe nhạc...) và quà xấu (vỏ lon, túi nhựa, đồ ăn hỏng...).
o	Sử dụng thư viện Pygame hoặc các hàm vẽ như pygame.draw.rect, pygame.draw.circle để vẽ hoặc tải hình ảnh từ file.
2.	Ngọc Tân - Lập trình chuyển động của giỏ
o	Điều khiển giỏ bằng phím mũi tên hoặc chuột thông qua các sự kiện pygame.KEYDOWN.
o	Giới hạn phạm vi di chuyển của giỏ trong màn hình.
o	Xử lý va chạm giữa giỏ và vật thể để nhận diện việc "bắt" quà.
3.	Tuấn Anh - Lập trình vật thể rơi
o	Tạo cơ chế cho vật thể xuất hiện ngẫu nhiên tại các vị trí trên màn hình.
o	Lập trình quà rơi từ trên xuống, tăng tốc độ theo thời gian.
o	Phân biệt rõ ràng giữa quà tốt và quà xấu để cập nhật điểm số.
4.	Trần Phát - Xử lý điểm và kết thúc game
o	Hiển thị và cập nhật điểm số liên tục.
o	Quy định điều kiện kết thúc game, ví dụ: hứng phải quà xấu hoặc hết thời gian.
o	Hiển thị màn hình "Game Over" và điểm cuối cùng của người chơi.
5.	Công Thành - Thiết kế giao diện và hiệu ứng
o	Xây dựng nền game (phòng khách, cây thông, bếp lửa…).
o	Thêm âm thanh và hiệu ứng:
	Âm thanh khi hứng quà.
	Hiệu ứng rung hoặc flash khi hứng quà xấu.
o	Hiển thị các thông tin như điểm số, thời gian còn lại, và thông báo "Game Over".
2. Tổng hợp và kiểm tra
•	Tích hợp các thành phần:
Ghép tất cả phần lập trình của các thành viên thành một project Pygame hoàn chỉnh.
•	Kiểm tra và sửa lỗi:
Test các tình huống trong game để đảm bảo cơ chế hoạt động trơn tru.
•	Cải tiến:
Tinh chỉnh đồ họa, tăng độ khó hợp lý, và tối ưu hiệu suất.
________________________________________
III. Kế hoạch quản lý dự án
1.	Mốc thời gian:
o	Thiết kế từng phần: 2 tuần.
o	Tích hợp và kiểm tra: 1 tuần.
o	Chỉnh sửa và cải tiến: 1 tuần.
2.	Công cụ sử dụng:
o	Python (Pygame): Lập trình game.
o	Trello/Google Docs: Quản lý công việc và trao đổi nhóm.
3.	Đánh giá tiến độ:
o	Thường xuyên báo cáo công việc hàng tuần.
o	Chạy thử nghiệm từng thành phần trước khi tích hợp.
________________________________________
IV. Kết luận
Dự án "Coal or Candy?" không chỉ mang tính giải trí mà còn truyền tải thông điệp về hành vi tốt xấu trong mùa lễ hội. Chúng em hy vọng trò chơi sẽ mang lại niềm vui cho người chơi, đồng thời rèn luyện kỹ năng lập trình và làm việc nhóm hiệu quả.

Open the main.exe to play.
