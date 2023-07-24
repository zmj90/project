# 固定的递归方法，需要记住
res = []  # 定义全局变量


def dfs(wait, stack, out):
    if not wait and not stack:
        res.append(' '.join(map(str, out)))
    if wait:  # 入栈，一开始一股脑都入栈
        dfs(wait[1:], stack + [wait[0]], out)
    if stack:  # 出栈，之后慢慢出栈
        dfs(wait, stack[:-1], out + [stack[-1]])


n, nums = int(input()), list(map(int, input().split()))

dfs(nums, [], [])
print(res)
for i in sorted(res):
    print(i)

