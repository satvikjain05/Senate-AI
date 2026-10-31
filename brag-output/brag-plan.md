# Brag Plan: Senate AI

## What is this app?
Senate AI is a multi-agent AI debate platform that deploys councils of LLM personas — Optimist, Skeptic, Fact-Checker — to argue a question in parallel across Groq, Gemini, and Perplexity, then synthesizes a conflict-aware consensus verdict streamed in real-time over WebSockets, all wrapped in a cyberpunk neo-brutalist UI.

## The angle
This isn't another chatbot. This is an AI *courtroom*. Three AI minds enter. One verdict leaves. The cinematic angle treats the debate like an intelligence showdown — dramatic, high-stakes, neon-lit. The product's cyberpunk aesthetic already feels like a movie. The video leans into that.

## Hook (first 2-3 seconds)
Big question, giant pixel text on pure black: **"WHAT IF AI COULD ARGUE WITH ITSELF?"** — slams in with impact. Neon green glow bleeds outward. The question earns the next 18 seconds because the answer is wild.

## Key moments (the middle)
- The three persona cards appear one by one — Fact-Checker (cyan), Optimist (green), Skeptic (pink) — each with a pulsing dot and a one-line stance preview. This is the product *working*.
- The pink synthesis bubble fires: "SYNTHESIZING MULTI-AGENT VERDICT..." with a sparkle spinner. The verdict text streams in character by character.
- The Conflict Analysis panel reveals: green "Points of Agreement" bullets vs. red "Contested Points" bullets side by side. This is the payoff — disagreement made visible.

## Outro / punchline
Product name SLAMS in full-screen: **SENATE AI** in Press Start 2P pixel font, neon green with pink glow. Below it, one line: **"Multiple AI minds. One intelligent answer."** Hold 2 seconds. Cut to black.

## User flow worth showing
1. **Entry** — A cursor types "Is quantum computing a threat to encryption?" into the neon-bordered input. Hits LAUNCH.
2. **Key action** — Three persona stance cards animate in simultaneously with pulsing debate dots. Each shows a role name, stance, and content preview.
3. **Result** — The pink synthesis bubble appears. Verdict streams. Conflict analysis unfolds showing agreements vs. disagreements.

## Tone
- Preset: `cinematic`
- Creative direction: dramatic AI warfare trailer — neon-lit intelligence showdown
- Interpretation: Big motion, dramatic reveals, heavy type, sweeping transitions. Each scene lands with weight before the next begins. The cyberpunk palette is already cinematic — the video amplifies it.

## Format: landscape — 1920x1080
## Duration: 20 seconds

## Visual identity (from the project)
- Background: `hsl(240 6% 7%)` → `#0D0D12` (near-black)
- Accent (primary): `hsl(160 100% 50%)` → `#00FFB3` (neon green)
- Accent (secondary): `hsl(191 100% 50%)` → `#00C8FF` (cyan)
- Accent (tertiary): `hsl(300 100% 65%)` → `#FF4FD8` (hot pink)
- Text: `hsl(160 100% 70%)` → neon green for foreground; `hsl(0 0% 90%)` for card content
- Display font: Press Start 2P (pixel/retro)
- Body font: IBM Plex Sans
- Strongest visual elements: neo-brutalist cards with 3-4px borders and offset colored shadows (`box-shadow: 4px 4px 0px #00FFB3`), glow borders, scanline overlays, diagonal patterns, chunky buttons with active:translate-y press effect

## Share copy (draft)
We made AI argue with itself — three models, one verdict, zero hallucinations. Senate AI.

## Audio direction
- Role: cinematic support with dramatic build
- Music: `happy-beats-business-moves-vol-9-by-ende-dot-app.mp3` (~115 BPM) — energetic, builds well, good for beat-synced reveals
- Music treatment: start at 0s, low intro volume for first 2s hook, swell into persona card reveals, peak at synthesis moment, fade out on outro hold
- Music cue guidance: preset available at ~115 BPM. Target strong cues at ~4.23s (persona card entrance beat 1), ~6.34s (persona card beat 2-3), ~10.54s (synthesis slam), ~12.65s (conflict reveal). Beat grid windows: persona cards stagger to beats between 4.23-6.34s.
- Audio-reactive treatment: subtle; neon glow pulse on cards breathes with bass energy, not waveform bars
- SFX posture: moderate; motion-matched, professional — impact hits for major reveals, soft UI sounds for card arrivals
- Audio-coupled moments: typed question with keyboard ticks; persona cards arrive with card/impact sounds one by one; verdict text types in with subtle clicks; final SENATE AI slam with deep impact hit
- Restraint rule: audio must not overwhelm the cyberpunk atmosphere; no cartoon sounds, no excessive reverb, no generic whooshes

## Storyboard

