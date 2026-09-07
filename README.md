# CoOS Specs

The public spec catalog for [CoOS](https://www.pirol.ai) — the free,
open-source, AI-first company stack for small service businesses.

Every folder describes one **extension**: what it does, which tables and views it needs, and which
standard processes it ships. The briefs are plain text on purpose — they are written for two
readers at once:

1. **You.** Browse the catalog (here, or inside CoOS under *Marketplace*), pick a brief, and
   let the built-in Extend agent build it into your own CoOS — on your data, under your roles,
   in one database with everything else.
2. **The agent.** A brief is a complete work order: the Extend agent must be able to reach a
   working extension from the text alone. That makes every spec in this repo a living benchmark of
   what CoOS can build for you.

Briefs are written in English (founder ruling 2026-09-08); the earlier German entries are being
migrated. Repository tooling and this README are English.

## Layout

```
<extension-id>/
  <extension-id>.spec   the brief: what to build, in prose
  process.md            the standard processes this extension ships (become runnable SOPs)
bundles/
  <bundle-id>.md        curated sets of extensions for one industry / use case
```

Curated, verified model solutions are maintained separately and delivered through the Pirol
endpoint inside the app. Anything here you can also hand to the agent yourself.

## Contributing

Open a PR with a new folder. Keep briefs self-contained: purpose, the data you track (tables +
fields in prose), the views you expect, and the processes it should ship. If the Extend agent
cannot build it from your text, the brief — not the agent — gets fixed first.
