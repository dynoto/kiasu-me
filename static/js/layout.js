$(document).ready(function(){
	$(document).foundation();
	$('.search_box a').click(function(){
		$('.search_box > form').submit();
	});


	$('.full_image').height($('html').height()+200);
	$('.full_image img').load(function(){
		var scr_h = window.innerHeight;
		var img_h = $(this).height();
		var diff = (scr_h - img_h) / 2;
		$('.full_image > div').css('padding-top',diff);
		$(this).css('opacity',1);
	});

	$('.deal_thumbnail').click(function(){
		var did = $(this).attr('deal_id');
		var src = $(this).attr('full_src');
		$('.full_image img').hide();
		if ( $('.full_image img#'+did).length > 0 ){
			$('.full_image img#'+did).show();
		}else{
			var elem = "<img id='"+did+"'' src='"+src+"'>";
			$('.full_image div').append(elem);
		}
		$('.full_image').css('display','block');
		$('.full_image > div').css('top',$(document).scrollTop());

		// $('.full_image img').attr('src',$(this).attr('full_src'));
		// $('.full_image').css('display','block');
		// $('.full_image > div').css('top',$(document).scrollTop());
		// $('.full_image img').css('opacity',0);

		// $('.full_image').css('top',top);
	});

	$('.full_image').click(function(){
		$(this).hide();
		$(this).children('img').hide();
	});

	// var jobrunner = setTimeout(function() {
	// 	if($.cookie('f1_ks_run')=='1'){
	// 		if (window.google_jobrunner==undefined && ($('#google-ads-1').length != 0)){
	// 			if($.cookie('e_1_temp')!='1'){
	// 		 		window.location = '/sorry/';
	// 			}
	// 		}
	// 	}else{
	// 		$.cookie('f1_ks_run','1',{expires:365, path:'/'});
	// 	}
	// }, 10000);
});

//INPUT CRSF
function csrfSafeMethod(method) {
// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
var csrftoken = $.cookie('csrftoken');
$.ajaxSetup({
crossDomain: false, // obviates need for sameOrigin test
beforeSend: function(xhr, settings) {
	if (!csrfSafeMethod(settings.type)) {
		xhr.setRequestHeader("X-CSRFToken", csrftoken);
	}
}
});

//FACEBOOK
(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=139156246267349";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

//TWITTER
!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');
