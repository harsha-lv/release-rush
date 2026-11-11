# RELEASE RUSH
## Phase 1 - Source Control & Repository Investigation

Total Marks: 20

## PRODUCTION INCIDENT

The inventory API production release has been blocked.

The development team reports that:

1. Multiple branches contain different application changes.
2. A health-check feature is waiting to be merged.
3. The production deployment manifest is missing.
4. The release branch may contain outdated code.

Your team has been assigned to investigate and restore the repository.

## YOUR TASKS

1. Investigate Git branches and commit history.
2. Identify the outdated release branch.
3. Merge the health-check feature into main.
4. Resolve the resulting merge conflict.
5. Preserve the existing API contract.
6. Recover the deleted deployment manifest.
7. Run the automated tests.
8. Submit the recovered release flag.

## STEP 1 - INVESTIGATE

git status
git branch -a
git log --graph --oneline --decorate --all

## STEP 2 - CREATE LOCAL FEATURE BRANCH

git switch --track origin/feature/health-check

## STEP 3 - MERGE FEATURE INTO MAIN

git switch main
git merge feature/health-check

A merge conflict is expected in app.py.

Resolve it without losing the existing service contract
or the new health-check functionality.

## STEP 4 - RECOVER THE DELETED FILE

git log --all --oneline -- deploy/production.yml

Identify the original commit.

Recover the file using:

git restore --source=COMMIT_HASH -- deploy/production.yml

Replace COMMIT_HASH with the correct commit hash.

## STEP 5 - RUN AUTOMATED TESTS

python -m unittest discover -s tests -v

All three tests should pass after the correct resolution.

## SUBMISSION REQUIREMENTS

Submit:

1. Identified repository issues.
2. Relevant branch names.
3. Explanation of the merge conflict.
4. Commands used to resolve the conflict.
5. Original commit hash containing the manifest.
6. Test execution results.
7. Recovered release flag.

## RULES

- Teams of 2â€“3 participants.
- Internet search is permitted.
- Discussion only within your own team.
- Do not use git reset --hard.
- Do not force-push.
- Preserve application functionality.
- Do not share answers with other teams.

Good luck!
