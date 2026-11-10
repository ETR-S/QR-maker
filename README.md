# QR-maker
it makes a QR code to any link you want and there's an option to save it on the desktop

## Save confirmation

Enter *y* to show and save the QR code, or *n* to show it without saving.

Uppercase letters and surrounding spaces are also accepted. For example, ` Y ` works just like `y`.

## Manual testing

- ` Y `: should show and save the QR code.
- ` N `: should show the QR code without saving.
- `y`: should show and save the QR code.
- `n`: should show the QR code without saving.

Actual results: all four checks passed

## How to run

1. Open `qr.py` 
2. Install `qrcode` and `Pillow` in the project's Python interpreter.
3. If using another computer, change the `path` value to your own Desktop location, keeping `qrcode.png` as the filename.
4. run `qr.py`.
5. Enter a link.
6. Enter `y` to display and save the QR code, or `n` to display it without saving.
