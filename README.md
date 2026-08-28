# A Decision Intelligence Framework for Enterprise Transformation Programs

**Sovereign context reasoning, APQC-spined traceability, and adoption-first sequencing in the SAP program context.**

*EVEglyphDesign — practitioner author · v1.0 — invited peer review draft · 2026*

## Read the paper

- **Public surface:** <https://eveglyphdesign.github.io/decision-intelligence-framework/>
- **Controlled PDF (8 pages, SHA-256 stamped):** [`docs/EVEglyphDesign_Decision_Intelligence_Framework.pdf`](docs/EVEglyphDesign_Decision_Intelligence_Framework.pdf)

## Abstract

Decision intelligence is now defined as a superset discipline in which business intelligence is one optional input, yet enterprise transformation programs continue to treat it either as a synonym for analytics or as an unbounded aspiration. This paper proposes a practitioner framework for embedding decision intelligence inside the SAP program context along three load-bearing choices: an AI context-reasoning surface hosted wholly inside the client's DMZ and operated as a durable enterprise capital asset; a program-wide numbering spine anchored on the APQC Process Classification Framework (v7.4) that threads blueprint, technical design, technical object, test plan, dataset, and role and authorisation records through the SAP Activate phase model; and an adoption-first sequencing that moves learning and role design forward in the plan on the evidence that people, not technology, are now the binding constraint on transformation outcomes.

The framework is positioned as additive to the existing SAP toolchain (Cloud ALM, Signavio, Solution Manager, Joule) and to the emerging TM Forum DT4DI stack (IG1307, IG1310, IG1310A, IG1310B, IG1310C), and it makes an explicit break with the systems-integrator-owned platform pattern by naming the sovereign context-reasoning repository as a client-held residual. The paper closes with an invitation to peer review, an evidence register, and a list of open questions the author does not yet have the data to close.

## Peer-review invitation

Ten specific claims in the paper are ahead of the peer-reviewed literature. Each is named in §8. Load-bearing claims for reviewers:

1. The client-DMZ sovereignty claim.
2. The APQC-spine traceability claim (novel structural use with no published precedent).
3. The adoption-first sequencing claim.
4. The human-authorised decision artifact as the control boundary.

Open an [issue](https://github.com/EVEglyphDesign/decision-intelligence-framework/issues) to comment on any claim, propose an evidence correction, or submit a section-level critique. Suggested peer-review venues are listed in Appendix A of the PDF (MISQE, HICSS, IEEE Software, CACM Practice, JEIM, TM Forum, ISACA Journal, JDS, IDT).

## Repository layout

```
paper/
├── build/
│   ├── build_paper.py       Two-pass PDF builder (canon)
│   └── paper_content.py     Paper content (isolated from layout)
├── docs/
│   ├── EVEglyphDesign_Decision_Intelligence_Framework.pdf
│   └── index.html           Public Pages surface
├── research/
│   └── literature_pass.md   96-source peer-review literature pass (evidence register)
└── README.md
```

## Reproduce the build

The PDF is built by a two-pass ReportLab pipeline (page count discovered on pass one, stamped on pass two, with the final SHA-256 stamped alongside an ISO-8601 UTC timestamp). Fonts: Fraunces (display), Inter (body).

```bash
python3 build/build_paper.py
```

## Canon compliance

Built to EgD-BOOT-001. Cream (`#fdfaf4`) and orange (`#e87722`) palette, Fraunces + Inter, EVEglyph watermark, KEY_ID `EgD-KEY-2026-07`, SHA-256 stamp, ISO-8601 UTC timestamp, closing mark *Pour le bien-être du peuple*. Every citation is a clickable Markdown link to the fetched primary source.

---

© 2026 EVEglyphDesign. Controlled copy.
*Pour le bien-être du peuple.*
