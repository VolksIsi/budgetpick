# AGENT.md - BudgetPick Master Context

## 🎯 Project Overview
**Name:** BudgetPick
**Description:** A fully static, fast-loading, mobile-friendly Amazon affiliate website focusing on budget audio equipment (specifically microphones under $50).
**Live URL:** [https://volksisi.github.io/budgetpick/](https://volksisi.github.io/budgetpick/)
**Repository:** [https://github.com/VolksIsi/budgetpick](https://github.com/VolksIsi/budgetpick)
**Amazon Associate ID:** `budgetpick21-20`

## 📁 Project Structure
The site is built entirely with vanilla HTML5 and CSS3. There are no build steps, no Node.js scripts required to run it, and no external framework dependencies.
*   `index.html`: The homepage featuring the grid of all products.
*   `styles.css`: Global stylesheet containing the design system (CSS variables, glassmorphism, responsive grid).
*   `[product-id].html`: 20 individual product review pages (e.g., `fifine-k669b.html`).
*   `blog.html`: The blog index.
*   `[blog-slug].html`: 5 SEO-optimized blog articles regarding audio setups.
*   `about.html` & `contact.html`: Standard static pages.
*   `sitemap.xml` & `robots.txt`: Essential SEO routing files.
*   `build_site.py` / `update_links.py` / `build_seo_site.py`: The temporary python generator scripts used to originally bootstrap and mass-update the files.

## 📜 Agent Guidelines & Rules
When assisting with this repository, **you MUST follow these rules:**

1.  **Architecture:** Do NOT introduce external dependencies (e.g., Tailwind CSS via CDN, Bootstrap, React, Vue, jQuery). Stick to vanilla HTML and CSS.
2.  **Design Language:** The site must maintain a clean, highly readable, and functional aesthetic inspired by professional review publications like The Wirecutter. Use a light theme (white/light gray background), high-contrast dark text (`#1f2937`), standard system fonts, clear solid buttons without gradients, and an absolute minimum of unnecessary animations. Do NOT use "Glassmorphism" or dark mode glows.
3.  **Monetization:** Any new product links MUST use the Associate ID: `budgetpick21-20` and the format `https://www.amazon.com/dp/[ASIN]/?tag=budgetpick21-20`. Links should have `rel="nofollow noopener sponsored"`.
4.  **SEO:** Every new page must include a `<title>`, meta `description`, `<link rel="canonical">`, and proper H1/H2 hierarchy. All pages must cross-link to relevant internal pages to pass link juice.
5.  *CRITICAL RULE - Link Validation:* **At the start of ANY new session/task where you are modifying content, you MUST automatically verify all Amazon affiliate links on the site.** Ensure every link points to a valid ASIN and uses the correct `budgetpick21-20` associate ID. If broken links are found, correct them automatically, deploy the fixes, and document the results in the changelog.
6.  *CRITICAL RULE - Status Updates:* **After completing any meaningful change, feature addition, or task on this project, you must automatically update the "Changelog & Status" section of this `AGENT.md` file before finishing your session.**
7.  *CRITICAL RULE - Live Link Verification:* **After ANY change to an affiliate link, the live URL MUST be opened directly and the button click physically verified (using a browser subagent/bot). Checking the code alone is insufficient. A task is only considered complete once this live physical verification confirms the correct destination.**

---

## 🕒 Changelog & Status
*Maintain a chronological record of changes here.*

*   **[2026-02-24]** Initial Bootstrap: Created the foundational HTML/CSS structure, 20 unique product reviews, basic standard pages, sitemap, and robots.txt.
*   **[2026-02-24]** Deployment: Initialized Git and successfully deployed the site to GitHub Pages automatically via tokens.
*   **[2026-02-24]** Link Integration: Scraped real Amazon ASINs for all 20 microphones (finding functional counterparts for generic ones) and injected the specific `budgetpick21-20` associate ID into all buy buttons.
*   **[2026-02-24]** SEO & Expansion: Regenerated the entire site to optimize Meta Titles, Meta Descriptions, and Canonical Tags. Implemented a dynamic "Related Microphones" section on product pages. Added a new 5-article interconnected Blog section.
*   **[2026-02-24]** Context established: Created this `AGENT.md` file to maintain project directives, rules, and history. 
*   **[2026-02-24]** Safety Rule Added: Implemented a new critical rule for automatic link verification (`budgetpick21-20`) at the start of all future agent sessions.
*   **[2026-02-24]** Link Validation: Automatically verified all 20 Amazon affiliate links across the site at the start of the session. All links are correctly formatted and use the `budgetpick21-20` associate ID.
*   **[2026-02-24]** Link Correction: Fixed the affiliate link for the Fifine K669B USB Microphone, updating the ASIN from the incorrect `B0DK8BMW2B` (Door Handle) to the correct `B06XCKGLTP`.
*   **[2026-02-24]** Safety Rule Added: Added a new critical rule requiring physical live-link verification (via browser click) after every link change. 
*   **[2026-02-24]** Organic Redesign: Overhauled the design to feature "Organic Glassmorphism". Implemented the Caveat handwritten font, random asymmetrical transforms for product cards, and ran a Python script to rewrite 20 product descriptions into an authentic, first-person review tone. **(Current Status: Active and Live)**
