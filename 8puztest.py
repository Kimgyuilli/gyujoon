import cv2
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import Button
from queue import PriorityQueue

class State:
    goal_positions = {}  # 목표 상태의 각 숫자의 위치를 저장하는 딕셔너리

    def __init__(self, board, moves=0):
        self.board = board  # 현재 상태의 퍼즐 보드
        self.moves = moves  # 현재까지의 이동 횟수
        self.key = tuple(tuple(row) for row in board)  # 상태의 고유 키(불변 튜플) 생성

    def __lt__(self, other):
        #비교 연산자
        return self.f() < other.f()

    def f(self):
        #상태함수 f(n) = g(n) + h(n)
        return self.g() + self.h()

    def g(self):
        #현재까지의 경로 비용
        return self.moves

    def h(self):
        #휴리스틱 함수
        dist = 0
        size = 3
        for i in range(size):
            for j in range(size):
                place = self.board[i][j]
                if place != 0:
                    goal_x, goal_y = self.goal_positions[place]
                    dist += abs(goal_x - i) + abs(goal_y - j)
        return dist

def astar(start: State, goal) -> dict:
# A* 알고리즘 구현
    que = PriorityQueue()
    que.put(start)
    marked = {start.key: None}
    while not que.empty() and (current := que.get()).board != goal:
        for state in expand(current):
            if state.key not in marked:
                marked[state.key] = current.key
                que.put(state)
    return marked

def exchange(state: State, prev_pos: tuple, new_pos: tuple) -> State:
# 빈칸(0)과 인접한 타일을 교환하여 새로운 상태 생성
    new_board = [row[:] for row in state.board]
    new_board[prev_pos[0]][prev_pos[1]], new_board[new_pos[0]][new_pos[1]] = new_board[new_pos[0]][new_pos[1]], new_board[prev_pos[0]][prev_pos[1]]
    return State(new_board, state.moves + 1)

def expand(state: State) -> list:
# 현재 상태에서 가능한 모든 다음 상태 생성
    result = []
    size = 3
    zero_pos = next((i, j) for i in range(size) for j in range(size) if state.board[i][j] == 0)

    if zero_pos[0] > 0:  # UP
        result.append(exchange(state, zero_pos, (zero_pos[0] - 1, zero_pos[1])))
    if zero_pos[1] > 0:  # LEFT
        result.append(exchange(state, zero_pos, (zero_pos[0], zero_pos[1] - 1)))
    if zero_pos[1] < size - 1:  # RIGHT
        result.append(exchange(state, zero_pos, (zero_pos[0], zero_pos[1] + 1)))
    if zero_pos[0] < size - 1:  # DOWN
        result.append(exchange(state, zero_pos, (zero_pos[0] + 1, zero_pos[1])))
    return result

def print_path(start, goal, marked):
# 시작 상태에서 목표 상태까지의 경로 출력
    path = []
    node = tuple(tuple(row) for row in goal)
    while node != tuple(tuple(row) for row in start):
        path.append(node)
        node = marked[node]
    path.append(tuple(tuple(row) for row in start))
    prev_pos = None
    for each in path[::-1]:
        current_pos = next((i, j) for i, row in enumerate(each) for j, val in enumerate(row) if val == 0)
        if prev_pos:
            img_list[(current_pos[0]*3) + current_pos[1]], img_list[(prev_pos[0]*3) + prev_pos[1]] = img_list[(prev_pos[0]*3) + prev_pos[1]], img_list[(current_pos[0]*3) + current_pos[1]]
            for i, ax in enumerate(axes.flatten()):
                ax.clear()
                ax.imshow(img_list[i])
                ax.axis('off')
            plt.draw()
            plt.pause(0.1)
        prev_pos = current_pos
    plt.clf()
    ax = plt.subplot(1, 1, 1)
    ax.axis('off')
    ax.imshow(completed_image)
    plt.text(250, 130, 'Clear', horizontalalignment='center', verticalalignment='center', fontsize=30)
    plt.draw()
    print("이동횟수 = ", len(path) - 1)

def read_image(img_path):
    #이미지 파일 읽고 BGR에서 RGB로 변환
    img = cv2.imread(img_path)
    if img is not None:
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    else:
        print(f"Error loading image {img_path}")
        return np.zeros((100, 100, 3), dtype=np.uint8)

