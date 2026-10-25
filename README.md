# Daniel's Number

A 1,021-digit proven Proth prime, recorded on October 25, 2026.

\[
N = 3796246154436756844729658716967717237708627977410256704163 \cdot 2^{3200} + 1.
\]

**FactorDB:** [Entry 1100000012037487955](https://factordb.com/index.php?id=1100000012037487955), listed as a proven prime using a Pocklington N−1 test (base 3).

## Primality proof

Let `k = 3796246154436756844729658716967717237708627977410256704163` and `N = k * 2**3200 + 1`. Since `k` is odd, `0 < k < 2**3200`, and

`pow(3, (N-1)//2, N) == N-1`,

Proth's theorem establishes that `N` is prime. Run `python3 verify.py` to check this certificate using Python's built-in arbitrary-precision integers.

## Provenance and attribution

The candidate was generated through a ChatGPT-assisted search on October 25, 2026, and the primality result was subsequently recorded on FactorDB. We call it **Daniel's Number**. The name is informal, not an official mathematical designation. This record does not establish that nobody previously computed the same prime. FactorDB's creation date is not proof of global priority.

## Contents

- `number.txt`: complete decimal expansion.
- `verify.py`: deterministic verification of the Proth certificate.
- `certificate.txt`: human-readable mathematical certificate.

## Citation

Cite this repository's permanent commit URL or an archived release. For a DOI, archive a release with Zenodo.
