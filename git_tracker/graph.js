		$.plot("#placeholder-$num", 
        [
            {bars: {barWidth: $bar_width, show: true}, data: $syntax_data },
            {lines: {show: true}, points: {show:true}, color: 'blue', data: $line_data, yaxis:2}
        ]
        ,options);

        $("#placeholder-$num").bind("plothover", function (event, pos, item) {

				if (item) {
					var x = item.datapoint[0].toFixed(2),
						y = item.datapoint[1].toFixed(2);

					$("#tooltip").html(y + " lines")
						.css({top: item.pageY+5, left: item.pageX+5})
						.fadeIn(200);
				} else {
					$("#tooltip").hide();
				}
		});
