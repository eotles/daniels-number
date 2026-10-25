# Daniel's Number

A 1,021-digit proven Proth prime, recorded on October 25, 2026.

\[
N = 3796246154436756844729658716967717237708627977410256704163 \cdot 2^{3200} + 1.
\]

**FactorDB:** [Entry 1100000012037487955](https://factordb.com/index.php?id=1100000012037487955), listed as a proven prime using a Pocklington N−1 test (base 3).

## Dedication

**Daniel's Number is named in honor of [Dr. Daniel James Comeaux, MD](https://anesthesia.wisc.edu/education-training/residencies/recent-graduates/)**, a 2025 graduate of the University of Wisconsin anesthesiology residency, listed by the department as practicing at Advocate Good Shepherd in Illinois. The name is a personal dedication, not an established mathematical naming convention or a claim that Dr. Comeaux participated in the computation.

## Primality proof

Let `k = 3796246154436756844729658716967717237708627977410256704163` and `N = k * 2**3200 + 1`. Since `k` is odd, `0 < k < 2**3200`, and

`pow(3, (N-1)//2, N) == N-1`,

Proth's theorem establishes that `N` is prime. Run `python3 verify.py` to check this certificate using Python's built-in arbitrary-precision integers.

## Verify locally

Requires Python 3, with no third-party dependencies:

```bash
python3 verify.py
```

The script checks the Proth conditions, verifies the modular-exponentiation witness, and compares the computed integer to `number.txt`. This is a deterministic proof of primality, not just a probable-prime test.

## Provenance and attribution

The candidate was generated through a ChatGPT-assisted search on October 25, 2026, and the primality result was subsequently recorded on FactorDB. We call it **Daniel's Number**. The name is informal, not an official mathematical designation. This record does not establish that nobody previously computed the same prime. FactorDB's creation date is not proof of global priority.

## Contents

- `number.txt`: complete decimal expansion.
- `verify.py`: deterministic verification of the Proth certificate.
- `certificate.txt`: human-readable mathematical certificate.

## Citation

Use the repository's **Cite this repository** menu (powered by `CITATION.cff`), or cite a versioned Zenodo DOI after the first release is archived. A DOI is a persistent record of this documentation, not independent proof of historical discovery priority.
