# Slack Release Alert Action

- [Inputs](#inputs)
- [Secrets](#secrets)
- [Example job](#example-job)

## Inputs

| Name                    | Type    | Required | Default value       | Description                      |
| ----------------------- | ------- | -------- | ------------------- | -------------------------------- |
| `APP_NAME`              | String  | true     |                     | App name to trigger release      |
| `DEFAULT_RUNNER`        | String  | false    | `***`               | Default runners                  |
| `IMAGE_TAG`             | String  | false    | `BRANCH-RUN_NUMBER` | Image tag                        |
| `RELEASE_REPO`          | String  | false    | `***`               | Release repo                     |
| `RELEASE_REPO_OWNER`    | Boolean | false    | `***`               | Release repo owner               |
| `RELEASE_REPO_WORKFLOW` | String  | false    | `***`               | Release repo workflow            |
| `RELEASE_SLACK_CHANNEL` | String  | false    | `***`               | Slack channel for sending alerts |
| `TRIGGER_RELEASE`       | Boolean | false    | `false`             | Release flag                     |

## Secrets

| Name                      | Type   | Required | Default value | Description         |
| ------------------------- | ------ | -------- | ------------- | ------------------- |
| `ACCESS_REPOS_TOKEN`      | String | false    | Inherited     | GitHub access token |
| `ACTIONS_SLACK_BOT_TOKEN` | String | false    | Inherited     | Slack bot token     |

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
