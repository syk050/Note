# 연속적으로 나열된 n개의 수가 있을 때 특정 구간의 모든 수를 합한 값을 계산하는 문제
# ex)   n개의 정수로 구성된 수열이 있을 때
#       m개의 쿼리 정보가 주어짐
#           - 각 쿼리는 left, right로 구성
#             - 각 쿼리에 대하여 [left, right] 구간에 포함된 데이터들의 합을 출력
#       수행 시간은 O(n+m)
#       => 접두사 합: 배열의 맨 앞부터 특정 위치까지의 합을 미리 구함
#           - n개의 수 위치 각각에 대하여 접두사 합을 계산해 p에 저장
#           - 매 m개의 쿼리 정보를 확인할 때 구간 합은 p[right] - p[left-1]
def sol(data):
    p = [0]
    hap = 0
    for i in data:
        hap += i
        p.append(hap)

    left = 3
    right = 5

    return p[right] - p[left-1]


print(sol([10, 20, 30, 40, 50]))
