Pyfixtures
============================================

Pytest style fixtures without pytest.

.. code-block:: python

    import asyncio
    from pathlib import Path
    from pyfixtures import fixture, FixtureScope

    @fixture
    def tmpdir() -> path:
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

.. toctree::
    :hidden:

    plugin.rst
    contributing.rst
