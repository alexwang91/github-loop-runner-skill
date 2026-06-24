# Long-Run Planning Addendum

Append this addendum to the external-agent runner prompt when the generated repository uses Long-Run Growth Mode.

## Additional File

Read `docs/long-run-growth-loop.md` before selecting the next milestone.

## Additional State Report

Report these values before editing:

- merged PR count,
- TODO backlog count,
- growth review due,
- deep review due,
- backlog below configured floor,
- final review eligibility.

## Planning Rules

- Apply the long-run policy before selecting work.
- When TODO backlog is below the configured floor, run growth review and append specific verifiable milestones.
- When the initial backlog is exhausted before the minimum PR budget, run deep review and plan expansion.
- Growth review compares current repo state with the initial product goal.
- Deep review checks product surface, correctness, verification, operability, architecture, security/governance, documentation, and harness quality.
- Final review eligibility requires the configured minimum PR budget and repeated empty deep reviews.

## Default Targets

| Setting | Default |
| --- | ---: |
| target merged PRs | 50 |
| minimum merged PRs before final review | 40 |
| growth review interval | 5 PRs |
| deep review interval | 10 PRs |
| minimum TODO backlog | 12 |
| preferred TODO backlog | 20 |
| expansion batch size | 8-15 milestones |
| empty deep reviews before final review | 3 |

## Expansion Rules

New milestones must include category, impact, reason from review, acceptance criteria, verification path, expected changed files or areas, and one-PR fit.

Do not add vague cleanup, polish, placeholder, or churn-only work.
