scroll_autohide = function (obj, el) {
    el.on("scroll", _.throttle(function(e) {
        // cancel the scroll timeout
        if (obj.scroll_timeout) {
            clearTimeout(obj.scroll_timeout);
        }

        el.addClass("scrolling", 1000);
        obj.scroll_timeout = setTimeout(function() {
            el.removeClass("scrolling", 1000);
        }, 1000);
    }, 100));
}
