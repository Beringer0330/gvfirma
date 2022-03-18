jQuery(document).ready(function ($) {
	"use strict";
	//  TESTIMONIALS CAROUSEL HOOK
	$('#customers-asocia').owlCarousel({
		loop: true,
		center: true,
		items: 3,
		margin: 0,
		autoplay: true,
		dots: true,
		autoplayTimeout: 8500,
		smartSpeed: 300,
		responsive: {
			0: {
				items: 1
			},
			768: {
				items: 2
			},
			1170: {
				items: 3
			}
		}
	});
});

jQuery(document).ready(function ($) {
	"use strict";
	//  TESTIMONIALS CAROUSEL HOOK
	$('#customers-sector').owlCarousel({
		loop: true,
		center: true,
		items: 3,
		margin: 0,
		autoplay: true,
		dots: true,
		autoplayTimeout: 8500,
		smartSpeed: 300,
		responsive: {
			0: {
				items: 1
			},
			768: {
				items: 2
			},
			1170: {
				items: 3
			}
		}
	});
});

jQuery(document).ready(function ($) {
	"use strict";
	//  TESTIMONIALS CAROUSEL HOOK
	$('#customers-testimonials').owlCarousel({
		loop: true,
		center: true,
		items: 3,
		margin: 0,
		autoplay: true,
		dots: true,
		autoplayTimeout: 8500,
		smartSpeed: 300,
		responsive: {
			0: {
				items: 1
			}
		}
	});
});

$('#clients .owl-carousel').owlCarousel({
	loop: true,
	margin: 10,
	nav: true,
	navText: [

	],
	autoplay: true,
	autoplayHoverPause: true,
	responsive: {
		0: {
			items: 1
		},
		600: {
			items: 3
		},
		1000: {
			items: 5
		}
	}
});

function readUrl(input) {

	if (input.files && input.files[0]) {
		let reader = new FileReader();
		reader.onload = e => {
			let imgData = e.target.result;
			let imgName = input.files[0].name;
			input.setAttribute("data-title", imgName);
			console.log(e.target.result);
		};
		reader.readAsDataURL(input.files[0]);
	}

};

function enableSending() {
	document.loginform.submit.disabled = !document.loginform.chec_tra.checked;
};