def get_inversion_count(arr):
    #역순 쌍 개수 계산
    inv_count = 0
    arr = [i for i in arr if i != 0]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count

def get_solvable_puzzle(img_list):
    #풀 수 있는 퍼즐 상태 생성
    while True:
        puzzle = random.sample(img_list, 9)
        flat_puzzle = [int(path.split('_')[-1].split('.')[0]) if 'num_0' not in path else 0 for path in puzzle]
        inversion = get_inversion_count(flat_puzzle)
        if inversion % 2 == 0:
            return puzzle, flat_puzzle

img_list1 = [
    "8-puzzle/num_1.jpg", "8-puzzle/num_2.jpg", "8-puzzle/num_3.jpg",
    "8-puzzle/num_4.jpg", "8-puzzle/num_5.jpg", "8-puzzle/num_6.jpg",
    "8-puzzle/num_7.jpg", "8-puzzle/num_8.jpg", "8-puzzle/num_0.png"
]

solved = [read_image(path) for path in img_list1]
img_list2, flat_puzzle = get_solvable_puzzle(img_list1)
img_list = [read_image(path) for path in img_list2]
img0 = read_image("8-puzzle/num_0.png")
completed_image = read_image("8-puzzle/numa.jpg")

Nlist = [flat_puzzle[i:i + 3] for i in range(0, len(flat_puzzle), 3)]
State.goal_positions = {val: (i // 3, i % 3) for i, val in enumerate(range(9))}

def find_zero_position(images):
    #빈 칸의 위치 찾기
    for idx, img in enumerate(images):
        if np.array_equal(img, img0):
            return idx
    return -1

def is_adjacent(pos1, pos2):
    #두 위치가 인접한지 확인
    if pos1 == pos2:
        return False
    row1, col1 = divmod(pos1, 3)
    row2, col2 = divmod(pos2, 3)
    return abs(row1 - row2) + abs(col1 - col2) == 1

def add_point(event):
    """마우스 클릭 이벤트 처리"""
    if event.button == 1:
        click_idx = next((i for i, ax in enumerate(axes.flatten()) if ax == event.inaxes), None)
        if click_idx is not None:
            zero_idx = find_zero_position(img_list)
            if is_adjacent(click_idx, zero_idx):
                img_list[click_idx], img_list[zero_idx] = img_list[zero_idx], img_list[click_idx]
                flat_Nlist = sum(Nlist, [])
                flat_Nlist[click_idx], flat_Nlist[zero_idx] = flat_Nlist[zero_idx], flat_Nlist[click_idx]
                Nlist[:] = [flat_Nlist[i:i + 3] for i in range(0, len(flat_Nlist), 3)]
                for i, ax in enumerate(axes.flatten()):
                    ax.clear()
                    ax.imshow(img_list[i])
                    ax.axis('off')
                plt.draw()

                solved_flag = all(np.array_equal(img1, img2) for img1, img2 in zip(img_list, solved))

                if solved_flag:
                    plt.clf()
                    ax = plt.subplot(1, 1, 1)
                    ax.axis('off')
                    ax.imshow(completed_image)
                    plt.text(250, 130, 'Clear', horizontalalignment='center', verticalalignment='center', fontsize=30)
                    plt.draw()

def solve(event):
    #A* 알고리즘을 사용하여 퍼즐 해결
    start_board = Nlist
    goal_board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    start = State(start_board)
    State.goal_positions = {val: (i // 3, i % 3) for i, val in enumerate(sum(goal_board, []))}
    marked = astar(start, goal_board)
    print_path(start.board, goal_board, marked)
    print("탐색 횟수 = ", len(marked))
    print("시작 상태", '\n', start.board)

fig, axes = plt.subplots(3, 3, figsize=(5, 5))
for i, img in enumerate(img_list):
    ax = plt.subplot(3, 3, i + 1)
    ax.axis('off')
    ax.imshow(img)
ax_button = plt.axes([0.7, 0.025, 0.1, 0.04])
button = Button(ax_button, 'Solve')
button.on_clicked(solve)
cid = fig.canvas.mpl_connect('button_press_event', add_point)
plt.subplots_adjust(wspace=0.01, hspace=0.02)
plt.show()
