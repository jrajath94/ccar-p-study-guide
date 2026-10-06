# Completion Validation Gate — CCAR-P v2 (Raj's order, 2026-10-06 ~14:06 EDT)

Runs AFTER Stage 9. Nothing ships until all four gates pass. Results written to
BUILD-LOG.md as the final section.

## Gate 1 — Presence validation

Build the explicit checklist from the prompt. Mark each PRESENT or MISSING.
No MISSING may remain.

- Crash course HTML: all 7 domains, prerequisite diagnostic, §7.x foundations.
- All §18 comparisons with 3+ minimal pairs each (26 pairs).
- All §21 implementation artifacts.
- 3 capstones + 9 labs.
- Question bank: 25 substantive questions per domain (175), 50 mixed-domain,
  4 full-length mocks matching the verified format, counterfactual drills.
- Error ledger. Readiness dashboard. October 6 currentness appendix.
- Final review sheets. Source registry. Blueprint coverage ledger.
- Print-spec PDF (built per v2-build/pdf-print-spec.md). Zip.

## Gate 2 — Figure validation

- Every lesson plate and chapter plate passes the visual_system_generic.md page
  audit: no blank figure cells, every architecture/change unit has before+after,
  all numbers computed.
- Every AI-generated image verified on-topic and clean; regenerations logged.

## Gate 3 — PDF validation (Raj's print spec)

- Anthropic Sans 10/14/18pt type scale; 1.3–1.4 line height; 0.5in margins.
- Widow/orphan control; page breaks before domains; keep-with-next on headers,
  figures, KEY TAKEAWAY blocks.
- Nested clickable TOC with verified physical page numbers (TOC numbers match
  rendered pages).
- Every image aspect-ratio-checked and rendering properly; monospace no-wrap
  code blocks.
- Visually inspect every page carrying an image.

## Gate 4 — Repo validation

- After the final push to jrajath94/ccar-p-study-guide: verify remote matches
  local — every file present, no drift, README and BUILD-LOG current, zip and
  PDF downloadable and intact.
- Report any missing remote files and re-push before calling it done.
