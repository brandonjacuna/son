# Peer list sources (draft, 2026-09-26)

Companion to `config/peers_draft.csv`. Status: draft for Brandon's approval.

## How this was checked

- Direct page reads (WebFetch and curl) were blocked by the session's network egress policy for every source domain tried: guide.michelin.com, statesman.com, austin.culturemap.com, austin.eater.com, tribeza.com, exploreatx.us, wikipedia.org, texasmonthly.com, resy.com, nytimes.com, foodandwine.com, bonappetit.com, esquire.com, and others.
- Everything below was verified through WebSearch result pages only: titles, URLs, and the search tool's excerpts from those pages. "Verified" means at least one publisher page or two independent outlets agreed on the fact. No Google, Yelp, OpenTable, or Resy search results were scraped, and no ratings or review counts were recorded.
- Addresses come from the restaurant's own site, Michelin, or local press as surfaced in search results. Where only an aggregator surfaced the address, the CSV note says to confirm it.

## Scoring weights

Michelin star 3, Green Star 2, Bib Gourmand 1.5, Michelin Recommended 1, JBF winner 3, JBF finalist 2, JBF semifinalist 1.5, every other list 1. A restaurant counts once per list. Tastemaker nominee and winner count as one appearance.

## Sources used in scoring

| Code | Source | Edition / date | URL | Verified? |
|---|---|---|---|---|
| MS, MG, MB, MR | Michelin Guide Texas | 2025 selection, revealed Oct 28 to 29, 2025 (Houston ceremony). Still current: the 2026 selection is scheduled for Oct 8, 2026, by press release with no ceremony, so it has not been released yet. | https://guide.michelin.com/us/en/texas/restaurants/bib-gourmand ; 2026 date: https://www.keranews.org/arts-culture/2026-08-19/michelin-guide-to-announce-2026-texas-selection-on-oct-8 | Partly. Stars, Green Stars and Recommended taken from the verified seed in BRIEF.md. Full Austin Bib list (16) confirmed through search excerpts of the Michelin and Tribeza pages: Briscuits, Cuantos Tacos, Dai Due, Distant Relatives, Emmer & Rye, Franklin Barbecue, Kemuri Tatsu-ya, KG BBQ, La Santa Barbacha, Mercado Sin Nombre, Micklethwait Craft Meats, Nixta Taqueria, Odd Duck, Parish Barbecue, Ramen del Barrio, Veracruz Fonda & Bar. KVUE reports 51 Austin entries in total; the seed plus Bib list accounts for 49, so up to 2 Recommended names may be missing. |
| JBS | James Beard Awards 2026 | Semifinalists Jan 21 to 22, 2026; finalists Mar 31, 2026; winners Jun 15, 2026 (Chicago) | https://www.kut.org/austin/2026-01-21/barley-swine-mercado-sin-nombre-and-7-more-austin-restaurants-named-james-beard-award-semifinalists ; https://www.kut.org/austin/2026-03-31/austin-tx-no-james-beard-award-finalists-texas ; https://austin.culturemap.com/news/restaurants-bars/james-beard-awards-2026-winners/ | Yes. Austin semifinalists: Best Chef: Texas: Thai Changthong (P Thai's Khao Man Gai & Noodles), Michael Che (Tsuke Edomae), Ali Clem (La Barbecue), Daniela and Rosa Landaverde (La Santa Barbacha), Bob Somsith (Lao'd Bar). National: Barley Swine (Outstanding Hospitality), Mercado Sin Nombre (Outstanding Bakery), Kalimotxo (Outstanding Wine and Other Beverages Program), Celia Pellegrini (Outstanding Professional in Beverage Service; not scored because her restaurant could not be confirmed). No Austin finalists and no Austin winners. Austin chef Tavel Bristol-Joseph was a finalist for Nicosi, which is in San Antonio, so it is not scored. |
| TM | Texas Monthly, Best New Restaurants | 2026 list (published Mar 2026; eligibility Dec 1, 2024 to Oct 31, 2025) | https://www.texasmonthly.com/food/best-new-restaurants-2026/ | Yes. Fish Shop, No. 4, is the only Austin entry. |
| RHL | Resy Hit List, Austin | Spring 2026 and Summer 2026 editions, from the current page | https://blog.resy.com/the-hit-list/austin-restaurants/ ; https://blog.resy.com/the-hit-list/austin-restaurants-spring-2026/ | Partly. Only names that appeared in search excerpts are scored. New in Spring 2026: Boni's Bar Next Door, The Meteor, Musashino Sushi Dokoro, Tzintzuntzan. New in Summer 2026: Anh Em Vietnamese Kitchen, Barley Swine, Eldorado Cafe (plus the East Austin Hotel Pool Pass, which is not a restaurant). Also on the page: Dai Due, VanHorn's, Rocco's, Kiin Di. The full list was not readable. |
| CMT | CultureMap Austin Tastemaker Awards | 2026 (ceremony Apr 9, 2026, Distribution Hall) | https://austin.culturemap.com/news/restaurants-bars/austin-tastemaker-awards-winners-2026/ ; https://austin.culturemap.com/news/restaurants-bars/tastemaker-awards-nominees-2026/ | Partly. Restaurant of the Year nominees (complete): Barley Swine, Fonda San Miguel, Fukumoto, Jeffrey's, La Barbecue, Lao'd Bar, Lenoir, LeRoy and Lewis, Odd Duck (winner), Tsuke Edomae. Chef of the Year nominees (partial): Ben Savage (Kalimotxo), Casey Wall (Le Calamar), Landaverdes (La Santa Barbacha, winners), Joseph Gomez (Sana Sana), Joseph Zoccoli (Casa Bianca), Kareem El-Ghayesh (KG BBQ), Laila Bazahm (Siti). Best New Restaurant (partial, 7 of 16): Moderna Bar & Pizzeria (winner), Le Calamar, Siti, VanHorn's, Fish Shop, Rocco's, Cousin Louie's. Bar of the Year: Parley (winner), 9 other nominees. Best Sandwich: Mum Foods. Rising Star and other categories were not captured. |
| NYT | New York Times Restaurant List (50 best) | 2026 (published Sep 2026) | https://austin.culturemap.com/news/restaurants-bars/nyt-favorite-restaurants-2026-paprika/ | Yes. Paprika (N Lamar) is the only Austin entry. It scores 1 and falls below the cutoff. |
| BA | Bon Appetit Best New Restaurants | 2026 (eligibility Mar 2025 to Mar 2026) | https://austin.culturemap.com/news/restaurants-bars/bon-appetit-best-new-calamar/ | Yes. Le Calamar is the only Austin entry. |

