# Kiddo Doodle Alive（童画活起来）

把小朋友的涂鸦照片，做成奶油纸底、缩小居中、保留稚拙线的静帧，再可选生成几秒「活过来」的短视频。

这是一个 [Agent Skills](https://github.com/agentskills) 兼容的公开 skill，适合父母用 AI agent 纪念孩子的创作。它**不是**任何商业修图 / 动图 App 的官方技能，也不复刻其品牌或界面。

## 安装

```bash
npx skills add https://github.com/JWu527/kiddo-doodle-alive --skill kiddo-doodle-alive
```

或手动克隆到 agent 的 skills 目录：

```bash
git clone https://github.com/JWu527/kiddo-doodle-alive.git ~/.agents/skills/kiddo-doodle-alive
```

## 你会得到什么

1. **静帧**：奶油纹理纸面 + 居中缩小的童画重绘 + 可选英文手写小字（如 `Lulu's little rainbow`）
2. **动效**：用户确认静帧后，生成 6–12 秒轻动作短视频（呼吸、闪烁、轻晃）
3. **文件纪律**：不覆盖原图；路径与像素写清楚

## 目录

```text
kiddo-doodle-alive/
├── SKILL.md
├── README.md
├── LICENSE.md
├── references/
│   ├── style-recipe.md
│   ├── still-prompt.md
│   ├── motion-prompt.md
│   └── privacy.md
├── examples/
│   └── caption-patterns.md
└── scripts/
    └── check_frontmatter.py
```

## 许可

MIT-0 — 见 `LICENSE.md`。

## 隐私

儿童画作默认私密。公开发布本仓库时**不要**提交真实孩子的原图或成片；示例只用脱敏文字。详见 `references/privacy.md`。
