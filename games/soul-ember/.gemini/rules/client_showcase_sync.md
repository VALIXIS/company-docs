# Client Showcase Auto-Sync Rule

## Context & Requirement
The private client showcase directory at `http://valixis.tech/showcase/` (hosted in the `VALIXIS/company-docs` repository under `/showcase`) is the private sales and client demonstration portal used by the founder (Subhash Annam) and co-founder.

Whenever ANY client demo website is created, edited, updated, or enhanced (such as Roastery Coffee House, Subko Coffee, Blue Tokai, Novel Hotel, or any new restaurant, cafe, or business client demo):

1. **Deploy Demo Assets:**
   - Commit and push the client demo files to `VALIXIS/company-docs/showcase/<client-slug>/index.html`.

2. **Update Showcase Hub (`showcase/index.html`):**
   - Add/update the client demo tab in the interactive live preview selector (`<button class="site-tab" ...>`).
   - Add/update the client entry in the `sites` JavaScript mapping dictionary with its `url`, brand `glow` color, and personalized outreach pitch.
   - Ensure the "Open Standalone in New Tab" button points directly to `<client-slug>/index.html`.
   - Update the client card with its direct link and features in the grid.

3. **Verify Deployment & Privacy:**
   - Push updates to `VALIXIS/company-docs:main` via the GitHub API.
   - Verify that `http://valixis.tech/showcase/` loads the updated client demo.
   - Strict privacy constraint: NEVER add public navigation links to `/showcase/` on the main corporate homepage (`index.html`). The showcase remains accessible only via direct private link for the founder and co-founder.
