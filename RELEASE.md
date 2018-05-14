# Release Workflow
Before submitting a new release, make sure all relevant pull requests and local branches have been merged to the `master`
branch. All tests must pass before a release is tagged.


## Testing
Make sure tests pass before starting with a release. See [TESTING.md](TESTING.md) for more information.

## 1. AUTHORS
Update the [AUTHORS](AUTHORS) and [.mailmap](.mailmap) file

``` bash
git checkout master
git log --use-mailmap | grep ^Author: | cut -f2- -d' ' | sort | uniq > AUTHORS
git commit -am "Update AUTHORS"
```

## 2. Changelog
Install [github-changelog-generator](https://github.com/skywinder/github-changelog-generator)
```bash
gem install github_changelog_generator
```

Generate [CHANGELOG.md](CHANGELOG.md)
```bash
github_changelog_generator -t <github-access-token> --future-release=v1.0.0
```

## 3. Git Tag
Commit all changes to the `master` branch

``` bash
git commit -v -a -m "Release version <VERSION>"
git push
```

Tag the release

``` bash
git tag -m "Version <VERSION>" v<VERSION>
```

Push tags

``` bash
git push --tags
```

## Ansible Galaxy
The role is uploaded automatically to [Ansible Galaxy](https://galaxy.ansible.com/).