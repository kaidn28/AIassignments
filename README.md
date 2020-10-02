# AIassignments
# pacman AI 

Q1:
- tạo 1 fringe là một stack chứa node start, một list visited chứa các điểm đã xét 
- Lặp tới khi fringe rỗng với node hiện tại = fringe.pop(), tìm các successor xung quanh node hiện tại, cho vào fringe nếu chưa xét
- trả về đường đi khi đến goal

Q2:
- tạo 1 fringe là một queue, một list expanded chứa các điểm đã được mở rộng đến
- Lặp tới khi hết fringe với node hiện tại = fringe.pop(), tìm các successors của node hiện tại, cho vào fringe nếu chưa được expanded
- trả về đường đi khi đến goal

Q3:
- tạo fringe là một list, và 1 list khác để chứa các node đã xét
- lặp  với node hiện tại bằng phần tử đầu trong fringe, lấy successors, nếu chưa xét thì thêm vào fringe, nếu xét rồi thì thay đổi khoảng cách đến successor đó nếu khoảng cách mới nhỏ hơn
- trả về đường đi khi đến goal

Q4:
- tạo fringe là một list chứa node và f(node) = h(node) + g(node), và một list để chứa các điểm đã xét
- lặp tới khi fringe rỗng: sắp xếp fringe theo f, node hiện tại = fringe.pop(), chọn successor chưa xét, nếu không có trong fringe thì cho vào, nếu có rồi thì kiểm tra xem khoảng cách mới có gần hơn không, nếu có thì thay bằng khoảng cách mới
- trả vê đường đi khi đến goal

Q5:
- getStartState() trả về vị trí khởi đầu và list các corner đã đi qua
- isGoalState() check xem đã đi qua cả 4 corner đi chưa bằng chiều dài của list các corner đã đi qua
- getSuccesors() trả về các successors xung quanh và update list các corner đã đi qua nếu đó là một corner mới
- Sau khi có 3 hàm này thì để bfs làm việc của nó

Q6:
- Tính h bằng khoảng cách manhattan của từng corner lần lượt là từ state -> corner 1 gần nhất -> corner 2 gần corner 1 nhất -> corner 3 gần corner 2 nhất
- Để A* làm việc của nó 



