# Design Review Workflow Setup – For Erik

This document explains how to set up fully automated design reviews that post directly to Jira.

---

## What Changed

**Before:** Claude generates report + images. You drag images into Jira manually. (15 min + 2 min manual)

**Now:** Claude generates report + images + posts everything to Jira automatically. (15 min, zero manual steps)

---

## Setup (5 minutes)

### Step 1: Install Atlassian MCP (Claude.ai)

1. Go to **claude.ai**
2. Click **Settings** → **Connectors** (or click the puzzle icon)
3. Search for **"Atlassian MCP"**
4. Click **Install**
5. Authenticate with your Alligo Jira account (OAuth — you never type your password)
6. Verify it says **"Connected"**

### Step 2: Create `.env` file (Project root)

1. In your `swedol-ui-prototype` folder, create a new file called `.env`
2. Add these two lines:

```
JIRA_INSTANCE=alligo.atlassian.net
JIRA_API_TOKEN=<your_token_here>
```

3. **To get your Jira API token:**
   - Go to https://id.atlassian.com/manage-profile/security/api-tokens
   - Click **Create API token**
   - Name it "Claude Design Review"
   - Copy the token
   - Paste it into `.env` as shown above

4. **Add to `.gitignore`** (so you never commit the token):
   ```
   .env
   ```

5. Save the file.

### Step 3: Enable Atlassian MCP in this chat

When you ask Claude to run the design-review skill:

1. Claude will check if Atlassian MCP is available
2. If you see **"Atlassian MCP not enabled"**, click **Connector settings** in the message
3. Toggle on **Atlassian MCP**
4. Run the skill again

---

## How to Use

### For each design review:

**1. Prepare the Jira ticket** (30 seconds)
   - Add Figma frame links (one per breakpoint) in the ticket description
   - Make sure the UAT URL is noted
   - Example:
     ```
     **Figma frames:**
     - Desktop (1440px): https://figma.com/...?node-id=916-134656
     - Tablet (768px): https://figma.com/...?node-id=4182-31410
     - Mobile (375px): https://figma.com/...?node-id=1123-112949
     
     **UAT:** https://uat.swedol.se/company/users2
     ```

**2. Ask Claude to run the skill** (15–20 minutes)
   ```
   Run design-review skill on AE-3512
   ```

**3. Wait** — Claude will:
   - Read your ticket
   - Test the UAT implementation
   - Compare against Figma + ECO Design System
   - Generate findings
   - Create comparison images
   - Post everything to Jira automatically

**4. Done** — Developers see the complete report + images in the Jira comment.

---

## What Gets Posted to Jira

The comment includes:

- **Report text** — All findings organized by severity:
  - 🔴 Critical (WCAG, design system breaks)
  - 🟠 Should fix (noticeable deviations)
  - 🟢 Nice-to-have (polish)
  - ❓ To confirm (intentional differences)
  - 📐 Figma file issues (for design team)

- **4 comparison images** — Figma vs. UAT side-by-side with marked deviations:
  - Desktop view
  - Row actions/hover states
  - Sorting behavior
  - Tablet/mobile layout

- **Everything in one comment** — No back-and-forth, no manual dragging.

---

## Troubleshooting

| Problem | Solution |
|---|---|
| **"Atlassian MCP not available"** | Go to claude.ai → Connectors → Install Atlassian MCP |
| **"JIRA_API_TOKEN not found"** | Create `.env` file in project root with your token |
| **"401 Unauthorized when uploading"** | Check token at https://id.atlassian.com/manage-profile/security/api-tokens — may have expired |
| **"Images didn't upload but report posted"** | Claude will include images as file attachments; you can drag them manually if needed |
| **"Claude in Chrome not working"** | Install the extension at chrome.google.com/webstore, sign in, and make sure you're logged into the UAT site |

---

## Questions?

If something isn't working:
1. Check the Setup checklist below
2. Verify Atlassian MCP is installed and connected
3. Verify `.env` file exists with token
4. Try running the skill again

If Claude shows an error, share it and we'll fix it.

---

## Setup Checklist

Before your first design review, verify:

- [ ] Atlassian MCP installed from claude.ai → Connectors
- [ ] Atlassian MCP shows "Connected"
- [ ] `.env` file exists in project root
- [ ] `.env` contains `JIRA_INSTANCE` and `JIRA_API_TOKEN`
- [ ] `.env` is in `.gitignore`
- [ ] Claude in Chrome extension installed (for testing UAT)
- [ ] You're logged into https://uat.swedol.se in Chrome
- [ ] You're logged into https://alligo.atlassian.net in Claude's browser

✅ All checked? You're ready to go.

---

## Example: Running AE-3512

**You say:**
```
Run design-review skill on AE-3512
```

**Claude does:**
1. Reads AE-3512 ticket → finds Figma frames + UAT URL
2. Opens UAT in Claude in Chrome
3. Tests at 375, 640, 768, 769, 1024, 1440px
4. Extracts CSS values using getComputedStyle
5. Compares to Figma designs + ECO tokens
6. Finds 6 Critical, 7 Should-fix, 3 Nice-to-have items
7. Creates 4 annotated comparison images
8. Posts complete report + images to Jira ticket
9. Reports: "✅ Review posted to AE-3512"

**Developers see:** Full findings + visual proof in one Jira comment

**Your time:** 0 minutes (fully automated)

---

**Generated:** 2026-09-30  
**Workflow:** Fully automated design reviews with Jira posting
