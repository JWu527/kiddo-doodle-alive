# 动效提示词模板

仅在用户确认静帧后使用。以静帧为 image_path（首帧）。时长默认 6 秒，用户要求更长时用 10–12 秒（不超过宿主上限）。

```text
Gentle picture-book life: the small doodle stays centered on cream paper.
{motion_beats}.
Keep the exact naive child-drawn look and the handwritten caption "{caption}".
No camera zoom, no morphing into photo-real, no new characters.
```

## motion_beats 示例

- 彩虹：soft breathing bob; clouds gently drift; tiny stars twinkle
- 动物：soft breathing bob; tiny blink; dots softly shimmer
- 多形状：each shape takes a turn — wobble, roll in place, soft heartbeat, twinkle

## 交付话术

- 先发视频附件，再给本机路径
- 明确：普通短视频 ≠ iPhone Live Photo
