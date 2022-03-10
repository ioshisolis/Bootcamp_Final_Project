var data = [
    {
      x: [40, 43.6797752809, 93.6797752809, 93.6797752809, 93.6797752809], 
      y: [26.79528403, 76.79528403, 28.8888888889, 60, 85.5555555556], 
      mode: "text", 
      name: "y", 
      text: [$Tweet1, $Tweet2, $Tweet3, $Tweet4, $Tweet5],
      textsrc: "tarzzz:616:bafb6b", 
      type: "scatter", 
      xsrc: "tarzzz:616:512d04", 
      ysrc: "tarzzz:616:da6e5c"
    }
  ];
  var layout = {
    annotations: [
      {
        x: 40, 
        y: 26.79528403, 
        showarrow: false, 
        text: $user1
      }, 
      {
        x: 43.6797752809, 
        y: 76.79528403, 
        showarrow: false, 
        text: $user2
      }, 
      {
        x: 80, 
        y: 28.8888888889, 
        showarrow: false, 
        text: $user3
      }, 
      {
        x: 80, 
        y: 60, 
        showarrow: false, 
        text: $user4
      }, 
      {
        x: 80, 
        y: 85.5555555556, 
        showarrow: false, 
        text: $user5
      }, 
    ], 
    height: 600, 
    hovermode: "closest", 
    shapes: [
      {
        fillcolor: "rgb(9,42,92)", 
        line: {width: 2}, 
        type: "rect", 
        x0: 0.0, 
        x1: 51, 
        y0: 0.0, 
        y1: 60
      }, 
      {
        fillcolor: "rgb(0,255,205)", 
        line: {width: 2}, 
        type: "rect", 
        x0: 0.0, 
        x1: 51, 
        y0: 60, 
        y1: 100.0
      }, 
      {
        fillcolor: "rgb(9,42,92)", 
        line: {width: 2}, 
        type: "rect", 
        x0: 51, 
        x1: 100.0, 
        y0: 0.0, 
        y1: 42
      }, 
      {
        fillcolor: "rgb(0,255,205)", 
        line: {width: 2}, 
        type: "rect", 
        x0: 51, 
        x1: 100.0, 
        y0: 42, 
        y1: 76.2962962963
      }, 
      {
        fillcolor: "rgb(9,42,92)", 
        line: {width: 2}, 
        type: "rect", 
        x0: 51, 
        x1: 100.0, 
        y0: 76.2962962963, 
        y1: 100
      }
    ], 
    width: 1000, 
    xaxis: {
      showgrid: false, 
      zeroline: false
    }, 
    yaxis: {
      showgrid: false, 
      zeroline: false
    }
  };
  var graphOptions = {layout: layout};
  Plotly.newPlot('myDiv', data, layout, {showSendToCloud: true});