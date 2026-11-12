# Inventory API release recovery

## Submission details

- Team ID: not provided; complete before submission.
- Team member names: not provided; complete before submission.
- Team repository: https://github.com/harsha-lv/release-rush
- Final commit hash: run `git rev-parse main` after the recovery commit.
- Final release flag: `FLAG{PHASE1_GIT_RECOVERY}`

## Investigation

All three source branches and all six original commits were inspected using
`git branch -avv`, `git log --all --graph --oneline`, `git show`, and `git diff`.

- `main` (`be0fdd8`) includes the newer `service` response key and API version
  `v2`, but lacks health reporting and the production manifest.
- `feature/health-check` (`827200a`) includes health reporting and the three
  supplied tests, but retains the old `name` response key.
- `release/1.0` (`fa1ef8c`) retains the old `name` contract and lacks health
  reporting and tests. Its API version is already `v2`, not an older version.
- `7d6525f2771171125f3e163b4464698f1b67866d` deleted the manifest while also
  updating the application contract. Reverting that entire commit would lose
  the required contract change.
- Later README updates were preserved rather than discarded.

## Recovery

The official remote was renamed to `source`; `origin` points to the team
repository. The original main was pushed there before changes. Nothing was
pushed to the official repository.

The feature was merged into main with `git merge --no-ff --no-commit
feature/health-check`. The expected `app.py` conflict was resolved by retaining
`service` and `version` from main and adding `health` from the feature:

```python
{"service": "inventory-api", "version": "v2", "health": "ok"}
```

The production manifest was recovered without modification using:

```bash
git restore --source=d9a13a38c7381f8bc004fd4f8a824fbf8a1c8f5f -- deploy/production.yml
```

The recovered file and historical file both have Git blob hash
`1ab19ac0da20c25e2475410d3b20129f5da98b85`. The annotation
`releaserush.io/flag` contains the release flag above. The manifest specifies
two replicas, image `inventory-api:2.0`, and container port 8000.

The stale release branch is reconciled by merging the repaired main into it,
preserving both branch histories. No reset, rebase, or force-push is needed.

## Verification

```text
$ python3 -m unittest discover -s tests -v
test_api_version ... ok
test_health_status ... ok
test_service_contract ... ok
Ran 3 tests
OK
```

`git diff --check` also passed. This verifies the challenge's Python contract
and exact manifest recovery, not a live production deployment. No container
build, cluster, or deployment credentials are supplied in this repository.
