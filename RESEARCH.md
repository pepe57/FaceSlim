# FaceSlim research

Updated for FaceSlim v1.29.1 on September 7, 2026.

## Executive Summary

FaceSlim is a local Python and PyQt desktop and CLI suite for landmark-based face reshaping, mask-guided finishing, batch rendering, Docker CLI use, and PyInstaller distribution. Its strongest position is private on-device editing with unusually broad GUI and CLI parity for a small project. Model verification, regression coverage, render diagnostics, reproducible setup, export provenance, accessibility metadata, media preflight, provider diagnostics, dependency canaries, and model inventory are now implemented.

## Product Map

- Core workflows: live webcam/file preview, slider-driven face reshaping, parsing-based beauty edits, batch image/video processing, manifest-driven CLI jobs.
- User personas: privacy-sensitive creators, batch editors processing portraits/video clips, developers wanting a local CLI/Docker renderer, streamers testing real-time virtual camera output.
- Platforms and distribution: Python 3.10+ source, Python 3.11 Windows release host, Windows/macOS/Linux source targets, PyInstaller Windows spec, Docker CLI image, local ONNX/MediaPipe model downloads.
- Key integrations and data flows: MediaPipe Face Landmarker -> TPS/ROI warp -> BiSeNet/MODNet ONNX masks -> OpenCV/Pillow export -> optional FFmpeg audio mux -> optional pyvirtualcam preview output.

## Competitive Landscape

- FaceFusion: strong model-zoo, provider, and job-pipeline surface for face manipulation. Learn its explicit model/runtime selection and batch ergonomics; avoid face-swap-first positioning that would dilute FaceSlim's reshape/retouch identity.
- GFPGAN and CodeFormer: strong face restoration baselines with identity/fidelity tradeoffs. Learn optional restoration as a post-stage with a fidelity slider; avoid making restoration mandatory or silently changing identity.
- Real-ESRGAN and Warlock-Studio: strong tiling/upscale/batch patterns for large media and GPU workflows. Learn tile preflight, estimated cost, and multi-model batch orchestration; avoid bloating the base install with every model.
- RetouchML: shows latent-space beautification can preserve smooth geometry better than mesh warps in some cases. Keep as an experimental path only because inversion cost and identity drift conflict with FaceSlim's fast local workflow.
- Facetune, YouCam Perfect, Meitu, Remini, Topaz Photo AI: commercial tools package one-tap presets, face/body controls, enhancer/upscale, and mobile-first UX. Learn guided presets, visual previews, and paid-tier signals; avoid subscription/account/cloud dependencies.
- Adobe Photoshop UXP: best integration path for professional editors. Learn local CLI/service automation from Photoshop actions; avoid building a plugin before the local API/manifest contract is stable.

## Security, privacy, and reliability

- Model downloads use pinned sizes and SHA-256 hashes, with cache inspection and redownload controls.
- Export failures are written to structured diagnostics and return nonzero CLI status where appropriate.
- Image exports preserve source metadata by default and add IPTC/XMP provenance for the edit.
- Large jobs run a preflight for media shape, codecs, output access, estimated resources, and free disk space.
- The repaired `.venv` provides the pinned Windows release environment and repeatable local verification.
- The runtime now pins MediaPipe 0.10.35, Pillow 12.3.0, Protobuf 6.33.5, and one OpenCV distribution after a local advisory review.

## Architecture assessment

- `faceslim/` now separates runtime, model, pipeline, exporter, UI, localization, and CLI responsibilities while compatibility launchers keep existing commands working.
- Provider selection covers CPU, CUDA, and DirectML with explicit diagnostics and fallback behavior.
- The PyQt interface carries accessible metadata, focus ordering, contrast checks, and pseudo-locale coverage.
- Local tests cover model integrity, CPU warp geometry, providers, manifests, exports, accessibility, compatibility, and setup repair.

## Brand direction

The approved mark is the asymmetric profile contour. It communicates face geometry without using a literal portrait, remains distinct at small sizes, and fits the dark cyan product palette. The symmetric contour study reads too much like an hourglass, while the jawline study loses personality when reduced. The fictional demo portrait remains a supporting evidence asset, not the primary logo.

## Rejected Ideas

- Face swap pipeline parity with Deep-Live-Cam/InsightFace: rejected because it conflicts with FaceSlim's retouch/reshape purpose and increases abuse risk.
- Cloud account sync/subscription features copied from mobile editors: rejected because local privacy is a differentiator.
- Mandatory GFPGAN/CodeFormer restore on every export: rejected because it can change identity and adds heavyweight dependencies; keep optional.
- Immediate 3DMM/DECA implementation: rejected for now because `Roadmap_Blocked.md` already records unresolved model/legal distribution decisions.
- Mobile app rewrite: rejected because current architecture is PyQt/OpenCV desktop/CLI; focus first on distribution quality and local plugin/API integration.

## Sources

Repo and OSS:

- https://github.com/SysAdminDoc/FaceSlim
- https://github.com/facefusion/facefusion
- https://github.com/TencentARC/GFPGAN
- https://github.com/sczhou/CodeFormer
- https://github.com/xinntao/Real-ESRGAN
- https://github.com/ju-leon/RetouchML
- https://github.com/Ivan-Ayub97/Warlock-Studio
- https://github.com/yakhyo/face-parsing
- https://github.com/yakhyo/modnet
- https://github.com/sczhou/Awesome-Face-Restoration

Commercial and integration:

- https://www.facetuneapp.com/
- https://www.perfectcorp.com/consumer/apps/ypc
- https://www.meitu.com/en/
- https://remini.ai/
- https://www.topazlabs.com/topaz-photo-ai
- https://developer.adobe.com/photoshop/uxp/

Standards and platform policy:

- https://c2pa.org/specifications/specifications/2.2/index.html
- https://iptc.org/std/photometadata/specification/IPTC-PhotoMetadata
- https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- https://support.google.com/youtube/answer/14328491

Dependencies and advisories:

- https://ai.google.dev/edge/mediapipe/solutions/vision/face_landmarker/python
- https://github.com/microsoft/onnxruntime/releases
- https://pypi.org/project/onnxruntime/
- https://pypi.org/project/mediapipe/
- https://pypi.org/project/opencv-python/
- https://pypi.org/project/numpy/
- https://devguide.python.org/versions/
- https://osv.dev/
- https://github.com/advisories?query=ecosystem%3Apip

## Open Questions

- Which model licenses and redistribution terms are acceptable for optional restoration/upscale models shipped or downloaded by FaceSlim?
- Should C2PA/IPTC disclosure be opt-out for all exported edits, or tied to the existing optional visual watermark?
