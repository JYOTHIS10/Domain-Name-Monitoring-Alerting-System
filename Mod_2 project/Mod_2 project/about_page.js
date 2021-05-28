// about page

$(document).ready(function() {

		// $("set1").hide();
		// $("set2").hide();
		// $("set3").hide();


		$(".pic1").on({
		mouseenter: function() {
		$(".set1").delay(1000);
		},

		mouseenter: function() {
		$(".set1").fadeToggle(1000);
		},

		mouseleave: function() {
		$(".set1").fadeOut(1000);
		}
	});

		$(".pic2").on({

		mouseenter: function() {
		$(".set2").delay(1000);
		},

		mouseenter: function() {
		$(".set2").fadeToggle(1000);
		},

		mouseleave: function() {
		$(".set2").fadeOut(1000);
		}
	});

		$(".pic3").on({

		mouseenter: function() {
		$(".set3").delay(1000);
		},

		mouseenter: function() {
		$(".set3").fadeToggle(1000);
		},

		mouseleave: function() {
		$(".set3").fadeOut(1000);
		}
	});
		
});

// $("p").on({
//   mouseenter: function(){
//     $(this).css("background-color", "lightgray");
//   }, 
//   mouseleave: function(){
//     $(this).css("background-color", "lightblue");
//   }, 
//   click: function(){
//     $(this).css("background-color", "yellow");
//   } 
// });