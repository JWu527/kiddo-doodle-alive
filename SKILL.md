---
name: kiddo-doodle-alive
description: Use when a user wants to turn a child's doodle or craft photo into a minimalist cream-paper remake and a short living animation, with naive line preserved, optional name caption, and originals never overwritten.
license: MIT-0
metadata:
  version: "0.1.0"
  homepage: https://github.com/JWu527/kiddo-doodle-alive
---

# Kiddo Doodle Alive — 童画活起来

把小朋友的随手涂鸦照片，做成「奶油纸底、缩小居中、保留稚拙线」的静帧，再可选做成几秒动效短片。适合家庭相册分享、纪念孩子创作，不是任何商业修图 App 的替代品或复刻。

以下路径相对于本 `SKILL.md` 所在目录。

## 许可与边界（强制）

- License: MIT-0；见 `LICENSE.md`
- 本 skill 是原创工作流说明，**不隶属于、不复刻、不替代**任何商业产品、App、课程或受版权保护的教程文案
- 用户提到具体商业 App 时：可以说「同类效果常见做法」，但不得声称本 skill 就是该 App，也不得照抄其界面文案、玩法名称或品牌素材
- 默认**不上传**孩子的画到未授权第三方；只用宿主已具备、用户已授权的本地或平台能力（例如本机图像/视频生成）
- 不覆盖原图；成片另存同目录，命名清楚
- 保留孩子原作的构图、比例、颜色倾向与稚拙笔触；不做换脸、虚构角色替换或过度「成人插画化」
- 英文手写小字只用用户提供的名字；没给名字就用中性标题或先问一句

## 何时使用

- 「把孩子的画做成活起来的效果 / 童画动起来 / 奶油纸极简解构」
- 用户发来小朋友涂鸦、手抄报、蜡笔/马克笔作品照片，希望做成可分享静帧或短视频
- 不要用于：成人商业插画精修、证件照、医疗影像、未经监护人同意的公开传播决策

## 工作流（强制）

1. **看原图**：用 Read / 图像工具打开用户照片，用一两句说清画面主体、介质（蜡笔、马克笔、贴纸等）和将做的改动。
2. **选配方**：默认走 `references/style-recipe.md` 的「极简奶油纸」配方。用户只要静帧就停在第 4 步；要动效再进第 5 步。
3. **静帧提示词**：按 `references/still-prompt.md` 组装生成提示，把原图路径放进 reference；画幅优先跟原图接近（常见 4:3）。
4. **交付静帧**：给用户预览；写明实际像素；另存文件，例如 `Lulu_彩虹_童画活起来.jpg`。用户不满意就按反馈改提示再出，不要直接跳到视频。
5. **动效**：用户确认静帧后，按 `references/motion-prompt.md` 做 6–12 秒短视频（宿主上限内）。先交付视频，再说明「这是普通短视频，不是 iPhone 实况照片」。
6. **路径回传**：同时给出可预览成片与本机完整路径（若已复制到用户电脑）。

## 输出命名

- 静帧：`{名字或主题}_童画活起来.jpg|png`
- 动效：`{名字或主题}_童画动效.mp4`
- 可选前后对比：`{名字或主题}_前后对比.jpg`（上原图下成片）

## 诚实说明局限

- AI 重绘可能平滑掉部分涂痕；若用户要「更像原作」，降低润色、加强参考权重
- 模型直出通常小于手机原片；需要打印时说明像素并尽量走宿主原尺寸能力
- 视频 ≠ Live Photo；转实况需另一步工具，且不保证成功
- 不能默认替代专业修图 App 的批量人像或 RAW 精修

## 参考文件

- `references/style-recipe.md` — 视觉配方与禁止项
- `references/still-prompt.md` — 静帧提示词模板
- `references/motion-prompt.md` — 动效提示词模板
- `references/privacy.md` — 儿童作品隐私
- `examples/caption-patterns.md` — 字幕句式示例（脱敏）
