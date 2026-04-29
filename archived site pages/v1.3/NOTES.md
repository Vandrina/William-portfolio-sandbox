# William McGuire Portfolio — Project Notes

Last updated: 2026

---

## Active Todo

### Images
- [ ] Choose hero slideshow images (3 total) — William to select
- [ ] Choose one representative image per discipline card (6 cards)
- [ ] Choose one representative image per client card (10 cards on homepage)
- [ ] Generate thumbnails (run `generate_thumbnails.sh`) and push to GitHub
- [ ] Update portfolio.html to use thumbnails in grid, full images in lightbox only
- [ ] Upload animation/video files when ready — add to manifest

### Code & Features
- [ ] Fix AND/OR filter logic bug — switching logic does not affect currently filtered results
- [ ] Build 404.html router for clean slug URLs (`/microsoft` → `portfolio.html?client=microsoft`)
- [ ] Add lazy loading to gallery grid images
- [ ] Test URL parameter deep linking end to end once thumbnails are in place

### Pages Still To Build
- [ ] About page
- [ ] Contact page (decide on system: form service, email link, or both)
- [ ] Custom 404 error page with site navigation intact
- [ ] Shop landing page or "coming soon" — decision pending on whether to remove shop links before go-live or build a placeholder

### Design Decisions Pending (William to decide)
- [ ] Filter UI: keep both active button highlights AND active tag row, or choose one?
  - Option A: buttons only — keep View All + OR/AND in right column
  - Option B: active tag row only — relocate OR/AND, remove View All
- [ ] Shop links: keep visible (links to williammcguire.shop) or hide until shop is live?
- [ ] Client cards on homepage: show all clients or curated selection only?

### Infrastructure
- [ ] Set up custom domain (williammcguire.net) on GitHub Pages
- [ ] Decide on host migration from Porkbun (Cloudways or similar — better I/O, no inode limits)
- [ ] WordPress site on Porkbun: keep as staging, migrate, or deprecate?

---

## Completed
- [x] Repo created and deployed to GitHub Pages (vandrina.github.io/William-portfolio)
- [x] 344 images organized into discipline folders and pushed
- [x] manifest.json generated and client/discipline tags added
- [x] portfolio.html built with filter bar, masonry gallery, lightbox
- [x] index.html built with hero slideshow, discipline grid, client grid
- [x] style.css shared stylesheet created
- [x] Mobile filter collapse working correctly
- [x] URL parameters update on filter click (?view= and ?client=)
- [x] Removed dev notes from index (see below)

---

## Known Bugs
- AND/OR toggle button works visually but does not affect filtered output
- Homepage discipline/client card links currently load full unfiltered gallery (thumbnail + lazy load fix will resolve load issue; URL param already correct)

---

## Design System Reference
- Gold: `#c8a46e` / Gold dim: `#6e5830` / Gold light: `#d4b580`
- Background: `#1c1c1e` / BG2: `#222224` / BG3: `#282828`
- Surface: `#242426` / Border: `#2e2e32` / Border mid: `#3a3a3e`
- Muted: `#52525a` / Mid: `#7a7a84` / Text: `#d0d0d8` / Bright: `#eeeef2`
- Fonts: Outfit (headings) · Inter (body) · Space Mono (mono/labels)

---

Dev Notes — Homepage
Hero Images
Three slides need real images chosen. Uncomment the <img> tags inside each .hero-slide div and replace placeholder filenames. William to choose one standout piece per slide. Hero auto-advances every 5 seconds.
Discipline & Client Card Images
Each card has a commented-out <img> tag. William to choose one representative image per discipline and per client. Replace CHOOSE_ONE.jpg with the actual filename. Cards link directly to pre-filtered portfolio views.
Still To Do
404.html router for clean slug URLs (/microsoft → portfolio filtered). About and Contact pages. Nordstrom, Nickelodeon, Stone Arch Books, Tech Smart Kids client cards not shown here — add if William wants them visible on homepage. Animation disciplines hidden until video files are uploaded.

---

## Client Slugs (use these exactly in manifest.json)
microsoft · amazon · big-fish · elevated-games · reflective-games ·
dreambox-learning · leapfrog · paramount · handmade-by-robots ·
mystery-society · nordstrom · nickelodeon · stone-arch-books ·
tech-smart-kids · agency · personal (exclude from filter UI)

## Discipline Slugs
illustration · concept-art · toy-design · backgrounds · books · nft ·
2d-animation · 3d-animation (last two pending video upload)

## Further Questions
- process for changing image names
  