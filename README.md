# 3List: A Quantum Algorithm for 3-Tuple Lattice Sieving 
Repository accompanying the paper _An Improved Quantum Algorithm for 3-Tuple Lattice Sieving_, to appear in the Proceedings of CRYPTO 2026. 


## Contents 
- `verify_3list.py` — verifies the time-complexity analysis of 3List in the proof of Theorem 3.1 (arXiv/ePrint), respectively Theorem 1 (Proceedings). 

## Usage 

Requires Python 3, no dependencies beyond the standard library.  

Run: 

```
python verify_3list.py
```

Expected output: 
```
Time exponent: 0.284551 (claimed exponent: 0.284551)
```

## Reference 

Lynn Engelberts, Yanlin Chen, Amin Shiraz Gilani, Maya-Iggy van Hoof, Stacey Jeffery, Ronald de Wolf. _An Improved Quantum Algorithm for 3-Tuple Lattice Sieving_. CRYPTO 2026. arXiv:[2510.08473](https://arxiv.org/abs/2510.08473). ePrint:[2025/2189](https://eprint.iacr.org/2025/2189.pdf). 
