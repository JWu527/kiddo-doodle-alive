# Publishing

1. 更新 `CHANGELOG.md` 与 `metadata.version`
2. `python3 scripts/check_frontmatter.py`
3. 确认没有真实儿童图片进入 git：`git status` / `git ls-files '*.jpg' '*.png' '*.mp4'`
4. push 到 `https://github.com/JWu527/kiddo-doodle-alive`
5. 安装验证：`npx skills add https://github.com/JWu527/kiddo-doodle-alive --skill kiddo-doodle-alive`
