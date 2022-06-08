Autofixture Sphinx Plugin
*************************

The `pyfixtures.sphinx.ext.autofixture` plugin extends `Sphinx Autodoc
<https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_ to
render fixture functions differently than standard python functions.

The standard `.. autofunction::` directive renders functions like this:

.. automodule:: showcase

.. autofunction:: this_is_a_normal_function

The `.. autofixture::` will render fixture functions as:

.. autofixture:: this_is_a_fixture

And `async` fixtures as:

.. autofixture:: this_fixture_is_async


Most of the time the arguments of a fixture function are all other fixtures, and
so aren't relevant to the usage of the fixture itself. By default `autofixture`
will replace the argument list by "`...`". Sometimes this behaviour is not
desired, so it is possible to disable this.

.. code-block:: python

    from pyfixtures import fixture

    @fixture(hide_params=False)
    def this_is_a_fixture_with_arguments(a, b = "default_value") -> Any:
        ...

Now the parameter list will be rendered:

.. autofixture:: this_is_a_fixture_with_arguments
