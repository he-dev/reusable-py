import win32com.client
import contextlib

import win32com.client as com


class Excel(contextlib.AbstractContextManager):

    def __enter__(self) -> win32com.client.CDispatch:
        self.app = com.Dispatch("Excel.Application")
        self.app.Visible = False
        self.app.DisplayAlerts = False
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.app:
            self.app.Quit()
