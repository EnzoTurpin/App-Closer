
# Application Closer

This Python script allows you to close a specific application by pressing a designated hotkey. In the current configuration, pressing F1 will close Notepad.

## Prerequisites

Before running this script, ensure you have Python installed on your system and the following Python packages:

- `psutil`
- `keyboard`

You can install these packages using pip:

```bash
pip install psutil keyboard
```

## Installation

To use this script, simply clone the repository or download the `.py` file to your local machine.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script:

```bash
python app_closer.py
```

4. Once the script is running, press the F1 key to close Notepad.
5. To stop the script, press the `Esc` key.

## Customization

To change the application that the script closes or the hotkey that triggers the action, edit the `app_closer.py` file:

- Replace `'notepad.exe'` with the `.exe` name of the application you wish to close.
- Replace `'f1'` with the desired hotkey you want to use for closing the application.

## Warning

Please use this script responsibly. Closing applications abruptly can result in unsaved work being lost.


## Contributions

Contributions are welcome. Please open an issue or pull request if you have suggestions or contributions.

## Contact

If you have any questions or feedback, please open an issue in the repository, and I will get back to you.

## Acknowledgments

This script was created using the `psutil` and `keyboard` libraries. Thank you to the developers and contributors of these libraries.
