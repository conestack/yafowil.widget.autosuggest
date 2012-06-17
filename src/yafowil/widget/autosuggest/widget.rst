autosuggest widget
================

Features
--------

    - renders textarea with autosuggest css class and provides a autosuggest
      resources.

Load requirements::

    >>> import yafowil.loader
    >>> import yafowil.widget.autosuggest

Test widget::

    >>> from yafowil.base import factory

Render widget::

    >>> widget = factory('autosuggest', 'rt', props={'required': True})
    >>> widget()
    u'<textarea class="autosuggest" cols="80" id="input-rt" name="rt" required="required" rows="10"></textarea>'

Widget extraction::

    >>> request = {'rt': ''}
    >>> data = widget.extract(request)

No input was given::

    >>> data.errors
    [ExtractionError('Mandatory field was empty',)]

Empty string in extracted::

    >>> data.extracted
    ''

Widget extraction. Returns markup from tinymce::

    >>> request = {'rt': '<p>1</p>'}
    >>> data = widget.extract(request)
    >>> data.errors
    []

    >>> data.extracted
    '<p>1</p>'

    >>> widget(data)
    u'<textarea class="autosuggest" cols="80" id="input-rt" name="rt" required="required" rows="10"><p>1</p></textarea>'

Display renderer::

    >>> widget = factory('autosuggest', 'rt', value='<p>foo</p>', mode='display')
    >>> widget()
    u'<div class="display-autosuggest"><p>foo</p></div>'

    >>> widget = factory('autosuggest', 'rt', mode='display')
    >>> widget()
    u'<div class="display-autosuggest"></div>'
