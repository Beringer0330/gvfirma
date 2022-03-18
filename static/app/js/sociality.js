var buttons = $('.buttonso-wrap .buttonso');
    for (var i = 0; i < buttons.length; i++) {
        $(buttons[i]).attr('style', 'z-index:' + (i * 10) + '; --activeBottom: ' + ((i + 1) * 60) + 'px; --activeDuration: ' + ((i + 1) * 0.2) + 's;');
    }

    $('.button-toggle a').click(function() {
        $(this).parent().parent().toggleClass('active');
        return false;
    });