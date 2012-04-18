// lightbox for every image link
$(function () {
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

//	$('.slider').nivoSlider();
	$('.slider').each(function () {
		var $slider = $(this);
		var $images = $slider.children('img');
		var total_images = $images.size();
		if (total_images > 1) {
			var i = 1;
			$images.each(function () {
				var $img = $(this);
				$img.data('i', i++);
			});
			const INTERVAL = 5000;
			i = 1;
			setInterval(function () {
				$images.each(function () {
					var $img = $(this);
					if ($img.data('i') == i) {
						$img.filter(':hidden').fadeIn(INTERVAL * 0.125);
					}
					else {
						$img.filter(':visible').fadeOut(INTERVAL * 0.275);
					}
				});
				i++;
				if (i > total_images) {
					i = 1;
				}
			}, INTERVAL)
		}
	});

	$('ul.works > li > a').hover(
		function () {
			var $a = $(this);
			if ( ! $a.data('hovered')) {
				$a.data('hovered', true);
				$a.transition({ scale: 1.1 }, function () {
					$(this).data('hovered', false);
				});
			}
		},
		function () {
			var $a = $(this);
			$a.data('unhovered', true);
			$a.transition({ scale: 1/1.1 }, function () {
				$(this).data('unhovered', false);
			});
		}
	)
});