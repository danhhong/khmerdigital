# Khmer Digital Font Usage Guidelines

ពុម្ពអក្សរខ្មែរឌីជីថល — Khmer Digital Typeface

---

## 1. Overview

Khmer Digital is the official Khmer Unicode typeface of the Ministry of Post and Telecommunications of Cambodia (MPTC). It is the standard font for digital government, enterprise systems and public services, and it works on screen and in print.

The typeface is released as two families:

| Family | Styles | Purpose |
|--------|--------|---------|
| **Khmer Digital** | 9 weights, Thin (100) to Black (900) | Everyday text: documents, websites, apps, interfaces and print |
| **Khmer Digital Max** | 1 style (Regular) | Inscription and carved-lettering contexts |

Use **Khmer Digital** for almost everything. Use **Khmer Digital Max** only where the text is inscribed, engraved, carved or presented in that style.

---

## 2. Supported Platforms

- Windows
- macOS
- Linux
- Web (CSS `@font-face`)
- Microsoft 365 applications (Word, Excel, PowerPoint, Teams, SharePoint)

---

## 3. Khmer Digital (Text Family)

### 3.1 Weights

| Weight | Name       | File                          | CSS                |
|--------|------------|-------------------------------|--------------------|
| 100    | Thin       | `KhmerDigital-Thin.ttf`       | `font-weight: 100` |
| 200    | ExtraLight | `KhmerDigital-ExtraLight.ttf` | `font-weight: 200` |
| 300    | Light      | `KhmerDigital-Light.ttf`      | `font-weight: 300` |
| 400    | Regular    | `KhmerDigital-Regular.ttf`    | `font-weight: 400` |
| 500    | Medium     | `KhmerDigital-Medium.ttf`     | `font-weight: 500` |
| 600    | SemiBold   | `KhmerDigital-SemiBold.ttf`   | `font-weight: 600` |
| 700    | Bold       | `KhmerDigital-Bold.ttf`       | `font-weight: 700` |
| 800    | ExtraBold  | `KhmerDigital-ExtraBold.ttf`  | `font-weight: 800` |
| 900    | Black      | `KhmerDigital-Black.ttf`      | `font-weight: 900` |

### 3.2 Recommended Use

| Use case | Recommended weight |
|----------|--------------------|
| Body text, official letters and reports | Regular (400) |
| Emphasis within text | Bold (700) |
| User interface: buttons, menus, labels, navigation | Medium (500) or SemiBold (600) |
| Headings and titles | SemiBold (600) or Bold (700) |
| Large display text, banners, posters | ExtraBold (800) or Black (900) |
| Large decorative or display text only | Thin (100) to Light (300) |

### 3.3 Good Practice

- Do not use Thin, ExtraLight or Light for body text or small sizes; the strokes become too faint to read, especially on screen.
- Use no more than two or three weights in one document or interface.
- Keep body text at a comfortable size: about 12 pt in print and 16 px on screen. Khmer subscripts and vowel signs need room, so avoid very tight line spacing (a line height of 1.5 or more is recommended for body text).

---

## 4. Khmer Digital Max (Inscription Family)

### 4.1 Purpose

Khmer Digital Max is a single-style companion family intended for **inscription and carved-lettering contexts**. Its letterforms are suited to text that is cut, engraved, etched or cast into a surface, or designed to look that way.

| Property | Value |
|----------|-------|
| Family name | Khmer Digital Max |
| Style | Regular |
| Weight | 400 |
| File | `KhmerDigital-Max.ttf` |

Because it is a separate family, select it by name ("Khmer Digital Max") in the font menu or in CSS, not as a weight of Khmer Digital.

### 4.2 Appropriate Uses

- Foundation stones, plaques and commemorative inscriptions
- Engraved or etched signage on stone, metal, wood or glass
- Monuments, memorials and building name inscriptions
- Awards, trophies, medals and certificates styled as inscriptions
- Seals, stamps and laser-cut or CNC-cut lettering

### 4.3 Not Recommended

- Body text, long paragraphs or official correspondence; use Khmer Digital Regular instead
- User interfaces, forms, tables and small text on screen
- Mixing with Khmer Digital weights in the same line or heading

### 4.4 Character Coverage

Khmer Digital Max covers the core Khmer alphabet, vowels, signs, digits and basic Latin. It does **not** include:

- Khmer divination numerals (U+17F0–U+17F9)
- The Khmer Symbols block, including lunar date symbols (U+19E0–U+19FF)
- Curly quotation marks “ ” (U+201C, U+201D); use straight quotes or set them in Khmer Digital

If your inscription needs any of these characters, set the text in Khmer Digital instead.

### 4.5 Production Tips

- Proof the text at full size on the actual material before cutting or engraving; fine details in subscripts and vowel signs must survive the cutting tool.
- Give the lettering generous letter and line spacing so the stacked parts of Khmer clusters do not run into each other on the surface.
- Convert text to outlines only in the final production file, and keep an editable copy for corrections.

---

## 5. Installation

### Desktop

| Platform | Steps |
|----------|-------|
| Windows | Right-click each `.ttf` file → **Install** (or **Install for all users**) |
| macOS | Double-click each `.ttf` file → **Install Font** |
| Linux | Copy files and refresh the font cache (see below) |

```bash
mkdir -p ~/.local/share/fonts
cp KhmerDigital-*.ttf ~/.local/share/fonts/
fc-cache -fv
```

Install `KhmerDigital-Max.ttf` together with the other files if you need the inscription family. It appears in font menus as **Khmer Digital Max**.

### Web

```css
/* Text family (repeat for each weight you use) */
@font-face {
  font-family: "Khmer Digital";
  src: url("fonts/KhmerDigital-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Khmer Digital";
  src: url("fonts/KhmerDigital-Bold.woff2") format("woff2");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

/* Inscription family */
@font-face {
  font-family: "Khmer Digital Max";
  src: url("fonts/KhmerDigital-Max.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

body {
  font-family: "Khmer Digital", sans-serif;
  font-weight: 400;
  line-height: 1.6;
}

.inscription {
  font-family: "Khmer Digital Max", "Khmer Digital", serif;
}
```

Load only the weights you use, to keep pages fast. If you only have the `.ttf` files, convert them to WOFF2 first (for example with `fonttools ttLib.woff2 compress KhmerDigital-Regular.ttf`).

---

## 6. Quick Reference

| I need to… | Use |
|------------|-----|
| Write a letter, report or document | Khmer Digital Regular, with Bold for emphasis |
| Build an app or website interface | Khmer Digital Regular for text, Medium or SemiBold for UI |
| Design a poster or banner headline | Khmer Digital Bold, ExtraBold or Black |
| Engrave a plaque, foundation stone or monument | Khmer Digital Max |

---

## 7. Licensing

Both Khmer Digital and Khmer Digital Max are licensed under the **SIL Open Font License 1.1**. You may use, share, embed and modify the fonts, including for commercial work, under the terms of the license. See [`ofl/khmerdigital/OFL.txt`](../ofl/khmerdigital/OFL.txt) for the full text.
