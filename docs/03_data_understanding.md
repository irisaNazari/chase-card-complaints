# Stage 3: Data Understanding

## Source
- CFPB Consumer Complaint Database, archived exports (21 zip files)
- Covers complaints received December 1, 2011 through August 14, 2026
- Link: https://www.consumerfinance.gov/foia-requests/foia-electronic-reading-room/cfpb-consumer-complaint-database-narratives-archive/
- Downloaded: November 24, 2026

## Surprises
- **2026 data ends August 14.** Year-to-date comparison changed from Jan–Oct to Jan–Jul. (Updated in 01_problem_framing.md.)
- **File size:** one month is about 169 MB unzipped (10 MB zipped). Full 2018–2025 data will be several GB.
- **Only 16 columns in the August 2026 file.** The CFPB database has historically had 18. Missing: `Consumer consent provided?` and `Consumer disputed?`. Need to check older files before combining them in Stage 4.
- **Credit reporting dominates the database.** In the August 2026 file, credit reporting is about 93% of complaints (~620,000 of ~667,000); credit card is about 1% (~8,000). Overall CFPB trends will mostly reflect credit reporting, so all trend analysis must filter to credit card only.
- **Product labels changed over time.** In this file, `Credit card` and `Prepaid card` are separate products. Older files likely use the combined label `Credit card or prepaid card`. Need to check older files and map labels in Stage 4, keeping credit cards only.
- **Many recent complaints are still "In progress."** In the August 2026 file, 35% of card complaints were unresolved when the archive was frozen. Monetary relief rate must use closed complaints only as the denominator (here ~15%, not ~10%), and recent months will be biased. Treat 2026 severity trends with caution.
- **Window changed to 2019–2025 (plus 2026 Jan–Jul).** Dropped 2018 to avoid downloading the 2011–2018 file for four months of data. 2019 still gives a pre-COVID baseline. Trade-off: one less year of history.
- **All archive files share the same 16 columns** (checked oldest and newest used). The two missing fields are absent from the whole archive, so files should combine cleanly. Limit: without `Consumer consent provided?`, can't tell why a complaint has no narrative.
- **Complaint volume grew about 8x per month** from 2018–2021 (~21 MB/month) to August 2026 (~169 MB/month), mostly credit reporting. Confirms card complaints must be analyzed on their own.
- **Old files combine credit and prepaid cards.** 2018–2021 uses `Credit card or prepaid card`; 2026 uses separate `Credit card`. Filtering old files on `Credit card` would silently return zero rows. Fix: in old files, keep only sub-products `General-purpose credit card or charge card` and `Store credit card`. Drop 3 rows with blank sub-product.
- **Credit card definition is stable across files.** Both old and new files use the same two sub-products. Plan: filter all files on `Sub-product IN ('General-purpose credit card or charge card', 'Store credit card')`, which works regardless of product label.
- **Company names are parent-company level.** Chase appears only as `JPMORGAN CHASE & CO.` in 2018–2021 card complaints (7,993). Discover appears separately as `DISCOVER BANK`, so the Capital One merger needs a decision in Stage 6. Raw counts rank Chase #3 behind Citi and Capital One, but that is not a fair comparison until normalized by size.
- **Early look at Chase's top issues (2018–2021):** "Problem with a purchase shown on your statement" is #1 at ~41% of Chase card complaints, early support for H1 (not yet tested fully). #2 is a catch-all, "Other features, terms, or problems" (~13%), which needs text classification in Stage 7.
- **Top issue labels are stable** between 2018–2021 and August 2026 (same 10 issues, same wording). Full check across all files in Stage 4.
- **Possible rise in Chase card complaint volume:** ~220/month in 2018–2021 vs ~620 in August 2026 (top 10 issues only). One month only, not normalized by accounts. Lead for H2, to test in Stage 5.

## Field guide (columns used in this project)

| Column | What it means | How I'll use it | Limits |
|---|---|---|---|
| `Date received` | Date the CFPB received the complaint | All trends (by year, Jan–Jul for 2026) | Date of complaint, not of the problem itself |
| `Product` | Broad product type | Not used for filtering | Label changed: `Credit card or prepaid card` (old) vs `Credit card` (new) |
| `Sub-product` | Specific product | Card filter: `General-purpose credit card or charge card`, `Store credit card` | A few rows blank; dropped |
| `Issue` | Main problem the customer chose | Grouping for top pain points (branch 1, 2) | Customer picks from a list, may pick wrong; includes catch-all "Other features, terms, or problems" |
| `Sub-issue` | More detail under the issue | Drill-down on top issues | Often blank |
| `Consumer complaint narrative` | Customer's own description | AI classification of causes (Stage 7) | Only published with customer consent, so covers a subset; personal info removed |
| `Company` | Company named in the complaint | Chase filter (`JPMORGAN CHASE & CO.`) and peer comparison | Parent-company names; Discover separate from Capital One |
| `Company response to consumer` | How the company closed the complaint | Severity: monetary relief rate (closed complaints only) | Reported by the company itself; "In progress" frozen in the archive |
| `Timely response?` | Whether the company answered on time | Possible extra signal of service quality | True/false only, no detail on delay |
| `Complaint ID` | Unique ID per complaint | Checking for duplicates in Stage 4 | A label, not a number to do math on |

## Columns not used
`Company public response`, `State`, `ZIP code`, `Tags`, `Submitted via`, `Date sent to company`. Not needed for Dana's decision; could revisit for later questions (for example, state-level patterns).
