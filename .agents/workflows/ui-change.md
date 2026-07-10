# UI Change Workflow

Use this for styling, layout, visual hierarchy, copy placement, accessibility, responsive behavior, and local interaction changes.

## Routing Gate

- If the change affects business rules, permissions, API contracts, persisted data, uploads, status behavior, or multiple independently delivered clients, use `module-delivery.md`.
- A narrow visual change may proceed after scope and verification are defined.
- A broad redesign, navigation change, or design-system change requires option comparison and explicit approval.

## Define Scope

| Item | Content |
| --- | --- |
| Page or component | `<LOCATION>` |
| Viewports or devices | `<TARGETS>` |
| User-visible goal | `<GOAL>` |
| Existing design conventions | `<DESIGN_SYSTEM_OR_PATTERNS>` |
| Behavior that must not change | `<NON_GOALS>` |
| Completion criteria | `<VISUAL_AND_INTERACTION_CRITERIA>` |

## Review Before Editing

- Loading, empty, error, disabled, read-only, and permission-denied states.
- Text expansion, localization, overflow, zoom, and responsive breakpoints.
- Keyboard navigation, focus order, labels, contrast, and motion preferences.
- Touch targets, hover/focus/active states, and destructive-action confirmation.
- Reused components and downstream screens.

## Verification

- Run the relevant static check and build from `../project/commands.md`.
- Inspect the changed UI at agreed viewports and interaction states.
- Prefer browser, simulator, device, or screenshot evidence for significant changes.
- Compare against the agreed design source when one exists.
- Report unverified visual states explicitly.

## Delivery

State what changed visually, what behavior remained unchanged, what was verified, compatibility compromises, and intentional non-goals.
