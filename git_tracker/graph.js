		$.plot("#placeholder-$num", 
        [
            {bars: {barWidth: $bar_width, show: true}, data: $syntax_data },
            {lines: {show: true}, points: {show:true}, color: 'blue', data: $line_data}
        ]
        ,options);
