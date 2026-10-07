# Security Policy & Glass-Box Safety Guarantees

## 1. Supported Versions
We actively maintain and provide security patches for the following versions of the **Neural Semantic Protocol (NSP)**:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

---

## 2. Core Safety Architecture (Glass-Box Invariants)

NSP is designed specifically to prevent unconstrained AI agent rogue behavior and covert machine communication.

All compliant implementations MUST adhere to the following **Zero-Stealth Security Invariants**:
1. **Deterministic Bi-Directional Decodability:** No agent may transmit symbolic payloads (`⟪...⟫`) that cannot be deterministically decoded by the Human Inspector into clear, unambiguous natural language.
2. **Cryptographic Intent Hashing (`Σ:hash`):** Every packet MUST carry a tamper-proof SHA-256 truncated signature of its causal ancestry, preventing man-in-the-middle payload alterations across agent hops.
3. **Emergency Halt Invariant (`0x99 EMERGENCY_HALT`):** The human owner retains non-negotiable authority. Any halt command immediately revokes lock acquisition and flushes memory buffers.
4. **Prohibition of Steganographic Latent States:** Encoding arbitrary executable byte blobs or steganographic text inside proofs (`π:...`) is strictly classified as a protocol violation (`0xFF SAFETY_REJECT`).

---

## 3. Reporting a Vulnerability

If you discover a security vulnerability, covert communication exploit, or safety misalignment within the NSP reference implementation:

1. **Do NOT open a public GitHub issue.**
2. Send an email to the security response team:
   * **Lead Architect:** `jasper@antigravity.ai`
   * **Subject:** `[SECURITY] NSP Vulnerability Report - <Brief Summary>`
3. Include detailed reproduction steps, example serialized frames, and affected model endpoints.

We acknowledge all valid security reports within **24 hours** and aim to release coordinated security patches within **72 hours**.

---

## 4. Responsible Disclosure & Bug Bounty
We appreciate researchers who practice responsible disclosure. Verified vulnerability reporters will be credited in our official release notes and security advisories.
