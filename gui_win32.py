import win32api
import win32con
import win32gui


def main():
    # get instance handle
    hInstance = win32api.GetModuleHandle()

    # the class name
    className = 'SimpleWin32'

    # create and initialize window class
    wndClass = win32gui.WNDCLASS()
    wndClass.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
    wndClass.lpfnWndProc = wndProc
    wndClass.hInstance = hInstance
    wndClass.hIcon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
    wndClass.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
    wndClass.hbrBackground = win32gui.GetStockObject(win32con.WHITE_BRUSH)
    wndClass.lpszClassName = className

    # register window class
    wndClassAtom = None
    try:
        wndClassAtom = win32gui.RegisterClass(wndClass)
    except:
        pass

    hWindow = win32gui.CreateWindow(
        wndClassAtom,  # it seems message dispatching only works with the atom, not the class name
        'Python Win32 Window',
        win32con.WS_OVERLAPPEDWINDOW,
        win32con.CW_USEDEFAULT,
        win32con.CW_USEDEFAULT,
        win32con.CW_USEDEFAULT,
        win32con.CW_USEDEFAULT,
        0,
        0,
        hInstance,
        None)

    # Show & update the window
    win32gui.ShowWindow(hWindow, win32con.SW_SHOWNORMAL)
    win32gui.UpdateWindow(hWindow)

    # Dispatch messages
    win32gui.PumpMessages()


def wndProc(hWnd, message, wParam, lParam):
    print(hWnd)
    if message == win32con.WM_PAINT:
        hDC, paintStruct = win32gui.BeginPaint(hWnd)

        rect = win32gui.GetClientRect(hWnd)
        win32gui.DrawText(
            hDC,
            'Hello send by Python via Win32!',
            -1,
            rect,
            0 | 0 | 0)
        win32gui.DrawText(
            hDC,
            'Hello!',
            -1,
            rect,
            100 | 0 | 0 | 0)
        #win32gui.FindWindowEx(hDC, None, 'Button', None)
        """
        win32gui.DrawText(
            hDC,
            'Hello!',
            -1,
            rect,
            100 | 0 | 0 | 0
        )
        """
        button = CreateWindowW("BUTTON", "\u27F3",
        WS_TABSTOP|WS_VISIBLE|WS_CHILD|BS_PUSHBUTTON, size - 105,
        size - 29, 100, 24, hwnd, None,
        None, None)
        win32gui.EndPaint(hWnd, paintStruct)
        return 0

    elif message == win32con.WM_DESTROY:
        print('Being destroyed')
        win32gui.PostQuitMessage(0)
        return 0

    else:
        return win32gui.DefWindowProc(hWnd, message, wParam, lParam)


if __name__ == '__main__':
    main()
