# SciOS / IOSP ⇄ SpaceTimeArc Integration Study

*Research report · 21 November 2026 · Christian Willmes / SpaceTimeArc context*

---

## 1. Executive Summary

SciOS (nonprofit, `scios.tech`) and its community arm IOSP (Institute of Open Science Practices, `iosp.science`) are building a **decentralized, researcher-owned infrastructure stack for open science**, organized around the lifecycle *Store → Share → Assess → Fund*. Their tooling — Matadisco, the IOSP Node Network, Lettuce/SciOS Compute, GREP, RRGI, MIRA, Citey, PRSM — is built on AT Protocol and IPFS/content addressing.

**SpaceTimeArc (STA)** is a three-tier System of Systems for spatiotemporal human–environment-interaction data: (1) Data Collection & Publication, (2) Data Storage & Distribution, (3) Client Applications — with cloud-native geospatial (CNG) formats, a CIDOC CRM-based semantic layer, and Matadisco already in the architecture diagram.

**The core finding: STA and SciOS/IOSP are converging on the same substrate from two directions.** STA brings the domain content (4D landscape datasets, geo data models, paleo/historical temporal semantics); SciOS/IOSP brings generic publishing, preservation, discovery, attribution, and distributed-compute infrastructure. The projects already share one critical person: **Volker Mische (@vmx)** is both STA team member and the author of Matadisco (IPFS Foundation). The integration is therefore not a stretch — it is mostly a matter of systematically adopting and feeding back into tools that are one degree of separation away.

Highest-value integration points:

| # | SciOS/IOSP asset | STA tier | Why |
|---|---|---|---|
| 1 | **Matadisco** | Tier 2 (discovery) | Already planned; solves the "share/manage COG/CNG URLs" problem flagged in the 26-11-20 meeting |
| 2 | **IOSP Node Network + RO-Crate + On-Demand Pinning** | Tier 2 (storage) | Replaces single-copy HiDrive hosting of the 11.7 GB DataR-D outputs with protocol-distributed, researcher-owned redundancy |
| 3 | **Lettuce / SciOS Compute** | Tier 1 (data production) | STA's heavy ELT notebooks (10–38 GB downloads each) become volunteer-run distributed computations |
| 4 | **GREP extraction pipeline** | Tier 1 (data sourcing) | A "geo-GREP" campaign extracting dataset mentions from Quaternary/paleoenvironmental literature — automated literature review |
| 5 | **MIRA schema** | Tier 1 (data model) | STA's standardized data model and publication framework expressed as a geospatial domain extension of the emerging shared research-record schema |
| 6 | **RRGI** | Tier 1 (publication) | STA dataset layers published as granular, PID-ed, attributed contributions to the shared scientific record — machine-actionable data citation |
| 7 | **Citey** | Tier 1 (citation) | CITATION.cff/codemeta.json for STA tools; candidate extension toward *data* citation for CNG layers |
| 8 | **Community/events** | All | ATScience x IOSP CFP closes **30 Nov 2026** — 9 days from now |

---

## 2. The Partners at a Glance

### 2.1 SciOS — `scios.tech`

A 501(c)(3) nonprofit (directors Ellie DeSota, Jonathan Starr; advisor Chris Erdmann) building "infrastructure for open science." Current tool portfolio (as of Nov 2026):

