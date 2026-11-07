# 动效提示词模板

仅在用户确认静帧后使用。以静帧为 `image_path`（首帧）。

## 默认参数（强制）

- 时长默认 **10 秒**；用户只要短一点再用 6 秒；不超过宿主上限（常见 15 秒）
- 分辨率优先 **720p**（宿主支持时）
- **只动原图 / 静帧里已经有的东西**：不添加蝴蝶、毛线、爱心、花草、太阳、云朵、新角色等原图没有的元素
- 动作要密、分镜清晰：约每 1.5–2 秒换一个姿态或节拍，避免整段只「呼吸」
- 不换背景、不换构图、不放大成写实、不抹掉稚拙线；手写 caption 保持不动

## 提示词骨架

```text
Animate only what is already drawn: {subject} on warm cream paper.
Keep every naive wobbly crayon/marker line, color, silhouette, paper texture and the handwritten caption "{caption}" exactly as they are.
Do NOT add any new objects, characters, props, sparkles, flowers, hearts or decorations that are not in the still.
Rich pose / motion beats only on existing elements:
{beat_0_2};
{beat_2_4};
{beat_4_6};
{beat_6_8};
{beat_8_10}.
Hand-drawn boiling-line feel, varied frames, steady camera, faint existing shadow only, soft warm light.
```

## motion_beats 示例（10 秒 · 五段）

- **动物（如粉点小猫）**
  - 0–2s blinks and breathes, ears twitch
  - 2–4s stretches and raises one paw
  - 4–6s turns slightly and wags its tail
  - 6–8s shifts weight and tilts its head
  - 8–10s settles back to a calm seated pose
- **彩虹**
  - 0–2s arcs gently breathe and shimmer along their lines
  - 2–4s colors ripple slightly from left to right
  - 4–6s whole rainbow soft-bounces, arcs flex a little
  - 6–8s a slow wave travels through the bands
  - 8–10s settles back to calm
- **多形状**
  - 0–2s each shape gently breathes and wobbles in place
  - 2–4s they take turns bobbing one after another
  - 4–6s they rotate slightly and bounce
  - 6–8s they shift toward each other a little then apart
  - 8–10s settle back to calm

## 反例（不要写进提示）

- 「butterfly / yarn / hearts / sparkles appear」「flowers sprout」「new stick figures join」
- 整段只有 soft breathing bob、没有任何姿态变化
- 镜头猛推拉、转场切镜、把童画改成成人插画或 3D

## 交付话术

- 先发视频附件，再给本机完整路径与实际宽高、时长
- 明确：普通短视频 ≠ iPhone Live Photo
- 若用户嫌「too much」：立刻去掉新增元素，只保留主体姿态变化后重出
