# Force Push Action

- [Inputs](#inputs)
- [Example job](#example-job)

## Inputs

| Name             | Type   | Required | Default value | Description     |
| ---------------- | ------ | -------- | ------------- | --------------- |
| `DEFAULT_RUNNER` | String | false    | `***`         | Default runners |

## Example job

```yaml
jobs:
  force-push:
    name: Force push
    uses: cryptoboyio/actions/.github/workflows/force-push.yaml@v1
    secrets: inherit
```
