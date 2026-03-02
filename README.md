# Image to ASCII

Convert images to ASCII art using either:

- a browser interface (`index.html`)
- a terminal CLI (`main.py`)

## Features

- Browser app: local conversion, no backend required
- Terminal CLI: fast conversion from image to terminal/text file
- Adjustable width (`20` to `600`)
- Custom character set support in CLI
- Copy/download support in browser UI

## Example                                                                                                                                                                                                                                                             
```text
.@@@.  @@@. .@@@. .@@@@..@@@@@@@@@..%@@@@@@..@@@.  %@@.. %@@@@@@@.   -@@@@@@.. .%@@@@@%. .@@@@@@%.  
.=@@.  @@@=..@@@..%@@@@:.  .@@@.  .@@@..:@@@.@@@   %@@.. %@@...@@@=.%@@-..@@@..@@@.. @@@.@@@...@@@  
..@@+.=@@@@..@@...@@=@@@.  .@@@.  .@@%. .@@@.@@@...%@@.. %@@. ..@@@.@@@.. .@@@.@@@.  ....@@@.. .....
  .@@-.@@-@@.@@@..@@@.@@@..  @@@   @@@.       @@@@@@@@@.  @@@   .@@#.@@=. .*@@:@@@ .......@@@@@@... 
   @@@@@*.@@@@@.@@@@. .@@+.  @@@   @*..  .....@@*..:-@@.  @@@   .@@# @:...@@@@:@@@..@@@@@. %@@@@:...
  .*@@@@..@@@....@@@@@@@@%.  @@@  .@@@.  .@@@.@@*...@@@ ..@@@.. -@@-.@@*. .%@@.@@@. ..@@@*%%....@@@ 
  .@@@@...@@@@..@@@....@@...@@@.  :@@@...@@..#@@...%@@...%@@...@@=..%@@-..@@@..@@@...@@:.@@ ...@@@. 
   -@@@.  @@@@.%@@=.  .@@@..@@-.   .*@@@@@#..@@@.  %@@.. %@@@@@@@. ...:@@@@@.. ..@@@@+@@..=@@@@@@   
                                       . .                             .....     . .       .. ..    
 ```                 

## Project Structure

```text
.
|-- index.html
|-- main.py
|-- requirements.txt
|-- README.md
|-- LICENSE
`-- .gitignore
```

## Browser Usage

1. Open `index.html` directly in your browser
2. Or run with VS Code Live Server
3. Select an image, choose width, click `Convert to ASCII`

The conversion is client-side and works on static hosting (including GitHub Pages).

## Terminal Usage

### 1. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 2. Run conversion

```bash
python main.py path/to/image.jpg
```

### Useful options

```bash
python main.py path/to/image.jpg -w 160
python main.py path/to/image.jpg -o ascii.txt
python main.py path/to/image.jpg --charset " .:-=+*#%@"
python main.py path/to/image.jpg --invert
```

## CLI Arguments

- `input`: path to source image (required)
- `-w, --width`: output width in characters (default: `120`)
- `-o, --output`: save ASCII output to file instead of printing
- `--charset`: characters ordered from dark to light
- `--invert`: reverse brightness mapping

## Deploy Web Version on GitHub Pages

1. Push repository to GitHub
2. Go to `Settings` -> `Pages`
3. Set `Source` to `Deploy from a branch`
4. Select `main` branch and `/ (root)`
5. Save

Site URL format:

`https://<your-username>.github.io/<your-repo>/`

## Notes

- Very large widths can produce huge outputs.
- Clipboard API in browser may require a secure context depending on browser rules.

## License

MIT
