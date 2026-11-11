# RELEASE RUSH
## Phase 1 — Source Control & Repository Investigation

**Total Marks: 20**

### PRODUCTION INCIDENT

The Inventory API production release has been blocked.

The development team reports that:

- Multiple branches contain different application changes.
- A health-check feature is waiting to be merged.
- The production deployment manifest is missing.
- The release branch may contain outdated code.

Your team has been assigned to investigate and restore the repository.

### OBJECTIVES

Investigate the repository, identify the version-control problems, restore the required application changes and recover the missing production configuration.

### YOUR TASKS

1. Investigate all available branches and commit history.
2. Identify inconsistencies between the branches.
3. Integrate the required health-check functionality into the main application.
4. Resolve any merge conflicts while preserving existing functionality.
5. Recover the missing production deployment manifest using the available Git history.
6. Run the supplied automated tests.
7. Verify that the restored repository is ready for release.

---

### PARTICIPANT SETUP

**Step 1 — Clone the official repository**

Official repository:

https://github.com/sammjoshuaa07-ui/ReleaseRush-Phase-1-Git

```bash
git clone https://github.com/sammjoshuaa07-ui/ReleaseRush-Phase-1-Git.git
cd ReleaseRush-Phase-1-Git
```

**Step 2 — Create your team's repository**

The team leader must create a new, empty GitHub repository under their own account.

Suggested name:

`RR-TEAM-ID-Phase-1-Git`

Do not initialize it with a README, Gitignore or license.

**Step 3 — Configure the remotes**

Rename the official repository remote:

```bash
git remote rename origin source
```

Add your own repository:

```bash
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Verify:

```bash
git remote -v
```

- `source` must point to the official event repository.
- `origin` must point to your team's repository.

**Step 4 — Push the original challenge into your repository**

```bash
git push -u origin main
```

You will now work independently in your team's repository.

---

### SUBMISSION REQUIREMENTS

Submit:

1. Team ID and member names.
2. Your team's GitHub repository URL.
3. Summary of the identified repository problems.
4. Explanation of the changes made.
5. Evidence of the recovered production manifest.
6. Automated test results.
7. Final commit hash.
8. Final release flag.

### RULES

- Teams of 2–3 members.
- Internet search is permitted.
- Discussion only within your own team.
- Do not use destructive Git operations to bypass the challenge.
- Preserve the existing application functionality.
- Do not share answers with other teams.
- Do not push to the official event repository or the `source` remote.
- All solutions must be committed and pushed to your own repository.

**Good luck!**
