# Khmer Digital Font

**ពុម្ពអក្សរខ្មែរឌីជីថល** — An official Khmer typeface published by the Ministry of Post and Telecommunications of Cambodia.

---

## Overview

Khmer Digital Font is a comprehensive, professionally designed Khmer Unicode typeface released by the **Ministry of Post and Telecommunications of Cambodia (MPTC)**. Built for use in official government documents, digital communications, and public-facing materials, this font brings a modern and authoritative voice to the Khmer script across all media.

The font family ships with **9 weights**, from Thin to Black, giving designers and developers full typographic control for both display and body text contexts.

---

## Font Weights

| Weight | Name        | CSS Value |
|--------|-------------|-----------|
| 100    | Thin        | `font-weight: 100` |
| 200    | ExtraLight  | `font-weight: 200` |
| 300    | Light       | `font-weight: 300` |
| 400    | Regular     | `font-weight: 400` |
| 500    | Medium      | `font-weight: 500` |
| 600    | SemiBold    | `font-weight: 600` |
| 700    | Bold        | `font-weight: 700` |
| 800    | ExtraBold   | `font-weight: 800` |
| 900    | Black       | `font-weight: 900` |

---

## Features

- ✅ Full Khmer Unicode support
- ✅ 9 weights for complete typographic range
- ✅ Optimized for official letters, reports, and government documents
- ✅ Suitable for screen and print
- ✅ Web font ready (WOFF2 / TTF)
- ✅ Free and open source under SIL Open Font License 1.1

---

## Usage

### Web (CSS)

```css
@font-face {
  font-family: 'Khmer Digital';
  src: url('fonts/KhmerDigital-Regular.woff2') format('woff2'),
       url('fonts/KhmerDigital-Regular.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
}

@font-face {
  font-family: 'Khmer Digital';
  src: url('fonts/KhmerDigital-Bold.woff2') format('woff2'),
       url('fonts/KhmerDigital-Bold.ttf') format('truetype');
  font-weight: 700;
  font-style: normal;
}

body {
  font-family: 'Khmer Digital', sans-serif;
}
```

### Download & Install

1. Download the latest release from the [Releases](../../releases) page
2. Extract the ZIP file
3. Install the `.ttf` files on your system:
   - **Windows**: Right-click → Install
   - **macOS**: Double-click → Install Font
   - **Linux**: Copy to `~/.fonts/` or `/usr/share/fonts/`

---

## File Structure

```
KhmerDigitalFont/
├── fonts/
│   ├── TTF/
│   │   ├── KhmerDigital-Thin.ttf
│   │   ├── KhmerDigital-ExtraLight.ttf
│   │   ├── KhmerDigital-Light.ttf
│   │   ├── KhmerDigital-Regular.ttf
│   │   ├── KhmerDigital-Medium.ttf
│   │   ├── KhmerDigital-SemiBold.ttf
│   │   ├── KhmerDigital-Bold.ttf
│   │   ├── KhmerDigital-ExtraBold.ttf
│   │   └── KhmerDigital-Black.ttf
│   └── WOFF2/
│       ├── KhmerDigital-Thin.woff2
│       ├── KhmerDigital-ExtraLight.woff2
│       ├── KhmerDigital-Light.woff2
│       ├── KhmerDigital-Regular.woff2
│       ├── KhmerDigital-Medium.woff2
│       ├── KhmerDigital-SemiBold.woff2
│       ├── KhmerDigital-Bold.woff2
│       ├── KhmerDigital-ExtraBold.woff2
│       └── KhmerDigital-Black.woff2
├── LICENSE.txt
└── README.md
```

---

## License

This font is licensed under the **SIL Open Font License, Version 1.1**.

> Copyright 2025 The Khmer Digital Font  
> Ministry of Post and Telecommunications of Cambodia

You are free to use, study, modify, and redistribute this font, including in commercial software, as long as:
- The font is not sold by itself
- The license is distributed with any copy
- Modified versions do not use the Reserved Font Name

See [LICENSE.txt](LICENSE.txt) for the full license text, or visit [openfontlicense.org](https://openfontlicense.org).

---

## Contributing

Contributions and improvements are welcome. Please open an issue or submit a pull request.

For major changes — such as new glyph coverage or weight additions — please open an issue first to discuss.

---

## Credits
Editor: Mok Rady, Pot Semtararath, Suon Pisey  
Designed by Danh Hong (NextOCR - https://nextocr.org)  
Published by the  
**Ministry of Post and Telecommunications of Cambodia (MPTC)**  
🌐 [https://www.mptc.gov.kh](https://www.mptc.gov.kh)

---

*Preserving and advancing the Khmer script in the digital age.*
