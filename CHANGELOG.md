# Changelog

## FaceSlim v1.28.0 - 2026-08-12

- Drained the active roadmap after verifying shipped coverage for model integrity, deterministic regression tests, structured render diagnostics, reproducible setup, export provenance, accessibility QA, media preflight, provider diagnostics, the dependency canary, model inventory, optional restoration/upscale, modular boundaries, and localization.
- Repaired the local development environment with `tools/bootstrap_dev.py` and verified the 38-test suite, compile checks, CPU provider benchmark, Python 3.12 compatibility dry-run, and clean PyInstaller build.

## FaceSlim v1.27.0 - 2026-07-01

- Fixed CLI batch processing where per-job params, max_faces, parser_model, and onnx_provider leaked between jobs — subsequent jobs inherited settings from earlier jobs when they lacked explicit overrides.
- Fixed video export and batch video processing silently exporting 0 frames when container format reported unknown frame count (CAP_PROP_FRAME_COUNT ≤ 0).
- Fixed OneEuroFilter ignoring timestamp `t=0` by using truthiness instead of None check, causing frequency drift on the first processed frame.
- Fixed NaN/non-finite FPS from cv2 VideoCapture causing crashes or infinite loops in preview, export, batch, and CLI video paths.
- Added parameter clamping (0–100, 0–1024 for tile size) to CLI and manifest overrides to prevent out-of-range values causing visual corruption.
- Added path sanitization to PresetManager.delete matching the existing save sanitization.
- Added user feedback for unsupported dropped files and failed image loads.
- Added missing file extensions (.flv, .m4v, .tif) to GUI file dialogs.
- Removed unused jax, jaxlib, and opencv-contrib-python from requirements.txt.
- Added explicit UTF-8 encoding to all file I/O operations.
- Deduplicated FACE_OVAL (was identical copy of JAW_CONTOUR).
- Removed unused variable and orphaned comment.

## FaceSlim v1.26.0 - 2026-06-29

- Split the legacy monolithic implementation into importable `faceslim` package modules for runtime/i18n, models, pipeline, exporters, UI, and CLI.
- Kept `FaceSlim_v1.py` as a compatibility launcher/re-export surface while preserving existing GUI and CLI commands.
- Added module-boundary regression coverage and updated Docker packaging to copy the new package.

## FaceSlim v1.25.0 - 2026-06-29

- Added localization-ready translation helpers with English default and pseudo-locale modes for UI/CLI QA.
- Routed main GUI labels, primary controls, tabs, and core CLI headings through the translation layer.
- Added pseudo-locale overflow guardrail tests and CLI pseudo-locale smoke coverage.

## FaceSlim v1.24.0 - 2026-06-29

- Added an optional post-stage model lane for GFPGAN face restoration and Real-ESRGAN 2x upscale, defaulting to off.
- Added GUI and CLI controls for post-stage model selection, strength, identity fidelity, and upscale tile size.
- Routed post-stage processing through image, video, batch, and CLI exports with split/side-by-side comparison support and 2x output sizing.
- Added GFPGAN and Real-ESRGAN provenance, license, hash, cache, and provider reporting to the model inventory.

## FaceSlim v1.23.0 - 2026-06-29

- Added model source, license, cache path, hash verification, and active-provider inventory for every downloaded model.
- Added GUI model inventory refresh/redownload controls and CLI `--list-models` / `--redownload-model`.
- Persisted packaged-build model downloads under `%APPDATA%\.faceslim\models` instead of PyInstaller's temporary extraction directory.
- Documented upstream model sources and licenses in the README model table.

## FaceSlim v1.22.0 - 2026-06-29

- Added `requirements-upgrade-canary.txt` for a Python 3.12+ dependency upgrade lane.
- Added `tools/check_compatibility.py` to compare current pins against PyPI and run an isolated canary import smoke.
- Documented the Python compatibility matrix and blockers before bumping runtime pins.

## FaceSlim v1.21.0 - 2026-06-29

- Added a persisted ONNX Runtime provider selector for Auto, CPU, CUDA, and DirectML.
- Added GUI and CLI provider diagnostics with available providers, selected/fallback provider, and one-frame benchmark output.
- Routed parser and matting ONNX sessions through a shared provider resolver with CPU fallback on unavailable or failed provider overrides.