### Scene 1 — The Hook — 3s
Full black screen. Giant Press Start 2P pixel text SLAMS in center-screen: **"WHAT IF AI COULD ARGUE WITH ITSELF?"** in #00FFB3 neon green. Text has a radiating glow that pulses once. Subtle scanline overlay.
Sequential/interaction: yes — text slams in as one unit with a slight scale overshoot (1.05→1.0)
Audio intent: dramatic impact, immediately grabs attention
Audio-coupled idea: single deep impact hit on text slam; low music bed fades in underneath
Music: cinematic build — starts low, energy rising
Transition mood: dramatic → Scene 2

### Scene 2 — The Interface — 4s
The Senate AI landing page input appears: dark background, neon green 3px bordered input field with the offset shadow. A cursor types **"Is quantum computing a threat to encryption?"** character by character (~1.5s typing). Then the **LAUNCH ⚡** button pulses and gets clicked. Below, the five agent pills (GPT, Claude, Gemini, DeepSeek, Perplexity) are visible in their colored bordered cards. Above, the **SENATE AI** logo in green + **AI** in pink, with the bouncing lightning bolt.
Sequential/interaction: yes — cursor types the question character by character, then clicks LAUNCH button with a press animation
Audio intent: building tension, the question being asked
Audio-coupled idea: subtle keyboard ticks on each typed character; satisfying click/snap on LAUNCH press
Music: energy building, approaching first strong beat
Transition mood: hard → Scene 3

### Scene 3 — The Council Debates — 6s
The ChatWorkspace debate view. Header bar with cyan border shows "COUNCIL IS THINKING & EVALUATING..." in pink with sparkle spinner. Below: three persona stance cards appear ONE BY ONE, staggered to beat grid:
1. **🔍 Fact-Checker** (cyan accent) — stance preview text fades in
2. **💡 Optimist** (green accent) — stance preview text fades in
3. **⚠️ Skeptic** (pink accent) — stance preview text fades in

Each card has a pulsing colored dot. Three animated ping dots (cyan/green/pink) pulse at staggered intervals. Status badge reads "CLASSIFYING & QUERYING" in green.

Then the pink synthesis bubble fires: border glows #FF4FD8, header reads **"SYNTHESIZING MULTI-AGENT VERDICT..."** with spinning sparkle icon. Verdict text begins streaming character by character.
Sequential/interaction: yes — three persona cards arrive one by one (~0.8s apart, aligned to beat grid between ~4.23-6.34s of track); then synthesis bubble slams in at ~10.54s strong cue
Audio intent: escalating energy — each card arrival adds momentum, synthesis is the peak
Audio-coupled idea: card arrival sounds (subtle impact) for each persona; louder impact hit for synthesis bubble slam; typing clicks as verdict streams
Music: building to peak, persona cards on beats, synthesis on strong cue
Transition mood: dramatic → Scene 4

### Scene 4 — The Verdict — 4s
The Conflict Analysis panel expands. Indigo header: **"Council Perspectives & Conflict Analysis — 3 LLMs Evaluated"**. Two panels slide in side by side:
- Left (emerald/green): **"Points of Agreement"** — 2 bullet points appear sequentially
- Right (rose/red): **"Contested Points & Disagreements"** — 2 bullet points appear sequentially

Above both, the **Synthesizer Judge Core Verdict** card in indigo shows a one-line verdict summary. The badge "Gemini • Groq • Llama" is visible.

This is the product's unique value prop made visual: AI disagreement, resolved.
Sequential/interaction: yes — agreement bullets appear one by one, then disagreement bullets one by one; verdict card fades in last
Audio intent: resolution, arrival, intelligence
Audio-coupled idea: soft reveal sounds for each bullet point; subtle confirmation tone for verdict card
Music: sustained energy from peak, beginning gentle descent
Transition mood: dramatic → Scene 5

### Scene 5 — The Slam — 3s
Clean black background. **SENATE AI** in massive Press Start 2P pixel font — "SENATE" in #00FFB3, "AI" in #FF4FD8 — slams in with scale overshoot and neon glow radiation. Below it, in IBM Plex Sans: **"Multiple AI minds. One intelligent answer."** fades in after 0.5s. Hold for 1.5s. Subtle scanline overlay. Cut to black.
Sequential/interaction: yes — logo slams first, tagline fades in after
Audio intent: final impact, dramatic close
Audio-coupled idea: deep impact hit on logo slam; music fades to silence during hold
Music: final beat hit, then fade to silence
Transition mood: end

**Music mood for this video:** cinematic, dramatic build-and-peak
**Audio summary:** A 20-second arc from silent impact → keyboard tension → escalating beat-synced council debate → peak synthesis slam → resolving verdict → final impact close. The audio mirrors the product's own flow: question → debate → verdict.
