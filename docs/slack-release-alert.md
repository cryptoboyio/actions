# Slack Release Alert Action

- [Inputs](#inputs)
- [Secrets](#secrets)
- [Examples](#examples)
  - [Minimum use case](#minimum-use-case)
  - [Slack and release use case](#slack-and-release-use-case)

## Inputs

| Name                  | Type    | Required | Default value       | Description                  |
| --------------------- | ------- | -------- | ------------------- | ---------------------------- |
| `BUILD_ARGS`          | List    | false    | `null`              | Build args                   |
| `BUILD_RUNNERS`       | String  | false    | `***`               | Comma-separated runners list |
| `CONTEXT`             | String  | false    | `.`                 | Docker context               |
| `DEFAULT_RUNNER`      | String  | false    | `***`               | Default runners              |
| `DOCKERFILE`          | String  | false    | `Dockerfile`        | Dockerfile                   |
| `IMAGE_TAG`           | String  | false    | `BRANCH-RUN_NUMBER` | Image tag                    |
| `IMAGE_TAG_LATEST`    | String  | false    | `BRANCH-latest`     | Image tag latest             |
| `PUSH_IMAGE`          | Boolean | false    | `true`              | Push image to registry       |
| `REGISTRY`            | String  | false    | `***`               | Docker registry              |
| `REPOSITORY`          | String  | false    | `GITHUB-REPOSITORY` | Repository in the registry   |
| `TRIGGER_RELEASE`     | Boolean | false    | `false`             | Release flag                 |
| `TRIGGER_SLACK_ALERT` | Boolean | false    | `false`             | Slack alert flag             |

If `IMAGE_TAG` or `IMAGE_TAG_LATEST` contains a `/` character, then the default values ​​will be as follows:

| Name               | Value              |
| ------------------ | ------------------ |
| `IMAGE_TAG`        | `build-RUN_NUMBER` |
| `IMAGE_TAG_LATEST` | `build-latest`     |

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
