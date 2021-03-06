# 다수의 자연수에 대하여 소수 여부를 판별할 때 사용
# 1. 2부터 N까지의 모든 자연수를 나열
# 2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
# 3. 남은 수 중에서 i의 배수를 모드 제거한다(i는 제거하지 않는다)
# 4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다.
import math


# 시간 복잡도 O(NloglogN)
def is_prime_number(x):
    number = set(range(2, x+1))

    for i in range(2, int(math.sqrt(x))+1):
        if i in number:
            number -= set(range(i*2, x+1, i))

    return number


print(is_prime_number(26))
