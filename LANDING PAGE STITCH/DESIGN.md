---
name: Alarcom Premium Security
colors:
  surface: '#061520'
  surface-dim: '#061520'
  surface-bright: '#2c3b47'
  surface-container-lowest: '#020f1b'
  surface-container-low: '#0e1d29'
  surface-container: '#12212d'
  surface-container-high: '#1d2b38'
  surface-container-highest: '#283643'
  on-surface: '#d5e4f5'
  on-surface-variant: '#c4c6cd'
  inverse-surface: '#d5e4f5'
  inverse-on-surface: '#24323e'
  outline: '#8e9197'
  outline-variant: '#44474c'
  surface-tint: '#b9c7df'
  primary: '#b9c7df'
  on-primary: '#233143'
  primary-container: '#0b1a2b'
  on-primary-container: '#758398'
  inverse-primary: '#515f73'
  secondary: '#83d0f7'
  on-secondary: '#003548'
  secondary-container: '#006b8e'
  on-secondary-container: '#bce6ff'
  tertiary: '#5ad7e6'
  on-tertiary: '#00363c'
  tertiary-container: '#001d20'
  on-tertiary-container: '#00909c'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d5e3fb'
  primary-fixed-dim: '#b9c7df'
  on-primary-fixed: '#0e1c2d'
  on-primary-fixed-variant: '#3a485b'
  secondary-fixed: '#c1e8ff'
  secondary-fixed-dim: '#83d0f7'
  on-secondary-fixed: '#001e2b'
  on-secondary-fixed-variant: '#004d67'
  tertiary-fixed: '#8cf2ff'
  tertiary-fixed-dim: '#5ad7e6'
  on-tertiary-fixed: '#001f23'
  on-tertiary-fixed-variant: '#004f56'
  background: '#061520'
  on-background: '#d5e4f5'
  surface-variant: '#283643'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  title-sm:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  mono-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
---

## Brand & Style

This design system is engineered for high-stakes B2B environments including industrial sectors, logistics, and government infrastructure. The visual identity balances unyielding security with cutting-edge technological sophistication.

The style is **Modern Corporate** with a heavy influence of **Subtle Glassmorphism**. It evokes a sense of "digital armor"—protective, transparent where necessary, and technologically superior. Surfaces use deep navy foundations with translucent overlays to create a multi-layered interface that feels like a high-end command center. The emotional response is one of absolute reliability, precision, and forward-thinking intelligence.

## Colors

The palette is anchored in **Deep Navy (#0B1A2B)** to establish authority and stability. **Tech Blue (#006C8F)** and **Teal (#00A6B4)** are used for data visualization and interactive states, representing connectivity and intelligence.

**Amber/Orange (#F4A340)** serves as the high-visibility accent for critical calls to action, alerts, and active status indicators. This color should be used sparingly to maintain its psychological impact. For backgrounds, while the primary mode is dark, **Cold White (#F5F8FA)** is utilized for high-legibility document views or secondary light-mode interfaces. **Steel Gray (#8A99A8)** provides the necessary neutral bridge for borders and secondary text.

## Typography

The typography strategy employs a dual-font approach to separate content from technical data. 

**Space Grotesk** is used for headlines, display text, and technical labels. Its geometric nature reflects the hardware and engineering precision of electronic security. **Inter** is the workhorse for all body copy and user input, chosen for its exceptional legibility in data-dense dashboards. 

Use uppercase styling for labels and technical identifiers to reinforce the professional, institutional character of the system.

## Layout & Spacing

The layout follows a **Fluid Grid** model based on an 8px rhythmic scale. For desktop enterprise applications, use a 12-column grid with 24px gutters to allow for complex data densities. 

- **Desktop:** 12 columns, 48px side margins.
- **Tablet:** 8 columns, 32px side margins.
- **Mobile:** 4 columns, 16px side margins.

Information density should be high but organized. Use "Safe Zones" of 40px (lg spacing) between major functional blocks to prevent cognitive overload in critical monitoring situations.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Subtle Glassmorphism**. 

1.  **Level 0 (Base):** Deep Navy (#0B1A2B).
2.  **Level 1 (Cards/Panels):** A semi-transparent overlay (White at 5% opacity) with a 16px Backdrop Blur. This creates the "glass" effect.
3.  **Level 2 (Modals/Popovers):** Higher opacity (White at 10%) with a soft, expansive shadow: `0 20px 40px rgba(0,0,0,0.4)`.

Borders on glass elements should be 1px solid, using a gradient from White (20% opacity) to White (5% opacity) to simulate a light-catching edge.

## Shapes

The design system uses **Rounded (0.5rem)** corners as the standard. This softens the industrial nature of the brand while maintaining a professional, structured look. 

- **Standard Buttons & Inputs:** 8px (0.5rem)
- **Large Containers/Cards:** 16px (1rem)
- **Status Tags/Chips:** Full pill-shaped for immediate recognition.

Avoid sharp corners to differentiate from legacy "brutalist" industrial software, opting instead for a modern, refined tech aesthetic.

## Components

### Buttons
- **Primary:** Amber (#F4A340) background, Navy text. High contrast for critical actions.
- **Secondary:** Tech Blue (#006C8F) stroke with subtle fill.
- **Ghost/Tertiary:** Transparent with Teal text.

### Inputs
Fields should use a dark semi-transparent fill (Glass effect) with a Steel Gray border. On focus, the border transitions to Tech Blue with a subtle outer glow. Labels use Space Grotesk in uppercase.

### Cards & Panels
Cards must feature the 16px Backdrop Blur and the 1px gradient border. Titles within cards should be Space Grotesk Semi-Bold.

### Status Indicators
- **Active/Secure:** Teal (#00A6B4)
- **Alert/Warning:** Amber (#F4A340)
- **Critical/Breach:** System Red (Standard utility color)

### Data Visualization
Use Teal and Tech Blue for primary data streams. Use light Steel Gray for grid lines and secondary axes to keep the focus on the data itself.