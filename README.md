# Fixtures

[Pytest](https://docs.pytest.org/en/7.1.x/) style [fixtures](https://docs.pytest.org/en/6.2.x/fixture.html) outside of Pytest.

```python
import asyncio
from pathlib import Path
from py_fixtures import fixture, FixtureScope

@fixture
def tmpdir() -> Path:
    path = Path("temp")
    path.mkdir()
    try:
        yield path
    finally:
        path.unlink()



def mk_temp_files(tmpdir: Path):
    tmp_file = tmpdir/"tempfile.txt"
    tmp_file.touch()


async def main():
    async with FixtureScope() as scope:
        operation = await scope.bind(mk_temp_files)
        await operation()


asyncio.run(main())

```
