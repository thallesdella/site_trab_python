/*
 * Biblioteca de eventos jQuery do Trabalho de Programação em Python 2018.2
 * Created on : 06/01/2016, 11:15:16
 * Author     : UpInside Treinamentos
 */

$(function () {
    //MOBILE MENU CONTROL
    $('.mobile_menu').click(function () {
        if ($('.dashboard_nav, .dashboard_nav_normalize').css('left') !== '-220px') {
            $('.dashboard_nav, .dashboard_nav_normalize').animate({left: '-220px'}, 300);
            $('.dashboard_fix').animate({'margin-left': '0px'}, 300);
        } else {
            $('.dashboard_nav, .dashboard_nav_normalize').animate({left: '0px'}, 300);
            $('.dashboard_fix').animate({'margin-left': '220px'}, 300);
        }
    });

    if ($(window).outerWidth() < '480') {
        $.getScript('jquery.mobile.js', function () {
            $(window).on("swipeleft", function () {
                if ($('.dashboard_nav, .dashboard_nav_normalize').css('left') !== '-220px') {
                    $('.dashboard_nav, .dashboard_nav_normalize').animate({left: '-220px'}, 300);
                    $('.dashboard_fix').animate({'margin-left': '0px'}, 300);
                }
            });

            $(window).on("swiperight", function () {
                if ($('.dashboard_nav, .dashboard_nav_normalize').css('left') === '-220px') {
                    $('.dashboard_nav, .dashboard_nav_normalize').animate({left: '0px'}, 300);
                    $('.dashboard_fix').animate({'margin-left': '220px'}, 300);
                }
            });
        });
    }
});