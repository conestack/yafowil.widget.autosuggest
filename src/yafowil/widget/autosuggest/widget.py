from yafowil.base import factory
from yafowil.common import generic_extractor, input_attributes_common
from yafowil.utils import managedprops


@managedprops('source', 'delay', 'minLength')
def autosuggest_renderer(widget, data):
    tag = data.tag
    source = widget.attrs['source']
    if callable(source):
        source = source(widget, data)
    if isinstance(source, (list, tuple)):
        source = '|'.join(source)
        source_type = 'local'
    elif isinstance(source, basestring):
        source_type = 'remote'
    else:
        raise ValueError, 'resulting source must be tuple/list or string'

    attrs = input_attributes_common(widget, data)
    attrs.update({'data-source-type': source_type,
                  'data-source': source,
                  'data-delay': widget.attrs['delay'],
                  'data-minLength': widget.attrs['minLength']
                 })
    attrs['type'] = 'text'
    return tag('input', **attrs)


def autosuggest_extractor(widget, data):
    return data.extracted


factory.register(
    'autosuggest',
    extractors=[generic_extractor, autosuggest_extractor],
    edit_renderers=[autosuggest_renderer])

factory.doc['blueprint']['autosuggest'] = \
"""Add-on blueprint `yafowil.widget.autosuggest
<http://github.com/bluedynamics/yafowil.widget.autosuggest/>`_ utilizing
`jquery autosuggest <https://github.com/wuyuntao/jquery-autosuggest/>`_ to
offer the user a selection based on the input given so far.
"""

factory.defaults['autosuggest.class'] = 'autosuggest'
factory.defaults['autosuggest.type'] = 'text'
factory.defaults['autosuggest.required_class'] = 'required'
factory.defaults['autosuggest.delay'] = '300' #ms
factory.defaults['autosuggest.minLength'] = '1' #characters
factory.defaults['autosuggest.disabled'] = False
factory.defaults['autosuggest.size'] = None
factory.defaults['autosuggest.source'] = None
factory.defaults['autosuggest.autocomplete'] = 'autocomplete'

factory.register_plan('autosuggestfield',
                      ['field', 'label', 'error', 'autosuggest'], {})
