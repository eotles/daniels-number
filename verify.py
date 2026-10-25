"""Verify Daniel's Number via Proth's theorem (Python 3, no dependencies)."""
from pathlib import Path

K = 3796246154436756844729658716967717237708627977410256704163
EXPONENT = 3200
WITNESS = 3


def verify():
    n = K * (1 << EXPONENT) + 1
    assert K % 2 == 1 and 0 < K < (1 << EXPONENT)
    assert pow(WITNESS, (n - 1) // 2, n) == n - 1
    assert str(n) == Path(__file__).with_name('number.txt').read_text().strip()
    print(f'Proven prime: {len(str(n))} digits; Proth witness {WITNESS}')


if __name__ == '__main__':
    verify()
