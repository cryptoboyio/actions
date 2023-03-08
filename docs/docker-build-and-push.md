# Docker Build & Push Action

- [Inputs](#inputs)
- [Secrets](#secrets)
- [Example job](#example-job)

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

## Example job

```yaml
jobs:
  slack-release:
    name: Slack release
    uses: cryptoboyio/actions/.github/workflows/slack-release-alert.yaml
    with:
      APP_NAME: "my-app"
      IMAGE_TAG: "my-app:latest"
    secrets: inherit
```

