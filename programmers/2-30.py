class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = dict()


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, string):
        if len(string) == 1:
            return 0
        now = self.root
        for i in string:
            if now.child.get(i):
                now = now.child[i]
            else:
                now.child[i] = Node(i)
                now = now.child[i]
        if now.data:
            return 0
        now.data = 1
        return 1


def solution(n, words):
    answer = [0, 0]
    trie = Trie()
    dummy = ''
    for idx, i in enumerate(words):
        if dummy:
            if dummy[-1] != i[0]:
                answer = [idx % n+1, idx//n+1]
                break
        if not trie.insert(i):
            answer = [idx % n+1, idx//n+1]
            break
        dummy = i
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer
