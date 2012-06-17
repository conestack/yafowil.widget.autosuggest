/*
 * yafowil autosuggest widget
 *
 * Optional: bdajax
 */

if (typeof(window['yafowil']) == "undefined") yafowil = {};

(function($) {

    $(document).ready(function() {
        // initial binding
        yafowil.autosuggest.binder();

        // add after ajax binding if bdajax present
        if (typeof(window['bdajax']) != "undefined") {
            $.extend(bdajax.binders, {
                autosuggest_binder: yafowil.autosuggest.binder
            });
        }
    });

    $.extend(yafowil, {
        autosuggest: {
            binder: function(context) {
                $('.autosuggest', context).each(function(event) {
                    var id = $(this).attr('id');
                    var element = $('#' + id);
                });
            }
        }
    });

})(jQuery);
