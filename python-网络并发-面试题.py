from collections import deque
import time

def hot_potato(children):
    queue = deque(children)
    while len(queue) > 1:
        for _ in range(7):   # 每7秒传递一次山芋
            queue.append(queue.popleft())  # 山芋传递给下一个孩子
        queue.popleft()  # 计时7秒后，当前持有山芋的孩子退出游戏
    return queue[0]  # 返回最后剩下的孩子

# 假设有6个孩子，编号为1到6
children = list(range(1, 7))
winner = hot_potato(children)
print(f"排在第{winner}个位置的孩子最终会获胜。")