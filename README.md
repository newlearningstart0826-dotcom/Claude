# Claude

## Skills

### social-post
Installed at `.claude/skills/social-post` from
[Hao0321/claude-skill-social-post](https://github.com/Hao0321/claude-skill-social-post) (MIT, `main` @ e0720ed).
Claude Code loads it automatically when you open this repo. Ask things like "寫一篇 IG 貼文", "幫我規劃內容" or "開啟 Social Post 工作台".

First-time personal setup (run on your own computer; these files are gitignored and stay local):

```bash
cd .claude/skills/social-post
cp style_profile.example.md style_profile.md
cp content_plan.example.md content_plan.md
# edit voice_quick.md and current_brief.md with your own voice/direction, then:
python -B scripts/social_governance.py bootstrap --write
python -B scripts/social_governance.py status
```

Workbench (local GUI): `python -B .claude/skills/social-post/scripts/workbench.py` → http://127.0.0.1:8766

Never commit real posts, analytics, comments, cookies or tokens.
