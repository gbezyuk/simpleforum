/*
 * This script runs for quite every page on site
 * By design it should simply initialize some triggers
 */

var doppler_global_js_triggers = {
    bind_lightbox_handlers: function () {
        $('a[href$=".jpg"]')
            .add($('a[href$=".jpeg"]'))
            .add($('a[href$=".png"]'))
            .add($('a[href$=".gif"]'))
            .lightBox(
            {
                fixedNavigation:    true,
                imageLoading:	    '/media/jquery-lightbox/images/lightbox-ico-loading.gif',
                imageBtnPrev:		'/media/jquery-lightbox/images/lightbox-btn-prev.gif',
                imageBtnNext:		'/media/jquery-lightbox/images/lightbox-btn-next.gif',
                imageBtnClose:		'/media/jquery-lightbox/images/lightbox-btn-close.gif',
                imageBlank:			'/media/jquery-lightbox/images/lightbox-blank.gif'
            }
        );
    },

    decorate_tables: function () {
        $('table').not('.unstyled').addClass('table table-striped table-bordered table-condensed');
    }
};

$(function () {
    doppler_global_js_triggers.bind_lightbox_handlers();
    doppler_global_js_triggers.decorate_tables();
});