- **RRGI** (Resilient Research Graph Infrastructure) — publishing pipeline that decomposes papers into granular contributions (questions, claims, evidence, methods), each with a persistent identifier, links, and author credit. ATProto-based. Live event graph: `graph-event.rrgi.scios.tech`.
- **IOSP Assessment App** — reads the research graph and scores questions/protocols/researchers with *open, published algorithms* (funders' goals → ranking).
- **Lettuce Compute** — open-source (AGPL-3.0) mass-scale distributed volunteer computing; anyone can deploy a server and define computations; volunteers contribute CPU/GPU via CLI, desktop app, or browser tab.
- **SciOS Compute** (`compute.scios.tech`) — SciOS's hosted Lettuce instance.
- **GREP** (Great Research Extraction Project) — local-first AI reading papers into structured records; first campaign extracted 5,665 software mentions from 1,356 open-access papers using a three-model consensus protocol run on volunteer machines.
- **IOSP Node Network** (`iosp.science/datanetwork`) — researcher-owned Raspberry Pi/laptop network mirroring a shared dataset list; indexer packages each dataset as an **RO-Crate** with keywords; human + machine search APIs.
- **Citey** (`citey.scios.tech`) — one-click software citation in Chrome; catalog of 152 packages; generators for CITATION.cff and codemeta.json.
- **PRSM** (`prsm.network`) — knowledge graph of publications, software, people, institutions, and dependencies (incl. binary symbol analysis of packages).
- Publications: *The Minimum Viable Scientific Record*, *The Core-Satellite Model*, *Resilient Data Futures* (`rdf.scios.tech`, itself published as an RRGI graph).
- Teaching: **PICoding** — 4-week course on building AI-agent workflows around researchers' own data.

### 2.2 IOSP — `iosp.science`

The Institute of Open Science Practices: an event, a community, and a coordinating institute. IOSP 2025 (Denver, 80 people) and **IOSP 2026 (Leiden, Oct 12–15, ~45 participants, hosted with the GO FAIR Foundation)**. IOSP 2026's working principle: *the people who depend on open science infrastructure and the people building it should be in the same room.* Notable Leiden outcomes:

- 44 participants created **DIDs on AT Protocol**; all workshop contributions (check-ins, records, algorithms) became signed, attributed records in a shared graph.
- A working **data network** of 11 laptops + 7 Raspberry Pis preserving at-risk datasets; four weeks later every dataset was still fully held.
- 159 participants' papers run through the RRGI extraction pipeline → 17,681 attributed contributions, 30,187 links; 4,161 contributions published directly during the workshop via three tools all writing the **MIRA** schema.
- Assessment workshop: groups wrote open funding-allocation algorithms over the graph.
- Community day: convergence of >20 modular-science projects (OXA, MIRA, Octopus, nanopublications, Semble…) on shared definitions; MIRA + Bycelium interop via "small shared core + extensions + connector."
- Tooling showcase: Matadisco (Robin Berjon, IPFS Foundation), On-Demand Pinning for IPFS kubo (Cornelius Ihle, Göttingen), Aster (ATProto data hosting for researchers), Sifa ID, Semble, dmactrac, software-metadata-sync-tool, Repo MetAudits, Octopus, Scroll Press, Liberata, LaborTrail, ATScience hacking stations.
- **Next events:** ATScience x IOSP conference (Netherlands, **April 29–30, 2027**, CFP open until 30 Nov 2026), claim extraction & modular publishing workshop (online, 26 Jan 2027), research assessment workshop (16 Feb 2027), IOSP 2027 (in person, Fall 2027).

The IOSP "theory of change" explicitly names the digital-native substrate with primitives STA also pursues: *content addressing, distributed hosting, append-only provenance, object graphs, open algorithms*. The "technological group's if-then statement" — *if each field can easily define its own schemas, then more people will write their knowledge in a structured form* — is precisely the gap STA's domain data model would fill for geosciences.

### 2.3 SpaceTimeArc — needs assessment (from local repos + talks)

From `/home/christian/git/SpaceTimeArc/` (Systemarchitecture, DataR-D) and the Geomob CGN (28 Oct 2026) & CHNT31 Vienna (11 Nov 2026) presentations:

- **Vision:** geobrowser with timeslider; underlying product = *integrated 4D landscapes* as data infrastructure for human–environment-interaction modelling ("integrative geography").
- **Tier 1 — Data Collection & Publication:** data models (space-time, environmental, human/cultural), CNG formats (vector/raster/mesh; SpaceTimeCubes via Zarr/GeoZarr/Icechunk under discussion), a formal data-publication framework (peer review, citation, data journals). DataR-D already contains 11 reproducible notebooks covering 200 Ma → 2100 (COG/GeoParquet outputs, `data_index.csv`, ISO 8601 expanded years, conda lock files), with notebook-specific licence provenance. A Quaternary paleoenvironments literature review is under way. The Netherlands Paleogeography & Archaeology dataset (`rce.webgis.nl`) is the pilot example dataset.
- **Tier 2 — Storage & Distribution:** S3 & IPFS storage ("anyone can host their own"), Matadisco (developed mainly by @vmx), LOD/SemanticWeb (geo-lod ontology anchored in CIDOC CRM/CRMsci/CRMarchaeo/CRMgeo, PeriodO, Wikidata; reproducible ELT in Jupyter; SPARQL endpoints) — mainly @fthiery.
- **Tier 3 — Applications:** WebApp, QGIS plugin (dataset compilation + metadata publishing focus), API.
- **Open problems (meeting notes):** storage/sharing/management of COG/CNG URLs (26-11-20); HiDrive single-copy hosting of ~11.7 GB outputs; heavy raw-download requirements (notebook 11 ≈ 38.5 GB, 09 ≈ 33 GB, 10 ≈ 10 GB); reproducible publication pipeline for 4D-landscape compilations in data journals.

---

## 3. Integration Analysis by STA Tier

### 3.1 Tier 2 — Data Storage & Distribution (nearest-term wins)

**Matadisco — the native discovery layer (already yours).**
Matadisco separates data discovery from storage: lightweight, signed ATProto records (`cx.vmx.matadisco` lexicon: `resource` URI + `publishedAt` + optional preview + up to 20 tags) pointing at *any* metadata standard (STAC, DataCite, IIIF, RSS…). Producers watch catalogues and publish; consumers build portals in ~100 lines of code. Existing implementations to reuse directly:

- `sentinel-to-atproto` (producer pattern for STAC catalogues) — STA's `data_index.csv` + HiDrive/S3 URLs map 1:1 onto this pattern; a `sta-to-atproto` producer publishing one Matadisco record per CNG file/layer is a small, concrete build.
- `matadisco-geo-viewer` (consumer, STAC-aware, renders spatial previews on a map) — a ready-made STA community portal; STAC metadata for STA layers would light up map previews with zero new code.
- `gdi-de-csw-to-atproto` (CSW → ATProto) — pattern for harvesting existing geodata catalogues (GDI-DE, INSPIRE) into the STA discovery space.
- `niiifty` (IIIF manifests + IPFS storage + AI semantic search) — relevant for cultural-heritage imagery layers of the Human Layer.

This directly answers the 26-11-20 meeting item *"we need to find a solution to store/share/manage COG/CNG URLs."* Recommendation: model STA dataset metadata as **STAC** (with a temporal extension carrying the ISO-8601 expanded years / `age_ma` from `data_index.csv`), publish via a Matadisco producer under the STA namespace, and consume through `matadisco-geo-viewer`. Because Volker Mische leads both, STA is arguably the * flagship geospatial reference adopter* Matadisco needs — a mutual benefit: Matadisco gets a real geoscience deployment; STA gets decentralized discovery for free.

**IOSP Node Network + RO-Crate — protocol-distributed preservation.**
The network mirrors an agreed dataset list on researcher-owned Raspberry Pis/laptops, with an indexer (built on Cornelius Ihle's `cid-indexer-ipfs`, Gipp Lab Göttingen) that packages each dataset as an **RO-Crate** ("one folder that holds the data together with a description of it"), assigns keywords, and exposes human (`iosp.science/datanetwork`) and machine (`/api/datanetwork/search`) search. The *Resilient Data Futures* whitepaper argues for exactly the architecture STA's "anyone can host their own S3 or IPFS" note gestures at: tier-4 preservation — distribution across a protocol no single organization operates, where each joining machine adds another copy.

Integration path for STA:
1. Package DataR-D outputs (per layer/time step, or per notebook section) as RO-Crates — the RO-Crate metadata can be generated from `data_index.csv` and the notebook-level source/licence tables, extended with geospatial context (bbox, CRS, temporal coverage). RO-Crate is the natural packaging for STA's "data publication" tier as well (see §3.2).
2. Propose the STA 4D-landscape corpus for the shared dataset list, or — better — start a **spacetimearc-nodes consortium** on the IOSP Node Network model (the network already hosts multiple groups: `iosp-nodes`, `iosp-laptops`). The Leiden proof (every dataset still held in full after 4 weeks, across machines participants took home) demonstrates the resilience STA needs for its "scientific peer-reviewed 4D model of the Earth."
3. Combine with **On-Demand Pinning** (kubo PR #11252, Cornelius Ihle): IPFS nodes that pin data *on demand* when a client requests it — the right model for large COGs that shouldn't be fully mirrored everywhere: anchor CIDs in Matadisco/RO-Crate records, fetch on demand from the network.

**Aster / Sifa ID — identity for the STA data space.**
Every published Matadisco record is signed by a DID. A project-level STA identity (or per-institution identities for data contributors in India/Cologne partnerships) gives dataset provenance at the account level; Aster (`aster.id`) offers not-for-profit ATProto data hosting with verified identities — an alternative to running a PDS in-house. This also future-proofs attribution when STA datasets become RRGI contributions (§3.2).

### 3.2 Tier 1 — Data Collection & Publication (the scientific-record integration)

**RRGI — 4D landscapes as granular contributions to the shared scientific record.**
RRGI publishes each question, claim, piece of evidence, and method as its own contribution with a PID, links, and per-author credit. STA's publication framework wants: peer-reviewed 4D-landscape compilations in data journals, all layers linked to their sources, and *exportable bibliographies for each spatiotemporal configuration*. These are the same requirement stated in two vocabularies:

- An STA **layer** (e.g., "temperature at 21 ka from CHELSA-TraCE21k, notebook 02") = an RRGI *evidence/method* contribution with its own PID, linked to the source publication (DataCite DOI), licence, producing notebook (reproducibility), and authors.
- An STA **4DLandscape compilation** (e.g., "Netherlands Paleogeography & Archaeology dataset") = an RRGI *study* whose evidence graph is the layer configuration; "export bibliography for this configuration" becomes a graph traversal.
- Future scenario layers (CHELSA CMIP6, SSP paths) can carry *claims* that are open to challenge — matching MIRA's evidence model where "a piece of evidence must be open to challenge in two places: the data and the statement that describes the data."

Concretely: STA could run its planned 4D-landscape data-journal manuscripts *also* through the RRGI pipeline (as IOSP did with participants' papers) so each dataset's granular records enter the shared graph, are citable at layer granularity, and are attributable to the students/researchers who compiled them (Shruti, Yogiraj, Abhijith — **micro-attribution of data-compilation work is RRGI's core value proposition** and solves STA's credit problem for dataset compilers).

**MIRA — the schema alignment to watch (and shape).**
MIRA (Modular Interoperable Research Attribution, `mira.science`) is the emerging shared schema for research records (Question, Claim, Evidence, Study, Protocol, Request; relations: addresses, supports, opposes, grounds, follows…). Tools already writing MIRA: Discourse Graphs, Semble, eLife Pathways, OXA, SciOS Graph. The Akamatsu-lab dataset on the node network shows the pattern: *a lab's discourse graph serialized against the MIRA schema, packaged as RO-Crate with a schema snapshot for offline reading.*

STA relevance: STA is developing "a common standardized data model for spatio-temporal environmental and human data." Rather than inventing a publication-layer schema alone, STA can position its model as the **geospatial/4D-geo domain extension of MIRA** — following the interop pattern agreed at Leiden (small shared core + domain extensions + connectors). Space-time context, layer, 4DLandscape, human-layer entities would become MIRA-adjacent record types. The MIRA kickoff (Dublin, June 2026, co-organized by SciOS and Discourse Graphs) tested exactly this process: six prototypes from three user stories against one draft schema. **Recommendation: engage with the MIRA community early (blog, kickoff follow-ups, the 26 Jan 2027 modular-science workshop) to ensure geo/temporal record types are in the core-or-extension discussion — STA is probably the most demanding temporal-semantics use case they have encountered (200 Ma → 2100, PeriodO-aligned, expanded ISO 8601 years).**

**GREP — automated literature review for the data basis.**
GREP's three-model consensus pipeline (run on volunteer compute via Lettuce) extracted 5,665 software mentions from 1,356 papers. STA's current bottleneck is precisely large-scale literature triage: the Quaternary Paleoenvironments literature review, the India spatiotemporal datasets survey, and the `data_sources_link.md` compilation. A **"geo-GREP" campaign** — extracting *dataset* mentions (repository + DOI/PANGAEA IDs, proxy types, spatial bounding boxes, geochronological periods) from Quaternary/paleo/archaeological literature — would:

- automate the population of the STA data-source index and the literature review's evidence tables;
- produce structured candidate lists for 4DLandscape compilations (which sources exist for which time-slice/region);
- run on the same Lettuce infrastructure, as a SciOS Compute campaign (GREP's second campaign pattern — a domain campaign is a natural evolution, and STA would be a flagship *geoscience* use case, currently under-represented: Environmental science had only 367 mentions/210 papers in GREP's corpus vs. biology's 2,364/270).

This is a joint-development opportunity to propose to SciOS: GREP's extraction schemas extended with spatiotemporal fields (bbox, time interval, period names mapped to PeriodO).

**Citey + software-metadata-sync-tool — citation hygiene today.**
Immediate, low-cost adoptions:
- Use Citey's generators to write **CITATION.cff and codemeta.json** for STA repos (DataR-D, Systemarchitecture, future tools), and register them in the Citey catalog (152 packages today). The Helmholtz `software-metadata-sync-tool` can keep CodeMeta/CITATION.cff/DataCite in sync in CI — directly useful for the STA GitHub org.
- **Extension opportunity matching STA's data-citation need:** Citey today cites *software*; STA needs one-click citation of *data layers* (BibTeX/DataCite per layer or per 4DLandscape configuration — the "exportable bibliography" requirement). Proposing a data-citation mode to Citey (or building the STA equivalent for CNG/STAC metadata) is a well-scoped contribution back to the ecosystem.

**PICoding — agent workflows for the ELT pipeline.**
STA's notebooks are already reproducible ELT jobs (download → convert to COG/GeoParquet → metadata). PICoding's curriculum (AI-agent workflows around researchers' own data) is directly applicable: metadata extraction agents, QA agents for CNG outputs, literature-triage agents. The ATScience hacking stations show the pattern of streaming data as ATProto records and building agents that preserve learning as durable facts — an interesting template for STA's "API" tier and for future agent-based clients that "time-travel" through the data via tools.

### 3.3 Tier 3 — Applications (clients)

- **Matadisco consumers as STA portals** (see §3.1): `matadisco-geo-viewer` (map-based, STAC) ≈ a minimal STA discovery app; ~100 lines of code per portal.
- **Semble** (`semble.so`, ATProto social knowledge network, MCP plugin for agents): curation "trails" of STA datasets — e.g., a trail "Europe during LGM" as a shareable collection; agents can consume via MCP.
- **ATScience hacking stations / Aster**: patterns for streaming STA data updates as ATProto records (new time-slice published → record → subscribers' clients update), and verified researcher identities for dataset authors.
- **QGIS plugin:** no direct IOSP counterpart, but the plugin's focus (dataset compilation + metadata publishing) maps onto producing RO-Crates/Matadisco records/MIRA records — the plugin could become the *geo* authoring tool for the shared record (the role Octopus/Discourse Graphs play in life sciences).
- **Assessment App pattern → STA coverage-gap ranking:** the IOSP Assessment App ranks contributions by funder goals. The same idea applied internally: an **open algorithm ranking candidate dataset compilations by space-time coverage gaps** (which 5-Myr steps, regions, variables are missing?) — STA's roadmap as a computable policy. Demonstrable with the existing `data_index.csv`.

### 3.4 Cross-cutting — positioning, funding, community

- **Core-Satellite Model:** STA as a *satellite* in a geoscience *core* (or seed of a "4D-geo data" core). The model's Domain Knowledge Map is exactly where a curated index of CNG tooling (STA's compilation of formats, Zarr/Icechunk decisions, etc.) would live.
- **PRSM:** once STA tools exist as packages, PRSM maps their adoption/dependencies — useful for funder reporting on the project's software ecosystem.
- **Resilient Data Futures + Minimum Viable Scientific Record:** framing documents for STA grant proposals — STA is a domain instantiation of the MVSR (funders pay for the shared record; STA delivers the geo/temporal slice) and of tier-4 data resilience.
- **Events (ordered by urgency):**
  1. **ATScience x IOSP CFP — closes 30 Nov 2026** (`atmosphereconf.org/science`). Perfect fit: STA's Matadisco/IPFS/ATProto story + a working geo deployment. A talk/demo of "STA 4D landscapes on the decentralized science stack" is the natural submission.
  2. Modular-science / claim-extraction workshop, online, **26 Jan 2027** — schema discussion (MIRA geo extension, RRGI for datasets).
  3. Research assessment workshop, online, **16 Feb 2027**.
  4. **ATScience x IOSP conference, Netherlands, 29–30 Apr 2027.**
  5. Engage! prize (closes 15 Jan 2027) — possible recognition avenue for STA open tooling.
  6. IOSP 2027 (Fall, in person) — target for a hands-on "4D-geo build session" à la the Leiden data-network workshop.
  7. FOSSGIS 2027 (Heidelberg, March) — STA already plans a submission; cross-link both communities there.

**Human network short paths:** Volker Mische (STA + Matadisco/IPFS Foundation — direct); Robin Berjon (Matadisco, IPFS Foundation); Cornelius Ihle (Gipp Lab Göttingen — cid-indexer, On-Demand Pinning; geoscience-adjacent lab, likely receptive to geo use cases); Matthew Akamatsu (Discourse Graphs/MIRA); Jonathan Starr & Ellie DeSota (SciOS); GO FAIR Foundation (Erik Schultes — co-host of IOSP 2026; FAIR alignment for the geo-lod/PeriodO work). The Leiden gathering already hosted the Netherlands Paleogeography context (IOSP 2026 was in Leiden; the Erfgoedatlas/RCE dataset STA chose as pilot is Dutch cultural-heritage data — a nice conversation opener with GO FAIR and Dutch partners).

---

## 4. Recommended Roadmap

### Quick wins (≤ 1 month)
1. **Submit ATScience x IOSP abstract** (deadline 30 Nov 2026) — demo: 4D landscape datasets + Matadisco discovery.
2. Generate **CITATION.cff / codemeta.json** for STA repos via Citey generators; add software-metadata-sync-tool to CI.
3. Prototype a **Matadisco producer** for DataR-D: STAC metadata (with temporal extension incl. expanded ISO-8601 years) → `cx.vmx.matadisco` records pointing at HiDrive URLs; render in `matadisco-geo-viewer`. (Coordinate with @vmx.)
4. Package one dataset (e.g., CHELSA-TraCE21k LGM layers, or the Netherlands pilot) as an **RO-Crate** from `data_index.csv` metadata.

### Medium term (1–6 months)
5. Join/launch the **node consortium** on the IOSP Node Network; mirror the 11.7 GB DataR-D corpus; evaluate On-Demand Pinning for large COGs; document the "S3 + IPFS dual-publishing" pattern.
6. Design the **MIRA geo extension / RRGI dataset-contribution profile** in dialogue with SciOS (use the 26 Jan 2027 workshop); publish 2–3 STA layers as granular contributions to test attribution and layer-level citation.
7. Scope the **geo-GREP campaign** with SciOS: extraction schema for spatiotemporal dataset mentions; pilot on the Quaternary literature review corpus.
8. Replace/augment HiDrive with **dual publication** (institutional S3 + IPFS pinning + Matadisco record) as the standard STA publication path for data-journal submissions (the data journals listed — ESSD, JOSS-adjacent data journals, Open Archaeology Data — accept links to repositories; a protocol-distributed copy strengthens preservation statements).

### Strategic (6–18 months)
9. **Lettuce computation** for STA ELT: package notebook pipelines as Lettuce server computations ("rebuild any 4D-landscape layer from sources at scale"); volunteers/students contribute compute; each output content-addressed and registered via Matadisco/RRGI.
10. **QGIS plugin as geo authoring tool** for the shared record (RO-Crate/Matadisco/MIRA output), positioning STA in the modular-science tool landscape next to Octopus/Discourse Graphs.
11. **Open coverage-gap algorithm** (Assessment-App pattern) over `data_index.csv` + graph — publish it as an open algorithm to steer (and justify funding for) compilation priorities.
12. Position STA in a **Core-Satellite structure** for the geo domain; contribute the Domain Knowledge Map for 4D/CNG tooling.

---

## 5. Risks & Caveats

- **Maturity:** Matadisco is explicitly "experimental — things may break or change"; RRGI/MIRA are early-stage; ATProto Lexicons can evolve. Mitigation: keep canonical metadata in stable standards (STAC, DataCite, RO-Crate, CIDOC CRM) and treat ATProto records as the discovery/attribution transport layer, not the archive.
- **Licences:** STA's most restrictive source licence (CC BY-NC-SA 4.0 for notebook 09; LR04 CC BY-NC-SA 3.0) constrains redistribution on public node networks — mirror only cleared subsets, or negotiate/replace NC-licensed layers (an RO-Crate records licence per file, which helps).
- **Dataset size vs. volunteer network:** the node network is proven on ~100–300 MB datasets; 11.7 GB is feasible (7,252 files · 293 MB-scale is routine, but pinning budgets should be planned; On-Demand Pinning mitigates).
- **Community focus:** SciOS/IOSP center on life sciences and scholarly-communication infrastructure; geoscience is under-represented. This is a risk (less ready-made geo tooling) and the opportunity (STA becomes the flagship geo use case that shapes the schemas).
- **Sustainability:** SciOS is a young nonprofit; diversify — the good news is every core component (Matadisco, Lettuce, cid-indexer) is open source and self-hostable, matching STA's "anyone can host their own" principle.

---

## 6. Sources

- SciOS: https://www.scios.tech/ (tool portfolio, events, publications)
- IOSP: https://www.iosp.science/ (Leiden 2026 programme, showcase, theory of change)
- IOSP 2026 outputs: https://www.iosp.science/leiden2026outputs
- IOSP Node Network: https://www.iosp.science/datanetwork
- Matadisco: https://matadisco.org (schema, producers/consumers, GitHub `ipfs-fdn/matadisco`)
- MIRA: https://mira.science (schema, integrations, kickoff report)
- GREP first-run report: https://compute.scios.tech/projects/grep/first-run
- Lettuce Compute: https://github.com/jring-o/lettuce-compute · https://compute.scios.tech
- RRGI event graph: https://graph-event.rrgi.scios.tech/
- Resilient Data Futures: https://rdf.scios.tech
- ATScience x IOSP: https://atmosphereconf.org/science
- SpaceTimeArc local repos: `/home/christian/git/SpaceTimeArc/Systemarchitecture/README.md`, `/home/christian/git/SpaceTimeArc/DataR-D/` (README, datamodel.md, meeting notes 26-10-08 … 26-11-20)
- Presentations: https://cwillmes.de/presentations/20261028_GeomobCGN/ (Geomob CGN, 28 Oct 2026) · https://cwillmes.de/presentations/20261111_CHNT/ (CHNT31 Vienna, 11 Nov 2026)
- GitHub org: https://github.com/SpaceTimeArc/
