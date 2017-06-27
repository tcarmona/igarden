jQuery( document ).ready(function() {
	function refresh_circles() {
	  var channel_id = "293365";
	  jQuery.get("https://api.thingspeak.com/channels/" + channel_id + "/fields/3/last.txt", function(data) {
	    var umidity = Circles.create({
		  id:                  'circles-hum',
		  radius:              60,
		  value:               data,
		  maxValue:            100,
		  width:               10,
		  text:                function(value){return value + '%';},
		  colors:              ['#236267', '#012F34'],
		  duration:            400,
		  wrpClass:            'circles-wrp',
		  textClass:           'circles-text',
		  valueStrokeClass:    'circles-valueStroke',
		  maxValueStrokeClass: 'circles-maxValueStroke',
		  styleWrapper:        true,
		  styleText:           true
	    });
	  });
	  jQuery.get("https://api.thingspeak.com/channels/" + channel_id + "/fields/1/last.txt", function(data) {
	    var lum = Circles.create({
		  id:                  'circles-lum',
		  radius:              60,
		  value:               data,
		  maxValue:            100,
		  width:               10,
		  text:                function(value){return value + '%';},
		  colors:              ['#AAA839', '#555300'],
		  duration:            400,
		  wrpClass:            'circles-wrp',
		  textClass:           'circles-text',
		  valueStrokeClass:    'circles-valueStroke',
		  maxValueStrokeClass: 'circles-maxValueStroke',
		  styleWrapper:        true,
		  styleText:           true
	    });
	  });
	}

	refresh_circles();
	var write_key = "PKD0HUN3RFC9J68T";
	jQuery("#coberto").change(function() {
	  if(jQuery(this).prop('checked')) {
            jQuery.post( "https://api.thingspeak.com/update" , "key=" + write_key + "&field5=1")
	  }
	  else {
            jQuery.post( "https://api.thingspeak.com/update" , "key=" + write_key + "&field5=0")
	  }
	});
	jQuery("#irrigar").click(function() {
          jQuery.post( "https://api.thingspeak.com/update" , "key=" + write_key + "&field6=1")
	});
});
