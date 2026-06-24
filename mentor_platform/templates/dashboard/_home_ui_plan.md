Home page UI improvement plan

Information gathered
- mentor_platform/templates/dashboard/home.html currently has: a hero header, a 3-card summary grid (assessment, placement, roadmap), and a “Recent assessment results” table section.
- mentor_platform/static/css/main.css already defines a design system (variables, container/header/nav, hero/cards, buttons, tables, badges) but the existing home.html does not fully leverage more polished components/classes.

Plan (code updates)
1) Update mentor_platform/templates/dashboard/home.html to a more modern dashboard layout:
   - Add a top “welcome” card with a subtle gradient and a primary CTA button row (View assessments, Explore projects, Chat with mentor).
   - Replace the simple summary cards with styled “stat cards” using existing CSS patterns (card + stat-like emphasis).
   - Add a secondary section “Next best actions” with 3 action cards.
     - If the context exists (stats/roadmap/recent_results), populate; otherwise show safe fallbacks.
   - Improve the “Recent assessment results” section:
     - Add empty state UI, a compact table header, and show “—” when values missing.
   - Add a “Quick roadmap” section that shows progress with a progress bar (implemented via inline markup/CSS classes).

2) Keep template logic defensive:
   - Use {% if %} checks for optional context variables like roadmap, recent_results, stats.
   - Use default filters where possible.

3) Extend styling only if needed:
   - Prefer using existing CSS classes from main.css.
   - Add minimal new CSS rules at the bottom of main.css if progress bar / dashboard utilities are missing.

Dependent files to edit
- mentor_platform/templates/dashboard/home.html
- mentor_platform/static/css/main.css (only if required for the new UI elements)

Followup steps
- Run server and open the dashboard home page to visually confirm layout, responsiveness, and that template variables render correctly.
- If any context variables are undefined, adjust template fallbacks.

