import os
import tempfile
import contextlib
from pathlib import Path
from typing import Callable, Iterator, Optional


@contextlib.contextmanager
def temp_file(name: Optional[str] = None, ext: Optional[str] = ".tmp", create=True, delete=True) -> Iterator[str]:
    path = Path(tempfile.gettempdir()) / f"{name or os.urandom(4).hex()}{ext}"
    if create and not path.is_file():
        # Create the file and close the handle to release it.
        with path.open("x"):
            pass
    yield str(path)
    if delete and path.is_file():
        path.unlink()
