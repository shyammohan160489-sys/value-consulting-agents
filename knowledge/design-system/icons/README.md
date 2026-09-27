# Icons for the Apex engine

Two stroke-icon families, both on a 24 × 24 grid with stroke width 2 and round caps, drawn by the engine as native
vector shapes (`X.icon_glyph(s, "phone-incoming", x, y, size, colour)`): crisp, recolourable, editable in PowerPoint and
Google Slides, no image files.

| Family | Folder | Icons | Licence | Fetched |
|---|---|---|---|---|
| Lucide | `lucide/` | 2,118 | ISC (`lucide/LICENSE`) | 25 Sep 2026, `lucide-static` 1.48.0 |
| Tabler | `tabler/` | 5,166 outline | MIT (`tabler/LICENSE`) | 27 Sep 2026, `@tabler/icons` 3.48.0 |

One namespace. A bare name (`users`) resolves to Lucide first, then Tabler; 652 names exist in both, so `tabler:users` or
`lucide:users` pins a family. `X.icon_search("bank")` searches both `tags.json` files and returns Tabler-only hits as
`tabler:name`, ready to paste. 6,632 distinct names across 7,284 files.

Tabler's filled variants (1,054 icons) are not installed: they are filled paths, and the engine strokes outlines.

The twelve PNG icons in `.claude/skills/exhibit-slides-pptx/assets/icons/` predate both sets (lifted from a Claude
Design export) and stay for the stat blocks that already use them.
