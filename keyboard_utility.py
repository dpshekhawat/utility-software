import infi.systray
import keyboard
from threading import Thread


class KeyboardBlocker:
    def __init__(self):
        self.blocked = False
        self.blocked_icon = "icons\mouse.ico"
        self.unblocked_icon = "icons\keyboard.ico"

    def block_keyboard(self):
        self.blocked = True
        for i in range(150):
            keyboard.block_key(i)

    def unblock_keyboard(self, icon, *args):
        self.blocked = False
        for i in range(150):
            keyboard.unblock_key(i)
        icon.update(icon=self.unblocked_icon, hover_text="Keyboard unblocked")

    def toggle_keyboard_block(self, icon):
        if self.blocked:
            self.unblock_keyboard(icon)
            icon.update(icon=self.unblocked_icon, hover_text="Keyboard unblocked")
        else:
            self.block_keyboard()
            icon.update(icon=self.blocked_icon, hover_text="Keyboard blocked")

    def on_quit(self, icon):
        pass  # Do nothing here

    def get_menu_options(self):
        return (
            ("Block Keyboard", None, self.toggle_keyboard_block),
            ("Unblock Keyboard", None, self.unblock_keyboard),
        )

    def run(self):
        infi.systray.SysTrayIcon(
            self.unblocked_icon,
            "Keyboard unblocked",
            self.get_menu_options(),
            on_quit=self.on_quit,
        ).start()


if __name__ == "__main__":
    kb_blocker = KeyboardBlocker()
    t = Thread(target=kb_blocker.run)
    t.start()
    t.join()  # Wait for the thread to finish before exiting
