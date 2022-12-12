/* Javascript for MyXBlock. */

let content = $('.collapse-content')
let contentHeight = content.css('height')

$('.collapse-button').click( function() {

    if (content.height() > 0) {
        content.animate({'height': 0, 'opacity': 0}, 300);
    }
    else {
        content.animate({'height': contentHeight, 'opacity': 1}, 300);
    }

});

