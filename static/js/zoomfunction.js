<html>
  <head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
        <script>
        var currFFZoom = 1;
        var currIEZoom = 100;

        function plus(){
            //alert('sad');
                var step = 0.02;
                currFFZoom += step;
                $('body').css('MozTransform','scale(' + currFFZoom + ')');
                var stepie = 2;
                currIEZoom += stepie;
                $('body').css('zoom', ' ' + currIEZoom + '%');

        };
        function minus(){
            //alert('sad');
                var step = 0.02;
                currFFZoom -= step;
                $('body').css('MozTransform','scale(' + currFFZoom + ')');
                var stepie = 2;
                currIEZoom -= stepie;
                $('body').css('zoom', ' ' + currIEZoom + '%');
        };
    </script>
    </head>
<body>
<!--zoom controls-->
                        <a id="minusBtn" onclick="minus()">------</a>
                        <a id="plusBtn" onclick="plus()">++++++</a>
  </body>
</html>
