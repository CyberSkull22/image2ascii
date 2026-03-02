# Image to ASCII (Browser-Only)

Convert any image into ASCII art directly in the browser.

No backend, no dependencies, no build step.

## Features

- Client-side conversion (works with Live Server and static hosting)
- Adjustable ASCII width (`20` to `600`)
- Instant preview of selected image
- Copy result to clipboard
- Download result as `ascii.txt`
- Responsive UI (desktop + mobile)

## Demo / Local run

This project is static HTML/CSS/JS.

1. Open `index.html` directly in your browser
2. Or run with VS Code Live Server

No Python server is required.

## Project Structure

```text
.
|-- index.html
|-- README.md
`-- .gitignore
```

## Deploy on GitHub Pages

1. Push this repository to GitHub
2. Go to `Settings` -> `Pages`
3. In `Build and deployment`, choose:
   - `Source`: `Deploy from a branch`
   - `Branch`: `main` and `/ (root)`
4. Save and wait a few seconds

Your app will be available at:

`https://<your-username>.github.io/<your-repo>/`

## Notes

- Clipboard copy may be blocked by some browsers if the page is not in a secure context.
- Very large output widths can take longer to process in the browser.



