import win32gui
import win32con
import time

# Step 1: List all active windows
def enum_windows():
    window_list = []

    def callback(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
            window_list.append((hwnd, win32gui.GetWindowText(hwnd)))

    win32gui.EnumWindows(callback, None)
    return window_list

# Step 2: Display window options and let the user choose
def select_window():
    print("\nSelect the window to keep always on top:")
    windows = enum_windows()
    for i, (hwnd, title) in enumerate(windows):
        print(f"{i + 1}: {title}")

    while True:
        try:
            choice = int(input("\nEnter the number corresponding to the window: "))
            if 1 <= choice <= len(windows):
                return windows[choice - 1][0]  # Return the hwnd of the selected window
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Step 3: Keep the window always on top
def keep_window_on_top(hwnd):
    print("\nLocking the selected window as always on top...")
    try:
        # Set the window to always stay on top
        win32gui.SetWindowPos(
            hwnd,
            win32con.HWND_TOPMOST,  # Always on top
            0, 0, 0, 0,            # No position or size change
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW
        )
        print("The window has been locked as always on top.")
    except Exception as e:
        print(f"Error locking window: {e}")

    # Keep the window on top in a loop
    try:
        while True:
            if not win32gui.IsWindow(hwnd):
                print("\nThe selected window has been closed or minimized. Exiting.")
                break

            win32gui.SetWindowPos(
                hwnd,
                win32con.HWND_TOPMOST,  # Keep it always on top
                0, 0, 0, 0,
                win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW
            )
            time.sleep(0.5)  # Check every half second
    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting.")

# Main execution
if __name__ == "__main__":
    print("Dynamic Prime Window Lock App")
    hwnd = select_window()

    if hwnd:
        keep_window_on_top(hwnd)