## FaceSlim v1.20.0 - 2026-06-28

- Added shared media preflight checks for video export, batch jobs, and CLI processing.
- Reported resolution, frame count/duration, output size, memory/time estimates, free disk space, output writability, and MP4 writer availability before long renders start.
- Refused blocked or unsafe jobs before inference and logged preflight failures to `render.log`.

## FaceSlim v1.19.0 - 2026-06-28

- Added accessible names and descriptions across primary GUI controls, sliders, toggles, combo boxes, and export/batch actions.
- Added explicit tab-order metadata for the main workflow.
- Added local accessibility QA tests for control metadata and dark-theme contrast ratios.

## FaceSlim v1.18.0 - 2026-06-28

- Added always-on FaceSlim provenance metadata to image exports.
- Embedded IPTC/XMP DigitalSourceType, edit timestamp, tool version, disclosure-watermark state, and source-preservation state in PNG/JPEG outputs.
- Updated `--strip-metadata` semantics so source metadata can be removed while FaceSlim provenance remains.

## FaceSlim v1.17.0 - 2026-06-28

- Added `tools/bootstrap_dev.py` to create or repair `.venv`, reinstall requirements, and run local verification from one command.
- Added stale `pyvenv.cfg` base-interpreter detection so copied or broken virtual environments are rebuilt automatically.
- Documented the bootstrap command in Quick Start and requirements setup.

## FaceSlim v1.16.0 - 2026-06-28

- Added JSON-lines `render.log` diagnostics for export, batch, CLI, frame-processing, and FFmpeg mux failures.
- Kept rendered video output intact when FFmpeg audio muxing fails and surfaced the warning in GUI status.
- Made CLI processing return a non-zero exit code when any requested media job fails.

## FaceSlim v1.15.0 - 2026-06-28

- Added exact-size and SHA-256 verification for all auto-downloaded model artifacts.
- Added atomic model download replacement with corrupt-cache retry handling.
- Added a local `unittest` regression suite for CLI, manifest, batch, cancellation, and image export paths.

## FaceSlim v1.14.0 - 2026-06-28

- Added an OBS-compatible Virtual Cam preview toggle powered by `pyvirtualcam`.
- Added graceful UI feedback when the local virtual-camera backend is unavailable.

## FaceSlim v1.13.0 - 2026-06-28

- Added a Docker CLI image path with a slim Dockerfile, `.dockerignore`, and reduced runtime requirements.
- Documented headless container usage for farm rendering.

## FaceSlim v1.12.0 - 2026-06-28

- Added a first-launch responsible-use gate for consent, disclosure, and platform-rule expectations.
- Persisted the acknowledgement in Qt settings while leaving CLI mode unchanged.

## FaceSlim v1.11.0 - 2026-06-28

- Added a per-second video timeline scrubber for file playback.
- Added seek handling that reprocesses the selected frame with the current slider state.

## FaceSlim v1.10.0 - 2026-06-28

- Added a batch queue dialog with per-file status, progress, ETA, and single-job cancellation.
- Added worker-side skip handling so queued or current video jobs can be cancelled without aborting the batch.

## FaceSlim v1.9.0 - 2026-06-28

- Added a visual-only Teeth Mask preview overlay for the BiSeNet mouth-interior whitening target.
- Kept the hint overlay out of exported image/video data by storing masks separately from processed frames.

## FaceSlim v1.8.0 - 2026-06-28

- Added expression neutralization with MediaPipe blendshape scores to soften frowns and raised/lowered brows.
- Added GUI and CLI controls for `expression_neutralize`.

## FaceSlim v1.7.0 - 2026-06-27

- Added optional MODNet ONNX matting refinement for ROI warp masks.
- Added GUI and CLI controls for `matting_refine` and documented the MODNet model.

## FaceSlim v1.6.0 - 2026-06-27

- Added selectable BiSeNet ResNet18/ResNet34 ONNX parser models for GUI, CLI, exports, and batch manifests.
- Persisted the parser-model setting and documented the new `--parser-model` option.

## FaceSlim v1.5.0 - 2026-06-27

