## My independent verdict (formed BEFORE steelmanning)

The methodology supports refuting the *narrow* subclaim in `audit_premises_README.md:18-20`: a reciprocal, unrestricted FTL signalling rule with speed `alpha > 1` in each sender's inertial rest frame is incompatible with ordinary Lorentz transformations without causal loops. The algebra in `audit_script.py:75-90` matches the standard tachyonic-antitelephone construction, and the threshold

```text
beta > 2 alpha / (1 + alpha^2)
```

follows from the numerator printed in `audit_raw_output.txt:15-16`.

However, the audit is inconclusive for the broader claim in `claim_statement_only.md:9-11`. The broader claim is about controllable FTL communication or transportation under established physics and positive-energy matter; this audit checks only one flat-spacetime communication law. The important physics assumption is not "FTL" alone but `audit_premises_README.md:29`: "B immediately replies with the same FTL rule in B's rest frame." If the actual FTL mechanism has a preferred frame, an effective metric, a one-way constraint, a finite operating domain, or a chronology-protection obstruction, this calculation does not apply.

## Strongest defense of the opposing position

The strongest defense is essentially the one stated by Liberati, Sonego, and Visser: causality cannot be decided from the words "faster than c" alone; the propagation law matters. The audit assumes the most dangerous law: arbitrary bidirectional FTL at the same superluminal speed in each local sender rest frame. That assumption makes the antitelephone work, but it is not forced by "controllable FTL" in general.

A defender could argue:

- Preferred-frame FTL avoids this loop. Liberati/Sonego/Visser explicitly discuss tachyon propagation that only moves forward in one distinguished frame; their Fig. 3 discussion says the antitelephone no longer yields `E2` before `E0`. This is directly aimed at the assumption in `audit_premises_README.md:29` and the code assumption in `audit_script.py:59-61`.
- Effective-medium or effective-metric FTL is not reciprocal in arbitrary inertial frames. The audit excludes "constrained effective-medium effects such as Scharnhorst propagation" only in the script's final prose (`audit_script.py:182-183`), but that exclusion is precisely the loophole that prevents overgeneralizing the result.
- GR FTL proposals are not local tachyon beams in Minkowski space. Olum-style and warp-drive/wormhole arguments are about global causal structure and energy conditions, not about a fixed-speed `alpha` signal in 1+1D flat spacetime. If the live claim is updated on the basis of this audit, the update should be limited to the reciprocal flat-spacetime signalling subclaim.
- Tachyon mechanics / reinterpretation-principle literature disputes whether the naive causal chain can be implemented with real tachyonic quanta. I am not saying that literature wins; I am saying the audit does not engage it, so it should not claim more than "this unrestricted signalling rule makes loops."

## Audit assumptions worth challenging

- The central assumption is stated in `audit_premises_README.md:29`: same FTL speed in each sender's rest frame. In code this enters as the reply equation `x_reply = x1p - alpha (t' - t1p)` in `audit_script.py:83-85`. That is the assumption that turns spacelike signalling into a causal loop. A mechanism with a fixed speed in one frame, or anisotropic velocity addition, is outside the audit.
- "Reciprocal, unrestricted" is doing load-bearing work. The audit needs arbitrary direction, arbitrary timing, immediate reply at reception, and operation from a platform moving at any `beta` above threshold. Those are engineering/physical capabilities, not consequences of Lorentz kinematics.
- The relative boost is "allowed" kinematically, but may not be allowed by the FTL propagation medium or device. `audit_premises_README.md:89` says "some allowed inertial boost always closes the loop"; this should be "some Lorentz-allowed boost closes the loop if the FTL rule remains reciprocal in that boosted sender frame."
- The audit is 1+1D and flat. That is appropriate for the antitelephone subclaim, but not enough for the full claim's asymptotic-inertial-observer and positive-energy-matter clauses (`claim_statement_only.md:9`).
- The numerical grid in `audit_script.py:168-175` scans the already-derived analytic formula. It is a sanity check, not independent numerical evidence.
- The sandbox stripping is imperfect: `audit_script.py:178-183` contains conclusion-bearing text under "VERDICT INPUT". This did not change my physics verdict, but it weakens the claimed blind-review isolation.

## Overreach: prose vs math

- `audit_premises_README.md:83-89` goes from the sign of `t2'` to "some allowed inertial boost always closes the loop." The math supports this only for events on A's worldline with the assumed reciprocal FTL law. The README should explicitly state the transform-back step `t2 = t2'/gamma` and keep the conclusion conditional on the propagation law.
- `audit_script.py:1-3` says "unrestricted reciprocal faster-than-light signalling in special relativity permits a causal loop." That is basically correct, but "in special relativity" can read broader than the modeled rule. Better: "the modeled reciprocal sender-rest-frame rule plus Lorentz transformations permits a causal loop."
- `audit_premises_README.md:57` says a civilization with `2c` signals "would need inertial platforms at `0.9c`" in the worked example. The threshold is `0.8`; `0.9c` is just a convenient point above it. This is minor, but the wording should not make the chosen example sound necessary.
- `audit_premises_README.md:104` calls the brute-force scan a "convergence scan." It does converge to the threshold, but only because it is evaluating the same closed-form function. The prose should not imply a separate simulation of signal propagation.
- If the audit is intended to feed the broader claim, the prose should avoid implying that one antitelephone model refutes every controlled FTL proposal.

