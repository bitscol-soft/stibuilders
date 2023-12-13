(function ($) {

    $(document).ready(function () {

        $('.slides').lightSlider({
            gallery: true,
            item: 1,
            loop: true,
            slideMargin: 0,
            thumbItem: 8,
        });
        $('.floor-slides').lightSlider({
            gallery: true,
            item: 1,
            loop: true,
            slideMargin: 0,
            thumbItem: 8,
        });

        $('#bathroom-range').val(null);
        $('#bedroom-range').val(null);

       
    });

    $("#grid-active-btn").click(function() {
        $("#list-filter").addClass("d-none");
        $("#grid-filter").removeClass("d-none");
    });
    $("#list-active-btn").click(function() {
        $("#grid-filter").addClass("d-none");
        $("#list-filter").removeClass("d-none");
    });

    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    })
   

    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();


    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.nav-bar').addClass('sticky-top');
        } else {
            $('.nav-bar').removeClass('sticky-top');
        }
    });


    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
        return false;
    });


    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: true,
        loop: true,
        nav: true,
        navText: [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });

   
    // Aminities Carousel
    $(".owl-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        items: 4,
        loop: true,
        nav: true,
        navText: [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 24,
        dots: false,
        loop: true,
        nav: true,
        navText: [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsive: {
            0: {
                items: 1
            },
            992: {
                items: 2
            }
        }
    });

    // Testimonials carousel
    $(".video-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 24,
        dots: false,
        loop: true,
        nav: true,
        navText: [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsive: {
            0: {
                items: 1
            },
            992: {
                items: 1
            }
        }
    });

    // Range Slider
    $('#price-range').jRange({
        from: 1000,
        to: 5000,
        step: 1000,
        format: '%s',
        scale: [1000, 2000, 3000, 4000, 5000],
        width: '95%',
        showLabels: true,
        isRange: true,
    });
 
   

    // Range Slider
    $('#bedroom-range').jRange({
        from: 1,
        to: 5,
        step: 1,
        scale: [1, 2, 3, 4, 5],
        format: '%s',
        width: '95%',
        value:null,
        showLabels: true,
        isRange: false
    });


    // Range Slider
    $('#bathroom-range').jRange({
        from: 1,
        to: 5,
        step: 1,
        scale: [1, 2, 3, 4, 5],
        format: '%s',
        width: '95%',
        showLabels: true,
        isRange: false
    });




})(jQuery);
