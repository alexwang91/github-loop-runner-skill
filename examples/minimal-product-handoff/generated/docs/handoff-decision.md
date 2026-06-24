# Handoff Decision

```yaml
handoff:
  status: pending
  chosen_mode: null
  decided_at: null
  decided_by: null
  prompt_generated: false
  bootstrap_pr: null
  first_todo_milestone: M0
```

## Modes

- `current_agent_development`: this agent enters the loop workflow.
- `external_agent_development`: another agent receives the complete runner prompt.
