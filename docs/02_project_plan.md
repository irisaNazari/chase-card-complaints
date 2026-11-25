## Issue Tree

Which 1–2 card pain points should Dana fund next quarter?
│
├── 1. What do customers complain about most?
│   ├── 1a. Which issues have the most complaints? → count by Issue
│   ├── 1b. What share of all complaints is each? → percent by Issue
│   └── 1c. Which issues get the most money back? → monetary relief rate by Issue
│
├── 2. Is it getting better or worse?
│   ├── 2a. Which issues are rising or falling each year? → count per year by Issue
│   ├── 2b. Is the complaint rate per account rising or falling? → complaints ÷ card accounts (10-K)
│   └── 2c. Is severity rising or falling? → monetary relief rate per year
│
├── 3. How do we compare to peers?
│   ├── 3a. Is Chase's overall rate higher or lower than peers? → complaints by Company ÷ each issuer's card accounts
│   ├── 3b. Is Chase worse than peers in the top issues? → rate per Issue by Company
│   └── 3c. Is Chase's gap with peers growing or shrinking? → yearly rate by Company
│
└── 4. Can Chase fix it?
    ├── 4a. What causes the complaints in the top issues? → AI tags on complaint text (Stage 7)
    └── 4b. What share is within Chase's control? → percent of tagged complaints with a Chase-process cause

## Risks

| Risk | Likely? | Impact | Plan |
|---|---|---|---|
| Peer card account numbers missing or reported differently | High | High | Use card loans outstanding as backup; check if Chase's rank changes between the two |
| CFPB category names changed over time | Medium | High | Check label changes in Stage 3; combine old and new labels before trends |
| Company names differ (e.g., Capital One and Discover separate) | High | Medium | Build a name map; decide and document whether to combine after the merger |
| Complaint text only exists for some complaints | High | Medium | Run Stage 7 on that subset; state the share covered |
| AI tags complaint causes wrongly | Medium | High | Hand-check a random sample of 100; report accuracy |
| Dataset too large to load at once | Low | Medium | Query with DuckDB from disk instead of loading into pandas |