## Citation-fidelity concerns (with which sources you fetched and how)

I fetched the two cited originals from arXiv using `curl -L -A physicsOS-peer-review-devil-advocate/1.0` inside the sandbox, then converted them with `pdftotext -layout`:

- `https://arxiv.org/pdf/gr-qc/0107091` -> `liberati-sonego-visser-0107091.pdf/.txt`
- `https://arxiv.org/pdf/gr-qc/9805003` -> `olum-9805003.pdf/.txt`

I also checked the arXiv metadata pages and DOI metadata via web search/open.

Liberati, Sonego, Visser 2002, [arXiv:gr-qc/0107091](https://arxiv.org/abs/gr-qc/0107091), Annals Phys. 298 (2002) 167-185, [10.1006/aphy.2002.6233](https://doi.org/10.1006/aphy.2002.6233):

- The audit's citation in `audit_premises_README.md:24` is faithful if read narrowly: LSV do warn that causality depends on the propagation law, not merely on "faster than c."
- The same source is a caution against broadening the audit. In the extracted PDF text, LSV say special relativity kinematically accommodates faster-than-c propagation, and in the tachyonic-antitelephone section they state that paradoxes require not just tachyons but the ability, in arbitrary frames, to send tachyons with the needed time orientation. They then discuss preferred-frame / Scharnhorst-type propagation as "benign."
- Therefore LSV supports the audit's assumption-sensitive framing, but would not support a categorical "any FTL signal implies loops" conclusion.

Olum 1998, [arXiv:gr-qc/9805003](https://arxiv.org/abs/gr-qc/9805003), Phys. Rev. Lett. 81 (1998) 3567-3570, [10.1103/PhysRevLett.81.3567](https://doi.org/10.1103/PhysRevLett.81.3567):

- The audit's citation in `audit_premises_README.md:25` is mostly faithful: Olum proves WEC violation for superluminal travel under his definition and assuming the generic condition.
- Important caveat from the original: Olum explicitly says the theorem does not mean superluminal travel is impossible, because quantum fields violate the WEC; he gives the Casimir effect as an example satisfying his condition. That does not rescue ordinary positive-energy matter, but it matters for scope.
- Olum is not load-bearing for the flat-spacetime antitelephone threshold. It is relevant to the broader claim's "ordinary positive-energy matter" clause, not to the symbolic derivation in `audit_premises_README.md:59-89`.

## Missing literature

- Richard C. Tolman, *The Theory of the Relativity of Motion* (1917), p. 54. LSV cite this as the original antitelephone/Tolman paradox source. Since the audit is exactly a Tolman-style antitelephone, this should be cited directly.
- G. A. Benford, D. L. Book, and W. A. Newcomb, "The Tachyonic Antitelephone," Phys. Rev. D 2, 263-265 (1970), [10.1103/PhysRevD.2.263](https://doi.org/10.1103/PhysRevD.2.263). This is the canonical named source for the device.
- O. M. P. Bilaniuk, V. K. Deshpande, and E. C. G. Sudarshan, "`Meta` Relativity," Am. J. Phys. 30, 718 (1962), plus Bilaniuk and Sudarshan, "Causality and Space-like Signals," Nature 223, 386-387 (1969), [10.1038/223386b0](https://doi.org/10.1038/223386b0). These are important for the reinterpretation-principle defense.
- Gerald Feinberg, "Possibility of Faster-Than-Light Particles," Phys. Rev. 159, 1089 (1967), [10.1103/PhysRev.159.1089](https://doi.org/10.1103/PhysRev.159.1089). Relevant background on tachyonic particles versus signals.
- Erasmo Recami, "The Tolman `Antitelephone` Paradox: Its Solution by Tachyon Mechanics," [arXiv:hep-th/9508164](https://arxiv.org/abs/hep-th/9508164), and later Recami/Fontana/Garavaglia discussion [arXiv:0709.2453](https://arxiv.org/abs/0709.2453). This is the strongest direct opposition literature, even if one ultimately rejects it.
- For broad claim updates: Morris, Thorne, and Yurtsever 1988 on wormholes/time machines; Hawking 1992 and Kay-Radzikowski-Wald 1997 on chronology protection; Bobrick and Martire 2021 [arXiv:2102.06824](https://arxiv.org/abs/2102.06824), Lentz 2022 [arXiv:2201.00652](https://arxiv.org/abs/2201.00652), and Santiago, Schuster, Visser 2022 [arXiv:2105.03079](https://arxiv.org/abs/2105.03079) for the modern warp-drive positive-energy/energy-condition dispute.

## Final verdict (one of: substantive issues / minor issues / agree despite trying not to)

substantive issues

The math is sound for the modeled reciprocal, unrestricted sender-rest-frame FTL rule. The substantive issue is scope: the audit should not be used as a general refutation of controllable FTL unless the claim is first narrowed to exactly that propagation law. LSV, the audit's own main causality source, says the propagation law is decisive and supplies preferred-frame/effective-metric loopholes to the naive antitelephone.
