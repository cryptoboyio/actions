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
  slack-release:
    name: Slack release
    uses: cryptoboyio/actions/.github/workflows/slack-release-alert.yaml@v1
    with:
      APP_NAME: "my-app"
      IMAGE_TAG: "my-app:latest"
    secrets: inherit
```
