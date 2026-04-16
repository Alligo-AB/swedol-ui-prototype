# swedol-ui-prototype

UI prototype project using Claude Code, GitHub Desktop, and Vercel for collaboration and deployment.

## Workflow

### 1. Development (Claude Code)

* Use Claude Code to generate/update UI code
* Work locally in this repo

### 2. Version Control (GitHub Desktop)

* Create a new branch for your work (e.g. `feature/header-update`)
* Commit and push changes using GitHub Desktop

### 3. Preview Deployments (Vercel)

* Every pushed branch gets a **preview deployment**
* Preview links require login (internal use only)

### 4. Staging (`test/acceptance`)

* Merge approved work into `test/acceptance`
* This branch deploys to a **public staging URL**
* Used for external review/testing

### 5. Production (`main`)

* Merge from `test/acceptance` → `main`
* `main` is deployed as **production**

---

## Local preview

Open `index.html` directly in a browser, or run a local server:

```bash
python3 -m http.server 8080
```

Then visit:
http://localhost:8080

---

## Branch Strategy

* `feature/*` → development branches (protected previews)
* `test/acceptance` → staging (public)
* `main` → production

---

## Notes

* Do not commit directly to `main`
* Always use branches + pull requests
* Use `test/acceptance` for final verification before production
