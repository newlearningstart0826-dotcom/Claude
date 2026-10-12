# newlearning-plugins

A Claude Code plugin marketplace.

## Install

In Claude Code:

```
/plugin marketplace add newlearningstart0826-dotcom/claude
/plugin install creator-toolkit@newlearning-plugins
```

## Plugins

### creator-toolkit

| Type    | Name               | What it does                                          |
|---------|--------------------|-------------------------------------------------------|
| Skill   | `content-calendar` | Builds a week-by-week posting plan from niche + goal  |
| Command | `/creator-toolkit:hooks <topic>` | Writes 10 short-form hooks for a topic  |

Works alongside [`instagram-skills`](https://github.com/sergebulaev/instagram-skills):

```
/plugin marketplace add sergebulaev/instagram-skills
/plugin install instagram-skills@instagram-skills
```

## Layout

```
.claude-plugin/marketplace.json          # marketplace catalog
plugins/creator-toolkit/
  .claude-plugin/plugin.json             # plugin manifest
  skills/<skill-name>/SKILL.md           # model-invoked skills
  commands/<command>.md                  # slash commands
```

## Adding a skill

1. Create `plugins/creator-toolkit/skills/<name>/SKILL.md` with `name` and
   `description` frontmatter (the description is what makes Claude pick it).
2. Bump `version` in `plugin.json` and `marketplace.json`.
3. Commit and push, then run `/plugin marketplace update newlearning-plugins`.

## Validate

```
claude plugin validate .
```
