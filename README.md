# GitHub Actions

See [docs folder](https://github.com/cryptoboyio/actions/tree/master/docs) for more details.

## Example release

For example, if the current version is `v1.23.5` and we want to increment only the patch version, we need to do the following:

```bash
git tag -d v1
git push --delete origin v1

git tag v1
git tag v1.23.6
git push --tags
```

But if we want to increment the major version, we need to do the following:

```bash
git tag v2
git tag v2.0.0
git push --tags
```
