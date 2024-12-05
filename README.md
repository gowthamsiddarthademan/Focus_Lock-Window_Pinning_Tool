# Focus Lock : Window Pinning Tool 

**Focus Lock** is a Python-based utility designed to keep a selected window always on top of other applications. This tool is similar to **DeskPins**, offering a programmatic solution for maintaining focus on a specific window, ensuring it remains visible and accessible even when switching between tasks.  

---

## Features  
Focus Lock is a lightweight and efficient tool packed with the following features:  
- **Dynamic Window Selection:** Detects all active windows and allows the user to select one to lock on top.  
- **Always-on-Top Functionality:** Keeps the selected window on top of all other windows, ensuring it remains visible at all times.  
- **User-Friendly Interface:** Simplifies window selection with a numbered list of active windows.  
- **Customizable and Lightweight:** Developed using Python, Focus Lock is highly customizable for developers and doesn’t consume significant system resources.  
- **DeskPins-Like Functionality:** Similar to DeskPins but implemented as a Python script, making it more adaptable and tailored to specific needs.  

---

## How It Works  
1. **Window Detection:** The script identifies all active windows running on the system.  
2. **User Selection:** The user selects the desired window from the list provided by the script.  
3. **Always-on-Top Implementation:** The selected window is locked in the foreground using the `pywin32` library, ensuring it stays on top of other windows.  

---

## Step-by-Step Guide  

### Prerequisites  
- Python (version 3.7 or above) installed on your system.  
- The `pywin32` library installed in your Python environment:  
  ```bash  
  pip install pywin32  
  ```  

---

### Running the Script  
1. Save the **Focus Lock** Python script (e.g., `focus_lock.py`) to a directory of your choice.  
2. Open a terminal or command prompt, navigate to the script's directory, and run:  
   ```bash  
   python focus_lock.py  
   ```  
3. Follow the instructions to select the window you want to keep always on top.  

---

## Creating an Executable File  

To make Focus Lock accessible without requiring Python installation, you can convert it into a standalone executable file using **PyInstaller**.  

### Steps to Convert the Script to an Executable  
1. **Install PyInstaller:**  
   Run the following command in your terminal:  
   ```bash  
   pip install pyinstaller  
   ```  

2. **Navigate to the Script Directory:**  
   Move to the folder containing the `focus_lock.py` script:  
   ```bash  
   cd C:\path\to\your\script  
   ```  

3. **Generate the Executable:**  
   Run the PyInstaller command:  
   ```bash  
   python -m PyInstaller --onefile focus_lock.py  
   ```  
   - The `--onefile` option ensures all dependencies are bundled into a single executable file.  

4. **Locate the Executable:**  
   After the build process completes, find the `.exe` file in the `dist` folder inside your script’s directory.  

5. **Run the Executable:**  
   Open the `dist` folder and double-click the `.exe` file, or run it via the terminal:  
   ```bash  
   cd dist  
   focus_lock.exe  
   ```  

---

## Additional Notes  
- **Error Handling:** The script dynamically checks the status of the selected window. If the window is closed, it gracefully exits without affecting your system.  
- **System Requirements:** Focus Lock is compatible with Windows operating systems and requires administrative privileges for certain functionalities.

---
## Any Enquiry..... 
- You can reach out in my E-Mail and Instagram
- gowthammsiddarthademan@gmail.com
- IG:@gowthamsiddarthademan
---

## Conclusion  
**Focus Lock** provides a simple, effective, and customizable solution for maintaining focus on critical tasks. By following the steps outlined above, you can easily run the script or create a standalone executable for convenient use. This lightweight tool serves as a reliable alternative to DeskPins, empowering users to manage their workspace efficiently.  