- Added DirectML-backed ONNX Runtime provider selection on Windows.
- Added under-eye smoothing, hair controls, and procedural makeup overlays across GUI and CLI.
- Added per-face overrides, batch manifests, disclosure watermarks, split/side-by-side video export, and image metadata preservation.
- Added PyInstaller packaging with multiprocessing freeze guards and a compatibility launcher.

## Roadmap archive — 2026-08-10 — ROADMAP.md

<details>
<summary>Original roadmap snapshot</summary>

```markdown
# ROADMAP

Backlog for FaceSlim. Keep the MediaPipe + BiSeNet backbone; expand model options, video export
quality, and batch pipelines.

## Planned Features

### Models

### Editing features

### Pipeline

### Safety

### Distribution

## Competitive Research

- **BeautyCam / Meitu / YouCam Perfect** — mobile apps with aggressive retouch presets and AR
  makeup. Feature cues: one-tap presets, skin-tone sliders, AR makeup.
- **Remini / Topaz Photo AI** — upscale + face-enhance pipelines. Borrow their superres stage as
  an optional post step.
- **Open-source `face-parsing.PyTorch` and `DECA`** — primary technical references for upgrades
  noted above.
- **Avatarify / Deep-Live-Cam** — real-time face manipulation frameworks; cues for low-latency
  preview, while FaceSlim remains reshape-first rather than swap-first.

## Nice-to-Haves

- **Preset marketplace** — signed JSON presets with thumbnails, community upload.
- **Photoshop plugin** via UXP that calls a local FaceSlim CLI for automation inside Photoshop
  actions.
- **Automatic preset suggestion** based on face shape analysis (oval / round / square / heart).
- **Undo stack export** as a recipe file — replay an edit on a different photo.
- **Timeline keyframes** for video — ramp sliders over time.

## Open-Source Research (Round 2)

### Related OSS Projects
- **RetouchML** — https://github.com/ju-leon/RetouchML — StyleGAN2 latent-space beautification; face detected, normalized, then gradient-ascended toward a "prettier" attractiveness classifier.
- **photo-enhancer (nuwandda)** — https://github.com/nuwandda/photo-enhancer — Wraps GFPGAN (faces) + RealESRGAN (background) in one pipeline; good reference for split face/bg processing.
- **FaceEnhancementAndMakeup** — https://github.com/ZainabZaman/FaceEnhancementAndMakeup — DLIB landmarks for makeup + CodeFormer for face restoration.
- **facefusion** — https://github.com/facefusion/facefusion — Industry-scale face manipulation platform; model zoo and pipeline graph are the takeaway.
- **Awesome-Face-Restoration** — https://github.com/sczhou/Awesome-Face-Restoration — Curated index of face restoration papers/weights; treat as the SOTA tracker.
- **GFPGAN** — https://github.com/TencentARC/GFPGAN — Canonical face-perfector GAN; still the baseline for skin-smooth + detail-preserve.
- **CodeFormer** — https://github.com/sczhou/CodeFormer — Robust face restoration under heavy degradation; better than GFPGAN on blurry/low-res input.

### Features to Borrow
- Latent-space slimming slider from `RetouchML` — move along the StyleGAN2 "face width" direction instead of mesh-warping; preserves identity better than liquify.
- Two-stage face/bg pipeline from `nuwandda/photo-enhancer` — segment face, enhance separately, alpha-composite back. Avoids background smoothing artifacts.
- DLIB 68-point landmark gating from `FaceEnhancementAndMakeup` — run reshape only inside the face polygon; skip ears/hair.
- Model-zoo selector like `facefusion` — let users pick between GFPGAN / CodeFormer / RestoreFormer at runtime.
- CodeFormer's "fidelity weight" slider — user dial between strict identity preservation and aggressive restoration.
- Batch CLI parity (`facefusion` style): every GUI operation also exposed as a CLI flag for headless runs.

### Patterns & Architectures Worth Studying
- **StyleGAN2 inversion + direction editing** (`RetouchML`): invert face → edit latent → regenerate. Cleaner for geometry edits than landmark warp.
- **ONNX Runtime model-swap** (`facefusion`): ship models as ONNX, let users download alternates. Avoids PyTorch install footprint.
- **Face-parsing mask composite**: BiSeNet face-parsing → per-region weight maps → blend restored face back into original pixels. Used by both `CodeFormer` and `GFPGAN` demos; prevents halo artifacts.
- **Tile-based inference for >4K images** (`RealESRGAN`): split into overlapping tiles, process, seam-blend. Needed if users drop in DSLR RAWs.

## Research-Driven Additions

- [ ] P0 - Verify downloaded model artifacts
  Why: Current model downloads only check minimum byte size, so corrupt or replaced weights can be accepted.
  Evidence: `FaceSlim_v1.py` `ensure_model()`, `ensure_parsing_model()`, `ensure_matting_model()`; MediaPipe/yakhyo model URLs.
  Touches: `FaceSlim_v1.py`, model download/cache helpers, README model section.
  Acceptance: Each downloaded model is validated against a versioned manifest with SHA-256, expected size, source URL, and clear retry/failure UI/CLI output.
  Complexity: M

- [ ] P0 - Add deterministic CLI and pipeline regression tests
  Why: The tracked tree has no tests, while the app now has many parser, manifest, export, and worker paths.
  Evidence: repo scan for tests; `FaceSlim_v1.py` `load_batch_manifest()`, `parse_face_overrides()`, `cli_process()`, `ExportThread`, `BatchThread`.
  Touches: `tests/`, `FaceSlim_v1.py`, fixture media, README test commands.
  Acceptance: Local test command covers preset listing, manifest parsing, face override validation, unsupported media handling, image export smoke, and worker cancellation without launching the GUI.
  Complexity: M

- [ ] P0 - Surface export and FFmpeg failures through structured logs
  Why: Audio mux and some frame-processing errors can be swallowed or printed without durable user diagnostics.
  Evidence: `FaceSlim_v1.py` `ExportThread._mux_audio()` broad `pass`, `VideoThread.run()` print-only frame errors, README crash-log behavior.
  Touches: `FaceSlim_v1.py`, export threads, status bar/toast handling, crash/log file path.
  Acceptance: Every failed mux/export/frame-processing path writes a timestamped render log, updates GUI/CLI status, preserves the original output when rollback is needed, and returns non-zero in CLI mode on hard failure.
  Complexity: M

- [ ] P0 - Repair reproducible local environment setup
  Why: The repo `.venv` points at a missing Python path on this machine, blocking the documented local verification path.
  Evidence: `.venv\Scripts\python.exe` failure; `CLAUDE.md` key commands; `requirements.txt`.
  Touches: README setup section, `requirements.txt`, optional setup script, `CLAUDE.md`.
  Acceptance: A fresh checkout can create a working venv with one documented command, run `--list-presets`, and compile the main modules without relying on stale absolute interpreter paths.
  Complexity: S

- [ ] P1 - Embed C2PA/IPTC provenance metadata on export
  Why: The optional visual watermark is useful but removable; platform policies and standards increasingly expect durable altered-media metadata.
  Evidence: C2PA 2.2, IPTC Photo Metadata, YouTube altered-content disclosure policy, `FaceSlim_v1.py` `apply_disclosure_watermark()` and `save_rgb_image()`.
  Touches: `FaceSlim_v1.py`, export pipeline, metadata preservation path, README disclosure section.
  Acceptance: Image exports can include C2PA/IPTC fields identifying FaceSlim editing, source preservation status, edit timestamp, and disclosure flag without stripping existing EXIF/ICC unless requested.
  Complexity: L

- [ ] P1 - Add accessibility metadata and contrast/focus QA
  Why: The GUI has many custom controls and tooltips but no explicit accessible names/descriptions or automated focus/contrast checks.
  Evidence: `FaceSlim_v1.py` GUI construction around sliders/buttons; PyQt accessibility APIs; commercial editor UX expectations.
  Touches: `FaceSlim_v1.py`, UI construction helpers, screenshot/QA harness.
  Acceptance: Sliders, checkboxes, buttons, combo boxes, timeline, and preview controls expose accessible names/descriptions; dark/light contrast and tab focus order are verified by a repeatable local check.
  Complexity: M

- [ ] P1 - Add large-media preflight and resource guardrails
  Why: Large videos and high-resolution images are processed without estimating memory, frame count, disk space, codec support, or output writability.
  Evidence: `FaceSlim_v1.py` `VideoCapture`/`VideoWriter` export loops; Real-ESRGAN tile-processing pattern; README DSLR/video claims.
  Touches: `FaceSlim_v1.py`, export dialog, CLI validation, batch queue.
  Acceptance: GUI/CLI report input resolution, duration/frame count, estimated output size/time, available disk space, codec availability, and a clear refusal/recovery path before long renders start.
  Complexity: M

- [ ] P1 - Add runtime provider diagnostics and selector
  Why: ONNX providers are auto-selected, but users cannot see or compare CUDA, DirectML, CPU, or future provider choices.
  Evidence: `FaceSlim_v1.py` `FaceParsingEngine` and `MattingRefinementEngine`; ONNX Runtime provider release docs.
  Touches: `FaceSlim_v1.py`, settings UI, CLI flags, README troubleshooting.
  Acceptance: Settings/CLI show available providers, selected provider per model, a one-frame benchmark, fallback reason, and persisted override with safe fallback to CPU.
  Complexity: M

- [ ] P1 - Create dependency and Python upgrade lane
  Why: The app pins MediaPipe 0.10.14, ONNX Runtime 1.18.1, OpenCV 4.10.0.84, NumPy 1.26.4, and Python 3.9+ while current PyPI and Python lifecycle data have moved on.
  Evidence: `requirements.txt`; PyPI version checks for MediaPipe/ONNX Runtime/OpenCV/NumPy; Python version status docs.
  Touches: `requirements.txt`, `requirements-docker.txt`, Dockerfile, PyInstaller spec, compatibility smoke tests.
  Acceptance: A compatibility matrix records supported Python/dependency versions, verifies Python 3.12+, tests ONNX Runtime upgrades, and documents any blockers before bumping pins.
  Complexity: L

- [ ] P1 - Add model provenance and license panel
  Why: Users need to know which model is active, where it came from, its license/provenance, and whether it was verified.
  Evidence: README model table; `FaceSlim_v1.py` model constants; `Roadmap_Blocked.md` legal/model-choice note for 3DMM.
  Touches: `FaceSlim_v1.py`, Settings/Quality UI, CLI `--list-models`, README model section.
  Acceptance: GUI and CLI list installed/downloadable models with source URL, size, hash status, license note, active provider, cache path, and redownload action.
  Complexity: M

- [ ] P2 - Add optional restoration/upscale post-stage with identity control
  Why: GFPGAN, CodeFormer, Real-ESRGAN, Warlock-Studio, and Topaz/Remini show restoration/upscale is table-stakes, but it must be optional to avoid identity drift.
  Evidence: GFPGAN, CodeFormer fidelity control, Real-ESRGAN tiling, existing ROADMAP superres note.
  Touches: model registry, export pipeline, CLI flags, settings UI, README.
  Acceptance: Users can enable a post-stage model with face/background separation, strength/fidelity control, tile size, preview comparison, and CLI parity; default remains off.
  Complexity: XL

- [ ] P2 - Split the monolithic implementation into testable modules
  Why: One 3,700+ line file mixes download, inference, effects, GUI, threads, export, presets, and CLI logic, making regression coverage and plugin/API work harder.
  Evidence: `FaceSlim_v1.py` class/function inventory; Adobe UXP/local automation opportunity.
  Touches: `faceslim/` package modules, `FaceSlim.py`, `FaceSlim_v1.py`, PyInstaller spec, Dockerfile, tests.
  Acceptance: Public launch commands still work, but model management, pipeline effects, exporters, CLI, and UI live in separate modules with import-safe tests.
  Complexity: L

- [ ] P2 - Add localization-ready UI strings
  Why: Commercial retouch tools are global, but FaceSlim strings are hard-coded throughout the PyQt UI and CLI.
  Evidence: `FaceSlim_v1.py` GUI labels/status strings; Facetune/YouCam/Meitu global product surfaces.
  Touches: `FaceSlim_v1.py`, translation resource files, README.
  Acceptance: UI/CLI strings are routed through a translation table, English remains default, and at least one pseudo-locale test catches clipping/overflow in the main controls.
  Complexity: M
```

</details>
