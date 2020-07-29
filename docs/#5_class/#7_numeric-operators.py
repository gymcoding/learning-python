#-- 수치 연산자
# ● 수치 연산자
#   ○ __add__(self, other)
#     - 연산자: + (이항)
#     - 사용 예: A + B, A += B
#   ○ __sub__(self, other)
#     - 연산자: - (이항)
#     - 사용 예: A + B, A -= B
#   ○ __mul__(self, other)
#     - 연산자: *
#     - 사용 예: A * B, A *= B
#   ○ __truediv__(self, other)
#     - 연산자: /
#     - 사용 예: A / B, A /= B (3이상 지원, 그 이하 버전에서는 __div__가 사용)
#   ○ __floordiv__(self, other)
#     - 연산자: //
#     - 사용 예: A // B, A //= B
#   ○ __mod__(self, other)
#     - 연산자: %
#     - 사용 예: A % B, A %= B
#   ○ __divmod__(self, other)
#     - 연산자: divmod()
#     - 사용 예: divmod(A, B)
#   ○ __pow__(self, other[, modulo])
#     - 연산자: pow(), **
#     - 사용 예: pow(A, B), A ** B
#   ○ __lshift__(self, other)
#     - 연산자: <<
#     - 사용 예: A << B, A <<= B