## Sources checked but not scored

| Source | What was found | Why excluded |
|---|---|---|
| Eater Austin Essential 38 | Search excerpts point to a Summer 2026 update, but the page could not be read and no reliable list of current names surfaced. Third-party copies (thevendry.com, luxehomesaustin.com) are undated. | Could not verify the current list or its update date. |
| Austin American-Statesman dining guide (Matthew Odam) | "The 40 best restaurants in Austin", updated Feb 18, 2026 (2025 guide: https://www.statesman.com/project/austin-2025-food-guide-best-restaurants/). The names and ranks were not retrievable. | Could not verify the contents. Older fact, not scored: the 2024 guide had Birdie's, Nixta Taqueria and Tsuke Edomae tied for No. 1. |
| Food & Wine Best New Restaurants 2026 | No Austin entry surfaced. | Could not confirm whether any Austin restaurant is listed. |
| Esquire Best New Restaurants | 2025 list exists (published late 2025). No Austin entry surfaced. The 2026 list was not found and is probably not yet published. | Could not confirm any Austin entry. |
| Resy "10 Restaurants That Defined Austin Dining in 2025" (Dec 2025) | Names include Lenoir, Eldorado Cafe, East End Ballroom, VanHorn's, Paprika, All Day Pizza. | This is not the Hit List and is not in the requested source set. Mentioned in notes only. |

## Closures and relocations found

- Olamaie: closed Jul 19, 2026 (Statesman, KXAN). CSV row status `closed_historical`.
- Maie Day (Michelin Recommended): closed May 2026 with the South Congress Hotel renovation and rebrand (Houston Chronicle, "A count of closed Texas Michelin-recommended restaurants", https://www.chron.com/food/article/michelin-restaurants-texas-closed-22387534.php).
- Pasta|Bar Austin (Michelin Recommended): closed Feb 2026 for a new concept (same Chronicle piece).
- Ramen del Barrio (Bib): moved from the W Parmer Ln truck to a brick-and-mortar at 2007 Kramer Ln in 2026.
- Not on the peer list, but in-market signals: dipdipdip Tatsu-ya closed Aug 2026; Perla's (S Congress) has been closed indefinitely since a Sep 6, 2026 kitchen fire; Bar Peached (W 6th) has been closed since a May 31, 2026 fire; El Naranjo closed in summer 2026.
