# 07 · Higgsfield (optional, out of contest)

## The trade-off

The Filmathon rules say that image, video, audio and music must come **only** from the ElevenLabs Pro package. Teams that use other generators, a larger package or extra credits **compete outside the contest and cannot win a prize**. The film can still be screened.

Higgsfield is not mentioned on the official event page. Use it only if you've decided the visual quality is worth giving up the prizes, or for a non-contest version of the same film afterwards.

## Connecting Higgsfield to Claude

Higgsfield documents a hosted MCP server. These details come from a third-party write-up that cites Higgsfield's help pages, so **verify them on Higgsfield's own site** before relying on them.

- **Server URL:** `https://mcp.higgsfield.ai/mcp`, with OAuth sign-in through your Higgsfield account (no API key)
- **Claude Desktop / claude.ai:** Settings → Connectors → Add custom connector → paste the URL
- **Claude Code:** the CLI route, `npm i -g @higgsfield/cli`, then log in and install the companion skills
- **Plan:** MCP use needs a paid plan, and generations draw on your normal credits

Third-party community MCP servers exist. Prefer the official one for anything that handles your account.

## Using it with this kit

Nothing else changes. Download the generated clips into `shots/`, name them `s01.mp4`, …, and run `rough_cut.py` as normal. The script normalises mixed sizes and frame rates, so clips from different tools still line up.

## Sources

- [What is Higgsfield MCP? (Creatify)](https://creatify.ai/blog/what-is-higgsfield-mcp-what-it-does-what-it-costs-and-how-to-use-it)
