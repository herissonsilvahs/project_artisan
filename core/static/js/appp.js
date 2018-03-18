let isMenuOpened = false;
let isDimmerVisible = false;

let tlToggleMenu = new TimelineLite({paused: true});
tlToggleMenu.add(tlMenuIcon()).add(tlMenu(), "-=0.7");

let tlSearchButton = new TimelineLite({paused: true});
tlSearchButton.add(tlSearch());

function tlMenuIcon() {
    let tlMenuIcon = new TimelineLite();
    tlMenuIcon.add(TweenMax.staggerTo('.menu-btn__rect:not(.menu-btn__rect--diag)', 0.2, {
        transform: 'translateX(60px)',
        opacity: 0,
        ease: Power2.easeInOut
    }, 0.1));
    tlMenuIcon.add(TweenLite.to('.menu-btn__rect--diag', 0.5, {
        width: "100%",
        opacity: 1,
        ease: Power2.easeInOut
    }), "0.4");
    return tlMenuIcon
}

function tlMenu() {
    let tlMenu = new TimelineLite();
    tlMenu.add(TweenLite.to('.menu', 1, {transform: 'scaleY(1)', ease: Power3.easeOut})); //red frontground
    tlMenu.add(TweenLite.to('.menu__bg', 1, {transform: 'scaleY(1)', ease: Power3.easeOut}), "-=0.6"); // blue background
    tlMenu.add(TweenMax.staggerTo('.menu__item', 0.5, {transform: 'translateX(5px)', opacity: 1}, 0.2), 0.5);
    return tlMenu
}

function tlSearch() {
    let tlSearch = new TimelineLite();
    let cardHeight = $('.card--search').height();
    tlSearch.add(TweenLite.to('.dimmer', 0.4, {opacity: 1, pointerEvents: 'auto', ease: Power2.easeOut}));
    tlSearch.add(TweenLite.to('.card--search', 0.4, {transform: `translateY(-${cardHeight}px)`, ease: Power2.easeOut}),"-=0.2");
    return tlSearch
}


$('.menu-btn').click(function () {

    if (isMenuOpened) {
        $('html, body').css('overflow-y', 'initial');
        tlToggleMenu.reverse();
        isMenuOpened = false;
    } else {
        $('html, body').css('overflow-y', 'hidden'); //todo: execute this only when animation ends
        tlToggleMenu.play();
        isMenuOpened = true
    }
});

$('.search').click(function () {
    tlSearchButton.play();
    isDimmerVisible = true;
});

$('.dimmer').click(function () {
    tlSearchButton.reverse();
    isDimmerVisible = false;
});


// transform: 'matrix(0.70711, 0.7071, -0.7071, 0.70711, 0, 0)'
