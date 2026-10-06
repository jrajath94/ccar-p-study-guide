# PDF Print Spec — CCAR-P v2 (Raj's order, 2026-10-06 ~13:07 EDT)

First-class deliverable, not an afterthought. The print stylesheet is drafted NOW
(v2-build/print.css); every fragment build must already conform to the structural
contract below so the final PDF assembly is mechanical, not a rewrite.

## Typography
- Body: Anthropic Sans → Inter → Source Sans 3 → IBM Plex Sans (first available).
- 10pt body. 14pt bold section headers. 18pt bold domain titles.

## Line spacing
- 1.3–1.4 line-height on body (O'Reilly reference style).

## Margins
- 0.5in top / bottom / left / right. Content width on letter = 7.5in.

## Pagination and flow
- widows: 3; orphans: 3 everywhere.
- Forced page break before each major domain (H1).
- Keep-with-next on ALL headers, figures/diagrams, and KEY TAKEAWAY blocks:
  `break-inside: avoid` + `page-break-after: avoid` on headers.

## Interactive TOC
- Nested, clickable TOC in the digital HTML.
- PDF: entries carry physical page numbers (generated at build time with a
  paged-media renderer — target-counter mechanism; verified against actual pages).
- Page-count sanity check: TOC numbers must match rendered pages.

## Images and diagrams
- Verify RENDERED, sharp, correctly proportioned, not clipped — visual check per
  image-bearing page, not just exit code.
- Check native size first; resize meaningfully before placing; preserve aspect
  ratio; never stretched, squished, or awkwardly tiny/huge.
- Max width 7.5in, scale proportionally. Center every image. 12pt padding above
  and below.
- Code snippets and ASCII diagrams: monospace (IBM Plex Mono → ui-monospace),
  NO text wrapping, structural integrity preserved exactly.

## Verification before shipping
- Render and inspect every image-bearing page.
- TOC page numbers match actual pages.
- Scan for widow/orphan violations and split KEY TAKEAWAY blocks.

## Fragment structural contract (all workers, all stages)
- Domain title: `# D1 — Name` (H1 only; assembler maps to 18pt bold + page break).
- Section header: `## ...` (H2 → 14pt bold). Subsections: `###`.
- KEY TAKEAWAY blocks: fenced div markers
  `:::takeaway` ... `:::` → `<div class="key-takeaway">` (never split across pages).
- Figures: `<figure class="fig">` inline SVG `</figure>` + `<figcaption>Caption.
  Shell N. Source: ...</figcaption>`.
- Code/ASCII: fenced code blocks only; never wrap lines by hand to fit — the
  renderer keeps them intact.
- No raw HTML tables for layout; markdown tables fine (renderer styles them).
- Filenames: no spaces. No file over 90MB.
