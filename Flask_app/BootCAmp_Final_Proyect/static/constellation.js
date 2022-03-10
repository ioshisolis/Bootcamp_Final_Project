
if (!window.requestAnimationFrame) {
    window.requestAnimationFrame = (window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.msRequestAnimationFrame || window.oRequestAnimationFrame || function (callback) {
        return window.setTimeout(callback, 1000 / 60);
    });
}

$(window).load(function() {

    setTimeout(function() {
    
        var onMobile = false;
        if( /Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent) ) { onMobile = true; }
        
        if( ( onMobile === false ) ) {
           
            // Init plugin
            $('#constellation').constellation({});
            
        } else {
                
                
            }    
    }, 2000);
    
});


(function ($, window) {

    function Constellation (canvas, options) {
        var $canvas = $(canvas),
            context = canvas.getContext('2d'),
            defaults = {
                star: {
                    color: 'rgba(37, 150, 190, .9)',
                    width: 2
                },
                line: {
                    color: '#00ffcd',
                    width: 0.3
                },
                position: {
                    x: canvas.width * 1,
                    y: canvas.height * 0.5
                },
                width: window.innerWidth,
                height: window.innerHeight,
                velocity: 0.4,
                length: 100,
                distance: 200,
                radius: 120,
                stars: []
            },
            config = $.extend(true, {}, defaults, options);

        function Star () {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;

            this.vx = (config.velocity - (Math.random() * 0.5));
            this.vy = (config.velocity - (Math.random() * 0.5));

            this.radius = Math.random() * config.star.width;
        }

        Star.prototype = {
            create: function(){
                context.beginPath();
                context.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
                context.fill();
            },

            animate: function(){
                var i;
                for (i = 0; i < config.length; i++) {

                    var star = config.stars[i];

                    if (star.y < 0 || star.y > canvas.height) {
                        star.vx = star.vx;
                        star.vy = - star.vy;
                    } else if (star.x < 0 || star.x > canvas.width) {
                        star.vx = - star.vx;
                        star.vy = star.vy;
                    }

                    star.x += star.vx;
                    star.y += star.vy;
                }
            },

            line: function(){
                var length = config.length,
                    iStar,
                    jStar,
                    i,
                    j;

                for (i = 0; i < length; i++) {
                    for (j = 0; j < length; j++) {
                        iStar = config.stars[i];
                        jStar = config.stars[j];

                        if (
                            (iStar.x - jStar.x) < config.distance &&
                            (iStar.y - jStar.y) < config.distance &&
                            (iStar.x - jStar.x) > - config.distance &&
                            (iStar.y - jStar.y) > - config.distance
                        ) {
                            if (
                                (iStar.x - config.position.x) < config.radius &&
                                (iStar.y - config.position.y) < config.radius &&
                                (iStar.x - config.position.x) > - config.radius &&
                                (iStar.y - config.position.y) > - config.radius
                            ) {
                                context.beginPath();
                                context.moveTo(iStar.x, iStar.y);
                                context.lineTo(jStar.x, jStar.y);
                                context.stroke();
                                context.closePath();
                            }
                        }
                    }
                }
            }
        };

        this.createStars = function () {
            var length = config.length,
                star,
                i;

            context.clearRect(0, 0, canvas.width, canvas.height);

            for (i = 0; i < length; i++) {
                config.stars.push(new Star());
                star = config.stars[i];

                star.create();
            }

            star.line();
            star.animate();
        };

        this.setCanvas = function () {
            canvas.width = config.width;
            canvas.height = config.height;
        };

        this.setContext = function () {
            context.fillStyle = config.star.color;
            context.strokeStyle = config.line.color;
            context.lineWidth = config.line.width;
        };

        this.loop = function (callback) {
            callback();

            window.requestAnimationFrame(function () {
                this.loop(callback);
            }.bind(this));
        };

        this.bind = function () {
            $(window).on('mousemove', function(e){
                config.position.x = e.pageX - $canvas.offset().left;
                config.position.y = e.pageY - $canvas.offset().top;
            });
        };

        this.init = function () {
            this.setCanvas();
            this.setContext();
            this.loop(this.createStars);
            this.bind();
        };
    }

    $.fn.constellation = function (options) {
        return this.each(function () {
            var c = new Constellation(this, options);
            c.init();
        });
    };
})($, window);
