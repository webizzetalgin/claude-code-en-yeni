---
name: my-remotion-video
description: Create fully rendered videos with Remotion (React-based programmatic video) tailored to specific social media platforms. Use this skill whenever the user wants to generate, produce, create, or render a video — including social media content (TikTok, Instagram Reels/Feed, YouTube Shorts, YouTube long-form, Twitter/X, LinkedIn), explainer videos, promotional clips, infographic videos, or animated content. Also trigger when the user uploads an existing video that needs subtitles, voiceover, or audio added. The skill handles the full interactive flow: asking for topic, brand color, target platform (with correct aspect ratio/resolution), language, then generates Remotion code with animations, infographics, royalty-free background music, captions/subtitles, and attention-grabbing visual effects. Trigger on phrases like "video oluştur", "video üret", "make a video", "create a reel", "generate a short", "Remotion ile video", or any video production request.
---

# My Remotion Video

This skill produces complete, render-ready Remotion video projects customized to the user's topic, brand, platform, and language. It also handles post-processing (subtitles + audio) for user-uploaded videos.

## Core principle

**Always interview the user first, then generate.** Never skip the intake questions — they determine dimensions, duration, tone, and assets. Ask them using the `ask_user_input_v0` tool when available (one question at a time if the interface supports it; otherwise grouped).

---

## Step 1: Detect the mode

Before asking anything, determine which mode applies:

- **Mode A — Generate from scratch**: No video file uploaded. Proceed to Step 2.
- **Mode B — Enhance uploaded video**: User uploaded a video file (check `/mnt/user-data/uploads/`). Skip to Step 6.

---

## Step 2: Intake interview (Mode A)

Ask these questions **in order**. Do not proceed until each is answered. Use `ask_user_input_v0` for questions 2–4 since they have discrete options; question 1 and 5 are free-text.

### Question 1 — Topic (free text)
> "Videonun konusu ne olsun? (örn: 'yapay zekanın geleceği', '5 sağlıklı kahvaltı tarifi')"

### Question 2 — Primary brand color
Offer common choices AND accept hex input:
- Option chips: `#FF0050` (pembe), `#0066FF` (mavi), `#00C853` (yeşil), `#FF6D00` (turuncu), `#9C27B0` (mor), `#000000` (siyah), "Özel hex gir"
- Store as `PRIMARY_COLOR`. Auto-derive a complementary accent and a neutral background.

### Question 3 — Target platform
Each platform maps to fixed dimensions, fps, and default duration:

| Platform | Width × Height | FPS | Default duration |
|---|---|---|---|
| TikTok | 1080 × 1920 | 30 | 30s |
| Instagram Reels | 1080 × 1920 | 30 | 30s |
| Instagram Feed | 1080 × 1350 | 30 | 30s |
| YouTube Shorts | 1080 × 1920 | 30 | 60s |
| YouTube (yatay) | 1920 × 1080 | 30 | 60s |
| Twitter/X | 1280 × 720 | 30 | 45s |
| LinkedIn | 1200 × 1200 | 30 | 45s |

### Question 4 — Language
Options: `Türkçe`, `English`, `Deutsch`, `Español`, `Français`, `العربية`. Affects on-screen text, captions, and TTS voice selection. For Arabic, enable RTL text rendering.

### Question 5 — Tone/style (optional, can default)
Options: `Enerjik & hızlı`, `Sakin & bilgilendirici`, `Mizahi`, `Profesyonel`, `Sinematik`.

Store answers as variables: `TOPIC`, `PRIMARY_COLOR`, `PLATFORM`, `DIMENSIONS`, `LANG`, `TONE`.

---

## Step 3: Generate the script and storyboard

