var umidity = Circles.create({
          id:                  'circles-hum',
          radius:              60,
          value:               42,
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
var lum = Circles.create({
          id:                  'circles-lum',
          radius:              60,
          value:               66,
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
