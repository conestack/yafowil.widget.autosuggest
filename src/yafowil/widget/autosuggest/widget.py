from yafowil.base import factory
from yafowil.common import generic_extractor, input_generic_renderer
from yafowil.utils import managedprops


@managedprops('source', 'delay', 'minLength')
def autosuggest_renderer(widget, data):
    result = data.rendered
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

    result += tag('div', source,
                  **{'data-source-type': source_type,
                     'data-source': source,
                     'data-delay': widget.attrs['delay'],
                     'data-minLength': widget.attrs['minLength'],
                    })

    return tag


def autosuggest_extractor(widget, data):
    return data.extracted


factory.register(
    'autosuggest',
    extractors=[generic_extractor, autosuggest_extractor],
    edit_renderers=[input_generic_renderer, autosuggest_renderer])

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

factory.register_plan('autosuggestfield',
                      ['field', 'label', 'error', 'autosuggest'], {})