Before writing code, draft a scene-by-scene plan and confirm briefly with the user (one-line confirmation is enough — don't over-interview).

Divide the duration into 4–8 scenes. Each scene has:
- A headline (≤8 words in the target language)
- A sub-point or data fact
- An animation type (see Step 4)
- Timing in frames

Write the caption script (for subtitles) in the target language — one line per scene, synced to timing.

---

## Step 4: Scaffold the Remotion project

Create the project under `/home/claude/my-remotion-video/`. Use bash:

```bash
cd /home/claude && npm create video@latest my-remotion-video -- --template=blank --yes
cd my-remotion-video && npm install
```

Then install visual/animation helpers:

```bash
npm install @remotion/google-fonts @remotion/shapes @remotion/transitions @remotion/captions @remotion/layout-utils
```

### Required composition structure

Create `src/Video.tsx` with a `<Composition>` that uses the dimensions from Step 2. The composition must include:

1. **Background layer** — gradient or subtle animated noise built from `PRIMARY_COLOR`.
2. **Scene sequencer** — use `<Series>` or `<TransitionSeries>` from `@remotion/transitions` with `fade`, `slide`, or `wipe` between scenes.
3. **Infographic layer** — for any scene with a number/stat, render an animated counter (`interpolate(frame, [start, end], [0, value])`) plus an SVG bar or donut from `@remotion/shapes`.
4. **Title animations** — use spring animations (`spring({ frame, fps, config: { damping: 12 } })`) for entrances. Never use instant cuts for text.
5. **Attention hooks** — every ~3 seconds something new must happen (new element, color pulse, zoom, text swap). This combats drop-off on short-form platforms.
6. **Captions layer** — always on, rendered on top. Use `@remotion/captions` or a simple `<Sequence>` per caption line. Style: bold, high-contrast, stroked or boxed background for legibility. Position: lower-third for horizontal, center-lower for vertical.
7. **Audio layer** — see Step 5.

### Font selection by language
- Latin (TR/EN/DE/ES/FR): `Inter` or `Poppins` via `@remotion/google-fonts/Inter`
- Arabic: `Cairo` or `Tajawal` via `@remotion/google-fonts/Cairo`, with `direction: 'rtl'`

---

## Step 5: Audio — royalty-free music + optional voiceover

### Background music (required, royalty-free only)

Use tracks from these **confirmed royalty-free** sources. Never embed copyrighted music:
- **Pixabay Music** (`https://pixabay.com/music/`) — CC0, no attribution required
- **Uppbeat free tier** (`https://uppbeat.io/`) — free with account
- **YouTube Audio Library** — free, some require attribution
- **Kevin MacLeod / incompetech** (`https://incompetech.com/`) — CC-BY

Instruct the user to download a track matching `TONE` and drop it at `public/bgm.mp3`. In `Video.tsx`:

```tsx
import { Audio, staticFile } from 'remotion';
<Audio src={staticFile('bgm.mp3')} volume={0.25} />
```

Volume must duck to ~0.15 if voiceover is present.

### Voiceover (optional)
If the user wants narration, generate a script in `LANG` and tell the user to either:
- Use a TTS service (ElevenLabs, OpenAI TTS, Google Cloud TTS) and save to `public/vo.mp3`, OR
- Record it themselves.

Then mount it:
```tsx
<Audio src={staticFile('vo.mp3')} volume={1} />
```

---

## Step 6: Mode B — Enhancing an uploaded video

When the user provides a video file, the output must include **both subtitles and audio**. Steps:

1. Copy the input to `/home/claude/my-remotion-video/public/input.mp4`.
2. In `Video.tsx`, use `<OffthreadVideo src={staticFile('input.mp4')} />` as the base layer.
3. **Subtitles — required**:
   - Ask the user: "Altyazıları sizin metninizden mi oluşturayım, yoksa videodaki konuşmayı otomatik mi çıkarayım?"
   - If auto: run Whisper locally — `pip install --break-system-packages openai-whisper` then `whisper input.mp4 --model small --output_format srt --language <LANG>`. Parse the SRT into `@remotion/captions` format.
   - If manual: take the text from the user and time-split evenly, or accept an SRT upload.
   - Render captions with the same legibility styling from Step 4 (bold, stroked, lower-third).
4. **Audio — required**:
   - Add royalty-free BGM (Step 5 sources) at `volume={0.2}`.
   - If the original has speech, keep it at `volume={1}`; if silent, offer TTS voiceover of the user's script.
5. Render using the input video's native dimensions.

---

## Step 7: Render

Update `src/Root.tsx` to register the composition with correct `width`, `height`, `fps`, and `durationInFrames` (= seconds × fps).

Render command:

```bash
cd /home/claude/my-remotion-video
npx remotion render src/index.ts MyVideo out/video.mp4 \
  --codec=h264 --crf=18
```

For platforms requiring specific codecs:
- Instagram/TikTok: H.264, AAC audio, MP4 — the default above works.
- YouTube Shorts: same.
- If render fails due to missing Chromium, run `npx remotion browser ensure` first.

Copy the final file to `/mnt/user-data/outputs/video.mp4` and present it with `present_files`.

---

## Step 8: Deliver

After rendering, present:
1. The rendered MP4 (primary deliverable).
2. The Remotion project folder (zipped) so the user can re-render with changes.
3. A short summary: platform, dimensions, duration, music source with license note.

Always include the license/attribution info for any music used, even CC0, so the user knows they're safe to publish.

---

## Failure modes to avoid

- **Don't skip the interview.** Guessing the platform means wrong dimensions and a useless render.
- **Don't use copyrighted music.** Only the sources in Step 5. If unsure, don't include it — use silence or a simple generated ambient tone.
- **Don't omit captions.** Every video from this skill ships with captions on — short-form platforms are watched muted.
- **Don't use static text.** Every title needs a spring or interpolate-based entrance.
- **Don't hardcode English.** Respect `LANG` for every on-screen word, including fallback/error text.
- **Don't forget RTL for Arabic.** Set `direction: 'rtl'` and right-align.
- **Don't render without verifying durationInFrames matches fps × seconds** — off-by-one here silently truncates the video.

---

## Quick reference — minimal Video.tsx skeleton

```tsx
import { AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';
import { TransitionSeries, linearTiming } from '@remotion/transitions';
import { fade } from '@remotion/transitions/fade';

export const MyVideo: React.FC<{ primaryColor: string; scenes: Scene[] }> = ({ primaryColor, scenes }) => {
  const { fps } = useVideoConfig();
  return (
    <AbsoluteFill style={{ backgroundColor: '#0b0b0f' }}>
      <TransitionSeries>
        {scenes.map((s, i) => (
          <React.Fragment key={i}>
            <TransitionSeries.Sequence durationInFrames={s.frames}>
              <SceneBlock scene={s} color={primaryColor} />
            </TransitionSeries.Sequence>
            {i < scenes.length - 1 && (
              <TransitionSeries.Transition timing={linearTiming({ durationInFrames: 15 })} presentation={fade()} />
            )}
          </React.Fragment>
        ))}
      </TransitionSeries>
      <CaptionsOverlay scenes={scenes} />
      <Audio src={staticFile('bgm.mp3')} volume={0.2} />
    </AbsoluteFill>
  );
};
```

Use this as the starting point and expand per scene needs.
