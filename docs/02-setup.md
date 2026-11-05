# 02 · Setup

Do this **before** the event if you can. It takes about 10 minutes.

## 1. Install

macOS:

```bash
brew install ffmpeg uv
```

Linux: `sudo apt install ffmpeg` and `curl -LsSf https://astral.sh/uv/install.sh | sh`.
Windows: `winget install Gyan.FFmpeg astral-sh.uv`.

You also need Python 3 (already on macOS) and [Claude Code](https://claude.com/claude-code).

Check:

```bash
ffmpeg -version | head -1
uvx --version
python3 --version
```

## 2. ElevenLabs API key

Registered participants get one month of **ElevenLabs Pro** (600,000 credits). Create an API key in your ElevenLabs profile settings, then:

```bash
cp .env.example .env
# edit .env and paste the key. Never commit this file.
```

## 3. Connect ElevenLabs to Claude Code

ElevenLabs publishes an official MCP server, [`elevenlabs-mcp`](https://pypi.org/project/elevenlabs-mcp). It lets the agent generate speech, sound effects and music and save files straight into this repo.

```bash
cp .mcp.json.example .mcp.json
# put your key in .mcp.json under ELEVENLABS_API_KEY
```

Or add it by command:

```bash
claude mcp add elevenlabs -e ELEVENLABS_API_KEY=your_key -e ELEVENLABS_MCP_OUTPUT_MODE=files -- uvx elevenlabs-mcp
```

Start `claude` in this folder and ask it to list ElevenLabs voices to confirm it works.

> **Know the limits.** The MCP server covers audio (speech, sound effects, music, voices). Check at the event whether it also exposes image/video generation. If not, generate image and video in the ElevenLabs web app and drop the files into `shots/`. The rule requires all generation to come from the Pro package either way.

Never paste API keys into chat. `.env` and `.mcp.json` are in `.gitignore`.

## 4. Pick an editor (optional)

`rough_cut.py` is enough for a first cut. For hand-tuning, see [05-editing.md](05-editing.md). Pre-download whichever you choose, because the venue wifi is shared.
