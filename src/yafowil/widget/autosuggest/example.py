# -*- coding: utf-8 -*-

from yafowil.base import factory

def get_example():
    part = factory(u'fieldset', name='yafowilwidgetautosuggest')
    part['text'] = factory('field:label:error:autosuggest', props={
        'label': 'Enter some text',
        'source': sorted((u'Weißburgunder', u'Welschriesling',
                          u'Sauvingnon Blanc', u'Sämling', u'Scheurebe',
                          u'Traminer', u'Morrilon', u'Muskateller'))})
    return [{'widget': part, 'doc': 'TODO'}]
