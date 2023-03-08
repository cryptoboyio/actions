# Slack Release Alert Action

- [Inputs](#inputs)
- [Secrets](#secrets)
- [Examples](#examples)
  - [Minimum use case](#minimum-use-case)
  - [Slack and release use case](#slack-and-release-use-case)

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

## Examples

### Minimum use case

```yaml
name: Build docker image on PR

on:
  workflow_dispatch:
  pull_request:
    branches:
      - "master"
      - "develop"
      - "release[0-9]+"
      - "release[0-9]+-[0-9]+"

jobs:
  build-and-push:
    name: Build PR-${{ github.event.number }}
    uses: cryptoboyio/actions/.github/workflows/docker-build-and-push.yaml@v1
    with:
      PUSH_IMAGE: false
    secrets: inherit
```

### Slack and release use case

```yaml
name: Build and push docker image on PUSH

on:
  workflow_dispatch:
  push:
    branches:
      - "master"
      - "develop"
      - "release[0-9]+"
      - "release[0-9]+-[0-9]+"

jobs:
  build-and-push:
    name: Build ${{ github.ref_name }}-${{ github.run_number }}
    uses: cryptoboyio/actions/.github/workflows/docker-build-and-push.yaml@docker-build-and-push-action
    with:
      TRIGGER_RELEASE: true
      TRIGGER_SLACK_ALERT: true
    secrets: inherit
```

