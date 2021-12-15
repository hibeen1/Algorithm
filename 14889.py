from itertools import combinations
import itertools
def my_code():
    # 2108ms 54592KB
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    def sum_score(team):
        result = 0
        for x in team:
            for y in team:
                result += graph[x][y]
        return result

    people = []
    for i in range(n):
        people.append(i)

    people = list(combinations(people, int(n/2)))
    a_team = []
    b_team = []

    result = int(1e9)

    for i in range(int(len(people)/2)):
        a_team = people[i]
        b_team = people[-i-1]
        a_sum = sum_score(a_team)
        b_sum = sum_score(b_team)
        result = min(result, abs(a_sum - b_sum))
    print(result)

def best_code():
    # 128ms 29200 KB
    # 무슨 논리인 지 모르겠다.
    N = int(input())
    S = [[int(x) for x in input().split()] for _ in range(N)]
    row_sums = [sum(row) for row in S]
    col_sums = [sum(col) for col in zip(*S)]
    stat_by_member = [x + y for x, y in zip(row_sums, col_sums)]
    total = sum(row_sums)
    min_diff = min(
        abs(total - sum(stats))
        for stats in itertools.combinations(stat_by_member, N // 2))

    print(min_diff)

best_code()